from dasbus.typing             import *
from dasbus.server.interface   import dbus_interface
from dasbus.server.interface   import dbus_signal
from dasbus.server.publishable import Publishable
from dasbus.server.template    import InterfaceTemplate

from bluetooth.characteristic  import Characteristic

class Service(Publishable):
    PATH = Characteristic._SERVICE_PATH           # will improve later
    UUID = "12634d89-d598-4874-8e86-7d042ee07ba7" # only hex characters!

    def for_publication(self):
        return ServiceInterface(self)

@dbus_interface("org.bluez.GattService1")
class ServiceInterfaceGatt(InterfaceTemplate):

    @property
    def UUID(self) -> Str:
        return Service.UUID

    @property
    def Primary(self) -> Bool:
        return True

class ServiceInterface(ServiceInterfaceGatt):

    _UUID = Variant("s", Service.UUID)

    def get_properties(self):
        return {
            "org.bluez.GattService1": {
                "UUID": self._UUID,
                "Primary": Variant("b", True),
                "Characteristics": Variant.new_array(None, [Variant("o", Characteristic.PATH)]),
            }
        }
