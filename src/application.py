from dasbus.typing             import *
from dasbus.server.interface   import dbus_interface
from dasbus.server.publishable import Publishable
from dasbus.server.template    import InterfaceTemplate

from bluetooth.service         import Service, ServiceInterface
from bluetooth.characteristic  import Characteristic, CharacteristicInterface

class Application(Publishable):
    PATH = "/com/raspberrypi-bluetooth/Thermometer/Application/1"

    def for_publication(self):
        return ApplicationInterface(self)

@dbus_interface("org.bluez.GattApplication1")
class ApplicationGattInterface(InterfaceTemplate):
    pass

@dbus_interface("org.freedesktop.DBus.ObjectManager")
class ApplicationInterface(ApplicationGattInterface):

    def GetManagedObjects(self) -> Dict[ObjPath, Dict[Str, Dict[Str, Variant]]]:
        return {
            Service.PATH:        ServiceInterface(Service()).get_properties(),
            Characteristic.PATH: CharacteristicInterface(Characteristic()).get_properties(),
        }
