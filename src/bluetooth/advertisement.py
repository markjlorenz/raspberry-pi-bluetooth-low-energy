from dasbus.typing             import *
from dasbus.server.interface   import dbus_interface
from dasbus.server.template    import InterfaceTemplate
from dasbus.server.publishable import Publishable

from bluetooth.service                   import Service

class Advertisement(Publishable):

    PATH = "/com/raspberrypi-bluetooth/Thermometer/Advertisement/1"

    def for_publication(self):
        return AdvertisementInterface(self)

@dbus_interface("org.bluez.LEAdvertisement1")
class AdvertisementInterface(InterfaceTemplate):

    def Release(self) -> None:
        print("released")

    @property
    def Type(self) -> Str:
        return "peripheral"

    @property
    def ServiceUUIDs(self) -> List[Str]:
        return [Service.UUID]

    @property
    def Discoverable(self) -> Bool:
        return True

    @property
    def Includes(self) -> List[Str]:
        return ["tx-power"]

    @property
    def LocalName(self) -> Str:
        return "Thermometer Device"

    # https://specificationrefs.bluetooth.com/assigned-values/Appearance%20Values.pdf
    @property
    def Appearance(self) -> UInt16:
        return 768 # Thermometer

    @property
    def MinInterval(self) -> UInt32:
        return 0

    @property
    def MaxInterval(self) -> UInt32:
        return 0
