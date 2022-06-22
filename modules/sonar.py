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
<<<<<<< HEAD
        v = a[3:7]
        avg = ( sum (v) / len(v) )/27
=======
        print(a)
        print('------')
        v = a[3:7]
        print(v)
        avg = ( sum (v) / len(v) )/27
        print(avg)
        
>>>>>>> 493a21c3f976ce4e2374a3ab0116bee8edd71caa
        return int(avg)
    except OSError as ex:
        return -1
