from time import sleep
from machine import Pin
from machine import ADC
def read(analog_pin):
    adc = ADC(Pin(analog_pin))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    try:
        a = []   
        for count in range(10):
            a.append(adc.read())
            sleep(0.01)            
        a.sort()
        v = a[3:7]
        avg = ( sum (v) / len(v) )/27
        return int(avg)
    except OSError as ex:
        return -1
