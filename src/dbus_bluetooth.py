from dasbus.connection         import SystemMessageBus
from dasbus.typing             import *
from dasbus.server.interface   import dbus_interface
from dasbus.server.interface   import dbus_signal
from dasbus.server.publishable import Publishable
from dasbus.server.template    import InterfaceTemplate

from dasbus.loop               import EventLoop
from threading                 import Thread

from bluetooth.application     import Application
from bluetooth.service         import Service
from bluetooth.characteristic  import Characteristic
from bluetooth.advertisement   import Advertisement

from time                      import sleep
from random                    import choice

class BluetoothManager:

    def __init__(self):
        bus = SystemMessageBus()
        Thread(target=EventLoop().run).start()
        bus.register_service("com.raspberrypi-bluetooth.Thermometer")

        proxy = bus.get_proxy("org.bluez", "/org/bluez/hci0")

        proxy.Set("org.bluez.Adapter1", "Powered", Variant("b", True))
        print("Adapter powered: %s" % proxy.Get("org.bluez.Adapter1", "Powered"))

        # We don't need pairing for this application
        proxy.Set("org.bluez.Adapter1", "Pairable", Variant("b", False))

        bus.publish_object(
            Advertisement.PATH,
            Advertisement().for_publication()
        )
        proxy.RegisterAdvertisement(Advertisement.PATH, {})

        self.characteristic = Characteristic().for_publication()
        bus.publish_object(
            Characteristic.PATH,
            self.characteristic
        )

        bus.publish_object(
            Application.PATH,
            Application().for_publication()
        )
        proxy.RegisterApplication(Application.PATH, {})

    def write_value(self, value: List[Byte]) -> None:
        self.characteristic.WriteValue(value, {})

if __name__ == '__main__':
    bm = BluetoothManager()

    # Put out some random values for debugging / testing purposes
    #
    while True:
        bm.write_value(
            [choice([0x01, 0x02, 0x03, 0x04, 0xAB, 0xDE])]
        )
        sleep(0.5)
