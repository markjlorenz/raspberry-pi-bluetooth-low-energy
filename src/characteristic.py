from dasbus.typing             import *
from dasbus.server.interface   import dbus_interface
from dasbus.server.interface   import dbus_signal
from dasbus.server.publishable import Publishable
from dasbus.server.template    import InterfaceTemplate
from dasbus.server.property    import emits_properties_changed

class Characteristic(Publishable):
    PATH =  "/com/raspberrypi-bluetooth/Thermometer/Characteristic/1"
    UUID =  "4116f8d2-9f66-4f58-a53d-fc7440e7c14e" # hex chars only!

    # Will improve this later.  Other problems to solve now.
    _SERVICE_PATH = "/com/raspberrypi-bluetooth/Thermometer/Service/1"

    def __init__(self):
        self._value = [None]
        super().__init__()

    def for_publication(self):
        return CharacteristicInterface(self)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


@dbus_interface("org.bluez.GattCharacteristic1")
class CharacteristicInterfaceGatt(InterfaceTemplate):

    def ReadValue(self, options: Dict[Str, Variant]) -> List[Byte]:
        print("TRIED TO READ VALUE")
        return self.implementation.value

    @emits_properties_changed
    def WriteValue(self, value: List[Byte], options: Dict[Str, Str]) -> None:
        self.implementation.value = value
        self.report_changed_property('Value')

    def StartNotify(self) -> None:
        print("TRIED START NOTIFY")
        pass

    @property
    def UUID(self) -> Str:
        return Characteristic.UUID

    @property
    def Service(self) -> ObjPath:
        return Characteristic._SERVICE_PATH

    @property
    def Value(self) -> List[Byte]:
        return self.implementation.value


class CharacteristicInterface(CharacteristicInterfaceGatt):

    _UUID = Variant("s", Characteristic.UUID)

    def get_properties(self):
        return {
            "org.bluez.GattCharacteristic1": {
                "Service": Variant("o", Characteristic._SERVICE_PATH),
                "UUID": self._UUID,
                "Flags": Variant.new_array(None, [Variant("s", "read"), Variant("s", "notify")]),
                "Descriptors": Variant.new_array(VariantType("t"), []),
            }
        }
