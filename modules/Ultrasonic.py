from machine import Pin
from machine import ADC

def read(analog_pin):
    adc = ADC(Pin(analog_pin))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    try:
        d = adc.read()
        return int(d) 
    except OSError as ex:
        return -1
