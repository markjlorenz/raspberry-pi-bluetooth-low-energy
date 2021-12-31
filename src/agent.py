from dasbus.typing             import *
from dasbus.server.interface   import dbus_interface
from dasbus.server.publishable import Publishable
from dasbus.server.template    import InterfaceTemplate

from dasbus.connection         import SystemMessageBus

class Agent(Publishable):
    PATH = "/com/raspberrypi-bluetooth/Thermometer/Agent/1"

    def for_publication(self):
        return AgentInterface(self)

@dbus_interface("org.bluez.Agent1")
class AgentInterface(InterfaceTemplate):

    def Release(self) -> None:
        print("release")
        pass

    def AuthorizeService(self, device: ObjPath, uuid: Str) -> None:
        print("authorize service")
        pass

    def RequestPinCode(self, device: ObjPath) -> Str:
        print("request pin code")
        pass

    def RequestPassKey(self, device: ObjPath) -> UInt32:
        print("request pass key")
        pass

    def DisplayPinCode(self, device: ObjPath, pin_code: Str) -> None:
        print("display pin code")
        pass

    def RequestConfirmation(self, device: ObjPath, pass_key: UInt32) -> None:
        print("request confimration")
        pass

    def RequestConfirmation(self, device: ObjPath, pass_key: UInt32) -> None:
        print("request confimration")
        pass

    def RequestAuthorization(self, device: ObjPath) -> None:
        print("request authorization")
        bus = SystemMessageBus()
        bus.get_proxy("org.bluez", device) \
            .Set("org.bluez.Device1", "Trusted",  Variant("b", True))
        pass

    def Cancel(self) -> None:
        print("request authorization")
        pass
