#BK549C.py

import pyvisa #pip install pyvisa
from time import sleep

# change this as every device has a unique identifier
idn1 = 'BK Precision,5493C,558G25163,V1.4.47'

def find_DMM():
    global rm, DMM
    rm = pyvisa.ResourceManager()
    resources = rm.list_resources()
    for res in resources:
        try:
            DMM = rm.open_resource(res)
            response = DMM.query('*IDN?')
            print(response)
            if response.strip() == idn1:
                # print(response)
                # print(DMM)
                print(res)
                return res  # 🎯 Return the VISA address if match
        except Exception:
            pass  # Ignore any devices that don't respond
    return None  # ❌ Not found

find_DMM()

def measure_DMM_voltage(res):
    global rm, DMM
    DMM = rm.open_resource(res)
    measured_voltage = DMM.query('MEAS:VOLT:DC? 100')
    DMM.close()
    return measured_voltage
