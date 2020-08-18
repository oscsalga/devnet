# -*- coding: utf-8 -*-
from borg3.result import ResultList, Result, Severity
from datetime import datetime, date
from pytz import timezone
import requests
import json
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

token = "NDg4NDQ3YWEtNjkyNC00ZGI5LTkwODQtOTZhMTliNmE1MWM4YmI2MWIwMjctZTZm_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
roomID = "Y2lzY29zcGFyazovL3VzL1JPT00vZDMyYzdhY2EtYTg1ZC0zYzNhLWIzZjMtNmU1MTBmODViYWUy"


def task(env):
    # Authorization for the bot

    headers = {
        'Authorization': 'Bearer ' + token}

    sr = {"roomId": roomID,
          "markdown": "Test"}
    requests.post('https://api.ciscospark.com/v1/messages',
                  json=sr, headers=headers)

    return "Task Function"


def borg_module(env, meta_data, cisco_service_request):
    """Check cases and sends to Spark room for IZZI."""
    rl = ResultList()
    SR_meta = meta_data['case']

    """Authorization for the bot"""
    headers = {
        'Authorization': 'Bearer ' + token}

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
    #device = str(meta_data["case"])
    """Define when to alert, on engineer change and creation"""
    change_type = SR_meta["ChangeType"]
    change_types_to_run_on = ["TACENGINEER_CHANGED"]
    fixed_contract_id = ["200392968",
                         "200839811",
                         "200847263",
                         "200881663",
                         "201059150",
                         "201300226",
                         "201838395",
                         "201838397",
                         "202661387",
                         "203301970",
                         "203301971",
                         "203301972",
                         "203301973",
                         "203301974",
                         "203301975",
                         "203301976",
                         "203301977",
                         "203301978",
                         "203301979",
                         "203301980",
                         "203301981",
                         "203301982",
                         "203301983",
                         "203301984",
                         "203301985",
                         "203301986",
                         "203301987",
                         "203301988",
                         "203301989",
                         "203301990",
                         "92104296",
                         "94964091"]

    golden_rule_comment = """PLEASE DO NOT FORGET TO UPDATE GCI\n\n
In case you take an SR with the following characteristics:\n\n
Customer: Izzi/Cablevision (Mexico)\n
Technology: XR-Routing-Platforms\n
Sub Technology: CRS\n
SW Versions: 5.3.4 / 6.4.2\n
Possible title keywords: Traffic Drops, Low Traffic, Traffic down\n\n
Background:\n
This is a highly escalated incident (ESC01022683 / BEMS01020722 / Main SR 685943823) in which IZZI has multiple CRSs with XR Versions 5.3.4 and 6.4.2, and in random time and random CGSE we see that for +/- 1 hour the traffic drops about 5% to 10% affecting end users with slow navigation or no navigation at all. Without action the traffic recovers.\n\n
Please do not ask for topology, it can be found at https://eportal.cisco.com/#/account/141046/links\n
For more detailed information contact the people in the Main Contacts section\n\n
Logs to be taken\n
When the failure is present, please capture the following logs:\n \n
show logrun on -f node0_1_cpu0 show_nat44_stats\n
Show plim services trace core error location 0/1/CPU0\n
show cgn nat44 NAT44-1 statistics\n
show cgn nat44 NAT44-1 statistics | in resource\n
show cgn nat44 NAT44-1 statistics | in drop\n
sh cgn nat44 nat44-2 mapping outside-address inside-vrf Inside2 start-addr 177.236.48.1 end-addr 177.236.55.254\n
show controllers pse statistics location 0/1/CPU0\n
show captured packets egress location 0/1/CPU0\n
show controllers pse utilization ingress location 0/1/CPU0\n
show controllers pse utilization egress location 0/1/CPU0\n
show controllers egress statistics location 0/1/CPU0\n
show controllers egress resources location 0/1/CPU0\n
show controllers ingress statistics location 0/1/CPU0\n
show controllers ingress backpressure all location 0/1/CPU0\n
show controllers plim asic statistics summary location 0/1/CPU0\n
show controllers fabricq statistics detail location 0/1/CPU0\n
show controllers services driver location 0/1/CPU0\n
Show controller service boot-params location 0/1/CPU0\n
show controllers services ha-config location 0/1/CPU0\n
Show services redundancy brief\n
Show cgn trace master-agent\n
show interface serviceInfra1 accounting\n
show interface serviceapp1 accounting\n
show interface serviceapp1\n
show interface serviceapp1 | in rate\n
show interface serviceapp1 | in drops\n
show interface serviceapp101 accounting\n
show interface serviceapp101\n
show interface serviceapp101 | in rate\n
show interface serviceapp101 | in drops\n
show route vrf INSIDE-CGSE1-SEV\n
show processes blocked location 0/1/CPU0\n
show processes blocked\n
show cgn nat44 NAT44-1 inside-vrf INSIDE-CGSE1-SEV counters\n \n
show tech-support services cgn location 0/2/CPU0 | file harddisk:/cgn\n
show tech-support services svi location 0/2/CPU0 | file harddisk:/svi\n\n
Action Plan to recover services\n
The AP we have until now in order to recover services:\n\n
1. Clear CEF/Route from corresponding affected CGSE from public prefix\n
2. Shut ServiceApp internal and external, wait 30 seg and perform no shut\n
3. Reconfigure CGS Service\n\n
Main Contacts\n\n
Please contact the following HTOM ASAP in the following schedule (all CST , from Monday - Friday):\n
Rafael Rojas (rarojas): 9 - 15 hrs  CT\n
Efrain Abarca (efabarca): 15 - 00 hrs  CT\n
Ricardo Miguel Fernandes Mega Fontes (rmegafon): 00 - 8 hrs  CT\n
Also consider involve the following people:\n
HTTS Main Contact: Diego Zorrilla  9 - 20 hrs(diefierr) CT\n
BU: Nikolay Karpyshev (nkarpysh)"""

    #######################################################
    try:

        if (contract_id in fixed_contract_id) or ("@megacable.com.mx" in current_contact_mail):
            # Getting the local time now
            utc_curr_time = datetime.strptime(datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")
            local_cst_time = str(utc_curr_time.replace(tzinfo=timezone(
                'UTC')).astimezone(timezone('America/Mexico_City')))
            local_date = local_cst_time[:local_cst_time.rfind('-')]

            curr_date = datetime.strptime(str(local_date), "%Y-%m-%d %H:%M:%S")
            local_date = str(datetime.strptime(
                local_date, "%Y-%m-%d %H:%M:%S").date())

            if len(str(curr_date.minute)) == 1:
                minutes = '0' + str(curr_date.minute)
            elif len(str(curr_date.minute)) == 2:
                minutes = str(curr_date.minute)

            time_now = str(curr_date.hour) + ':' + minutes

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

            data = "---<br/>***MEGACABLE<br/>" + "**Time:** " + time_now + "<br/>" + fast_start + "**SR:** " + sr_with_link + "<br/>" + "**Title:** " + title + "<br/>" + "**Sev:** <b>" + sev + \
                   "</b><br/>" + "**Contract ID:** <b>" + contract_id + "</b><br/>" + "**Customer:** " + \
                   customer + "<br/>" + "**Status:** " + change_type + \
                   "<br/>" + "**Owner:** " + owner_with_link + note

            """Set the room to MEGA"""
            sr_json = {
                "roomId": roomID,
                "markdown": data
            }
            requests.post('https://api.ciscospark.com/v1/messages',
                          json=sr_json, headers=headers)

        if (change_type.strip().upper() in change_types_to_run_on) and \
                ((contract_id in fixed_contract_id) or ("@megacable.com.mx" in current_contact_mail) or (
                        "@metrocarrier.com.mx" in current_contact_mail)):

            URL = "http://orgstats.cisco.com/api/1/entries?users="
            r = requests.get(URL + owner)
            user_list = r.json()
            if not len(user_list):
                return rl

            fast_start = ''
            golden_line = ''
            case_note = ''
            fast_start, sr_owner, sr_prev_owner, golden_line, case_note = get_case_details(cisco_service_request)
            """
            try:
                rl.debug("adding case note {}".format(golden_rule_comment))
                ret_stat = addNote(owner, sr, golden_rule_comment)
                golden_line = ''
                for each_line in golden_rule_comment.splitlines():
                    golden_line += each_line + '<br>'
            except Exception as e:
                rl.debug("exception {}".format(e))
                msg = 'Will continue evenif case note giving exception.'

            msg = 'Sending system generated Email to All CSE.'
            body = 'Hi ' + owner + ',' + '<br><br>'
            imp_comment = 'Since you are the current owner of this case, please make sure that you go through the "GOLDEN RULES" for the SR#' + str(
                sr) + ', before sending the mail to the Client. ' + '<br><br>' + golden_line
            body += '<p style="background-color:#FFFF00;color:#B22222"><b> Important Note: ' + \
                '<br>' + '=============<br>' + imp_comment + '</b></p><br><br>'

            subject = 'READONLY IF INCIDENT IS CGSE RELATED: Important Notes for SR#' + str(sr)
            to = str(owner)+'@cisco.com'
            cc = 'fts-izzi@cisco.com'

            rl.debug("sending mail with body {}".format(body))
            emailHtml('bdb_no_reply@cisco.com', to, cc, subject, body)
            """
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