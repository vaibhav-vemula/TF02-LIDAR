import serial

d=serial.Serial("/dev/ttyTHS1", 115200)

def data():
    while True:
        
        count=d.in_waiting
        if(count>=8):
            value=d.read(9)   
            d.reset_input_buffer() 
          
            if(value[0]=='0x59' and value[1]=='0x59'):   
                distance=value[2]+value[3]*256 
                print('DISTANCE = ',distance)
                d.reset_input_buffer()
                
if __name__ == '__main__':
    try:
        if d.is_open == False:
            d.open()
        data()
    except KeyboardInterrupt:
        if d!= None:
            d.close()
