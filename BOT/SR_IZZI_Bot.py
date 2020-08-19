# -*- coding: utf-8 -*-
from borg3.result import ResultList, Result, Severity
from datetime import datetime
from pytz import timezone
import requests
import json
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

token = "NDg4NDQ3YWEtNjkyNC00ZGI5LTkwODQtOTZhMTliNmE1MWM4YmI2MWIwMjctZTZm_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
roomID = "Y2lzY29zcGFyazovL3VzL1JPT00vZDMyYzdhY2EtYTg1ZC0zYzNhLWIzZjMtNmU1MTBmODViYWUy"
emailList = ["@izzi.mx"]
fixed_contract_id = ["10000201673992", "200994944", "200998434", "200998451", "200998453", "201001054",
                     "201029449", "201872033", "202221453", "202369173", "202643856", "93311039", "94594589",
                     "94596454"]


def task(env):
    return sendMessage("Testing Izzi: " + fecha())


def sendMessage(mensaje):
    headers = {'Authorization': 'Bearer ' + token}
    sr = {"roomId": roomID,
          "markdown": mensaje}
    try:
        r = requests.post('https://api.ciscospark.com/v1/messages',
                          data=sr, headers=headers)
        return mensaje
    except Exception as e:
        pass


def fecha():
    mxTimeZone = timezone('America/Mexico_City')
    mxTime = datetime.now(mxTimeZone)
    mxTime = mxTime.strftime('%H:%M:%S')
    return mxTime


def borg_module(env, meta_data, cisco_service_request):
    """Check cases and sends to Spark room for IZZI."""
    rl = ResultList()
    SR_meta = meta_data['case']

    """Gathering SR details"""
    sr = SR_meta["CaseNumber"]
    title = SR_meta["Title"]
    sev = SR_meta["Severity"]
    customer = SR_meta["Customer_Company_Name__c"]
    owner = SR_meta["Owner"]
    owner_queue = SR_meta["Owner_Queue__c"]
    queue = SR_meta["Queue"]
    status = SR_meta["Status"]
    prev_queue = SR_meta["Previous_Queue__c"]
    workgroup = SR_meta["Workgroup__c"]
    contract_id = str(SR_meta["ContractId"])
    current_contact_mail = SR_meta["Current_Contact_Email__c"]
    # device = str(meta_data["case"])
    """Define when to alert, on engineer change and creation"""
    change_type = SR_meta["ChangeType"]
    change_types_to_run_on = ["TACENGINEER_CHANGED"]

    #######################################################
    try:

        if (contract_id in fixed_contract_id) or (current_contact_mail in emailList):
            if (owner == "NULL"):
                owner = "CSE yet to pick this case."
            fast_start = ''
            golden_line = ''
            case_note = ''
            fast_start, sr_owner, sr_prev_owner, golden_line, case_note = get_case_details(cisco_service_request)

            if status == "New":
                change_type = 'New'
            elif (status == "Requeue"):
                if sr_prev_owner and sr_owner:

                    if str(sr_prev_owner) == "UNDISPATCHED":
                        change_type = "Requeued to " + str(sr_owner)
                    else:
                        change_type = "Requeued from " + \
                                      str(sr_prev_owner) + " to " + str(sr_owner)

                elif (status == "Requeue" and prev_queue == 'unknown'):
                    change_type = "Requeued to " + owner_queue

                elif (status == "Requeue" and prev_queue != owner_queue):
                    change_type = "Requeued from " + prev_queue + " to " + owner_queue

            sr_with_link = "<a href='https://scripts.cisco.com/app/quicker_csone/?sr=" + \
                           sr + "' target='_blank'>" + sr + "</a>"
            owner_with_link = "<a href='https://directory.cisco.com/dir/reports/" + \
                              owner + "' target='_blank'>" + owner + "</a>"

            if fast_start == "Service Capability: Fast Start":
                fast_start = "**Service Capability: Fast Start** <br/>"
            else:
                fast_start = ''

            if ((status == "New") or (status == "Requeue") or (status == "Closed")):
                note = "<br/>" + "**NOTE:** " + 'Please make sure that you go through the "GOLDEN RULES" for the SR#' + \
                       sr + ', before sending the mail to the Client.' + "<br/>---"
            else:
                note = "<br/>***---"

            data = "---<br/>***IZZI<br/>" + "**Time:** " + fecha() + "<br/>" + fast_start + "**SR:** " + sr_with_link + "<br/>" + "**Title:** " + title + "<br/>" + "**Sev:** <b>" + sev + \
                   "</b><br/>" + "**Contract ID:** <b>" + contract_id + "</b><br/>" + "**Customer:** " + \
                   customer + "<br/>" + "**Status:** " + change_type + \
                   "<br/>" + "**Owner:** " + owner_with_link + note

            sendMessage(data)

        if (change_type.strip().upper() in change_types_to_run_on) and \
                ((contract_id in fixed_contract_id) or (current_contact_mail in emailList)):

            URL = "http://orgstats.cisco.com/api/1/entries?users="
            r = requests.get(URL + owner)
            user_list = r.json()
            if not len(user_list):
                return rl

            fast_start = ''
            golden_line = ''
            case_note = ''
            fast_start, sr_owner, sr_prev_owner, golden_line, case_note = get_case_details(cisco_service_request)

        return rl

    except Exception as e:
        emailHtml('bdb_no_reply@cisco.com',
                  'oscsalga@cisco.com', '', 'Error', str(e))
        return rl


def emailHtml(addrFrom, addrTo, addrCc, subject, htmlBody):
    # Mail server
    smtp_server = 'outbound.cisco.com'

    # HTML MIME type email
    msg = MIMEMultipart('alternative')
    msg['To'] = addrTo
    if addrCc:
        msg['Cc'] = addrCc
    msg['From'] = addrFrom
    if subject:
        msg['Subject'] = subject
    if htmlBody:
        txtEmail = MIMEText(htmlBody, 'plain')
        htmlEmail = MIMEText(htmlBody, 'html')
        msg.attach(txtEmail)
        msg.attach(htmlEmail)

    # Send it
    s = smtplib.SMTP(smtp_server)
    s.sendmail(addrFrom, addrTo.split(",") +
               addrCc.split(","), msg.as_string())
    s.quit()


def get_case_details(cisco_service_request):
    try:
        msg = 'Creating field list to be fetched from SR.'
        sr_owner = cisco_service_request.owner
        sr_prev_owner = cisco_service_request.previous_queue
        fast_start = ''
        golden_line = ''
        case_note = ''
        msg = 'Check if status code returned as 200.'
        return fast_start, sr_owner, sr_prev_owner, str(golden_line), str(case_note)
    except Exception as e:
        print('Error while ' + msg)
        print("Unexpected Error:", sys.exc_info()[0], e)
        return e


def addNote(owner, srNumber, note_detail):
    # Adds note to a CSOne Case.
    note_type = "Other"
    note_status = "Internal"
    note_title = "SPECIAL HANDLING INSTRUCTIONS\n"
    ID = 'f44f945ab40f4be4a289636de8e05e36'
    SECRET = 'b15a9961d8FF4BbfB69E8d8737282a5a'
    from PyCSOne.client import CS1Client  # MAMORTEN moved these here for lazy loading performance reasons.
    client = CS1Client(ws_endpoint='https://apx.cisco.com/custcare/cm/v1.0/')
    client.authenticate(client_id=ID, client_secret=SECRET)
    client.logged_id = owner  # env.user_name
    from PyCSOne.case import Case, Note  # MAMORTEN moved these here for lazy loading performance reasons.
    my_case = Case(client, number=srNumber)
    note_detail = "**NOTE:** " + 'Please make sure that you go through the "GOLDEN RULES" for the SR#' + str(
        srNumber) + ', before sending the mail to the Client.' + '\n\n' + note_detail
    new_note = Note({"noteDetail": note_detail, "noteStatus": note_status,
                     "note": note_title, "noteType": note_type})
    try:
        note_added = my_case.add_note(new_note)
    except Exception as e:
        note_added = "Note add Failed." + str(e)
    return note_added