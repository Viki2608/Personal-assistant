import bluetooth
import asyncio
from winrt.windows.devices import radios


async def bluetooth_power(turn_on):
    all_radios = await radios.Radio.get_radios_async()
    for this_radio in all_radios:
        if this_radio.kind == radios.RadioKind.BLUETOOTH:
            if turn_on:
                result = await this_radio.set_state_async(radios.RadioState.ON)
                print("Turned On")
            else:
                result = await this_radio.set_state_async(radios.RadioState.OFF)
                print("Turned Off")


def connect(device_name):
    target_name = device_name
    target_address = None

    nearby_devices = bluetooth.discover_devices()
    asyncio.run(bluetooth_power(True))
    for devices in nearby_devices:
        if target_name == bluetooth.lookup_name(devices):
            target_address = devices
            break

    if target_address is not None:
        print("found target bluetooth device with address ", target_address)
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        print("Trying connection")
        i = 0  # ---- your port range starts here
        max_port = 3  # ---- your port range ends here
        err = True
        while err == True and i <= max_port:
            print("Checking Port ", i)
            port = i
            try:
                sock.connect((target_address, port))
                err = False
                print("Successfully connected")
                break
            except Exception:
                print("Exception occurred")
            i += 1
        if i > max_port:
            print("Port detection Failed.")
            exit(0)
        sock.close()
    else:
        print("could not find target bluetooth device nearby")


def disconnect():
    asyncio.run(bluetooth_power(False))


def connect_bluetooth(activity, device_name):
    if activity == 'Connect':
        connect(device_name)
    else:
        disconnect()


connect_bluetooth('Connect', 'D2')