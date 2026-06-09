from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def showType(self):
        pass

class CoolingDevice:
    def cool(self):
        print("Cooling items inside fridge")

class WiFiEnabled:
    def connectWiFi(self):
        print("Connected to WiFi")

class SmartFridge(Appliance, CoolingDevice, WiFiEnabled):
    def showType(self):
        print("This is a Smart Fridge")

fridge = SmartFridge()
fridge.showType()
fridge.cool()
fridge.connectWiFi()