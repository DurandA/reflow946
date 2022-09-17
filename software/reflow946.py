import asyncio
from collections import namedtuple
import sys
from typing import List

from bleak import BleakClient

ADDRESS = "10:52:1C:A5:01:2E"

MODEL_NBR_UUID = "0000{0:x}-0000-1000-8000-00805f9b34fb".format(0x2A24)
DEVICE_NAME_UUID = "0000{0:x}-0000-1000-8000-00805f9b34fb".format(0x2A00)
MANUFACTURER_NAME_UUID = "0000{0:x}-0000-1000-8000-00805f9b34fb".format(0x2A29)

REFLOW_SERVICE_UUID = "946c0200-ca89-a45f-6829-45990a88c1de"
TEMPERATURE_CHAR_UUID = "946c0201-ca89-a45f-6829-45990a88c1de"
TARGET_CHAR_UUID = "946c0202-ca89-a45f-6829-45990a88c1de"
REFLOW_PROFILE_CHAR_UUID = "946c0205-ca89-a45f-6829-45990a88c1de"
NVS_REFLOW_PROFILE_CHAR_UUID = "946c0206-ca89-a45f-6829-45990a88c1de"

MAX_PROFILE_STEPS = 5

ReflowStep = namedtuple('ReflowStep', ['duration', 'temperature'])

def reflow_profile_data(reflow_profile: List[ReflowStep]) -> bytearray:
    STEP_BYTES = 4
    profile_data = bytearray(STEP_BYTES * MAX_PROFILE_STEPS)
    profile_slices = (slice(i*STEP_BYTES, i*STEP_BYTES + STEP_BYTES) for i in range(MAX_PROFILE_STEPS))

    for reflow_step, profile_slice in zip(reflow_profile, profile_slices):
        duration = reflow_step.duration.to_bytes(2, byteorder='little')
        temperature = reflow_step.temperature.to_bytes(2, byteorder='little')
        profile_data[profile_slice] = duration + temperature

    return profile_data


async def main(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

        try:
            device_name = await client.read_gatt_char(DEVICE_NAME_UUID)
            print("Device Name: {0}".format("".join(map(chr, device_name))))
        except Exception:
            pass

        reflow_profile = [
            ReflowStep(90, 170), # raise temperature to 170°C and hold it for 90s
            ReflowStep(90, 217), # raise temperature to 217°C and hold it for 90s
            ReflowStep(50, 240), # raise temperature to 240°C and hold it for 50s
            ReflowStep(20, 245), # raise temperature to 245°C and hold it for 20s
        ]
        await client.write_gatt_char(REFLOW_PROFILE_CHAR_UUID, reflow_profile_data(reflow_profile))

        async def temperature_handler(sender, data):
            celcius = int.from_bytes(data, 'little') / 10;
            print("Temperature: {0}".format(celcius))

        await client.start_notify(TEMPERATURE_CHAR_UUID, temperature_handler)
        await asyncio.sleep(900.0)
        await client.stop_notify(TEMPERATURE_CHAR_UUID)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) == 2 else ADDRESS))
