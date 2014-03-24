#!/usr/bin/env python

APIN_PATH = "/proc/adc"

scale = 10
ref_vcc = 3.3

def is_charging(Apin1,Apin2):
    if (0 <= Apin1 <= 5) and (0 <= Apin2 <= 5):
        fname1 = APIN_PATH + str(Apin1)
        fname2 = APIN_PATH + str(Apin2)
        with open(fname1, "r") as f1:
            value1 = int(f1.read()[5:-1])
            print "value1", value1
            f1.close()
        with open(fname2, "r") as f2:
            value2 = int(f2.read()[5:-1])
            print "value2", value2
            f2.close()

        v1high = 2048 if Apin1 >= 2 else 25
        v1low = 500 if Apin1 >= 2 else 10
        v2high = 2048 if Apin2 >= 2 else 25
        v2low = 500 if Apin2 >= 2 else 10

        if (value1 > v1high) and (value2 < v2low):
            return 1 #battery is charging
        elif (value1 < v1low) and (value2 > v2high):
            return 2 #battery is fully charged
        else:
            return 3 #no battery detected

    else:
        raise ValueError("ADC PIN must be between 0-5")

def battery_level(Apin):
    if (2 <= Apin <= 5):
        fname = APIN_PATH + str(Apin)
        with open(fname, "r") as f:
            value = f.read()[5:-1]
            f.close()
        print "battery level value:", value
        #voltage = (int(value) * ref_vcc)/4095 * scale
        voltage = (float(value)/4095) * ref_vcc * scale
        return voltage
    else:
        raise ValueError("ADC PIN must be between 2-5")
   

if __name__ == "__main__":
    print battery_level(5)
    print is_charging(4, 1)
