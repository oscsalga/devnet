# Webex Clone Using WEBEX REST API

from PyQt5 import QtCore, QtGui, QtWidgets
from webexteamssdk import WebexTeamsAPI
import requests
import sys


class Ui_OpenWeather(object):
    token = "ZDk3ZTg0N2ItY2JlMS00ZWNhLTg3YzctYjUxNTdmNTE0Y2VlMGZiMDQyZTctZDhi_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
    urlRooms = "https://webexapis.com/v1/rooms"
    urlMessages = "https://webexapis.com/v1/messages?roomId="
    headers = {"Application": "application/json",
               "Authorization": "Bearer " + token}
    rooms = {}
    maxMessages = 50

    def itemActivated_event(self, item, index):
        url = self.requestData(self.urlMessages + self.rooms[index]["id"] + "&max=" + str(self.maxMessages))["items"]
        self.listWidget2.clear()
        num = len(url)
        for x in range(0, num):
            #print(x)
            try:
                self.listWidget2.addItem(str(x))
                self.listWidget2.addItem(url[x]["personEmail"])
                self.listWidget2.addItem(url[x]["text"])
                self.listWidget2.addItem("*" * 30)
                self.listWidget2.addItem("\n")
            except Exception as e:
                self.listWidget2.addItem("Message is a File")
                self.listWidget2.addItem("*" * 30)
                self.listWidget2.addItem("\n")
                pass

    def requestData(self, url):
        r = requests.get(url, headers=self.headers)
        if r.status_code == 200:
            return r.json()
        else:
            sys.exit()

    def setupUi(self, OpenWeather):
        OpenWeather.setObjectName("OpenWeather")
        OpenWeather.resize(884, 560)

        self.listWidget = QtWidgets.QListWidget(OpenWeather)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 361, 531))
        self.listWidget.setObjectName("listWidget")

        self.listWidget2 = QtWidgets.QListWidget(OpenWeather)
        self.listWidget2.setGeometry(QtCore.QRect(370, 10, 500, 531))
        self.listWidget2.setObjectName("listWidget")

        self.rooms = self.requestData(self.urlRooms)["items"]

        for room in self.rooms:
            self.listWidget.addItem(room["title"])

        self.listWidget.itemClicked.connect(lambda item: self.itemActivated_event(item, self.listWidget.currentRow()))

        self.retranslateUi(OpenWeather)
        QtCore.QMetaObject.connectSlotsByName(OpenWeather)

    def retranslateUi(self, OpenWeather):
        _translate = QtCore.QCoreApplication.translate
        OpenWeather.setWindowTitle(_translate("WebexClone", "WebexClone"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenWeather = QtWidgets.QWidget()
    ui = Ui_OpenWeather()
    ui.setupUi(OpenWeather)
    OpenWeather.show()
    sys.exit(app.exec_())
