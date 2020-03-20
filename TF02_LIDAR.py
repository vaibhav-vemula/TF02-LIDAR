import serial

da=serial.Serial("/dev/ttyTHS1", 115200)

def data():
    while True:
        
        count=da.in_waiting
        if(count>=8):
            value=da.read(9)   
            da.reset_input_buffer() 
          
            if(value[0]=='0x59' and value[1]=='0x59'):   
                distance=value[2]+value[3]*256 
                print('DISTANCE = ',distance)
                da.reset_input_buffer()
                
if __name__ == '__main__':
    try:
        if da.is_open == False:
            da.open()
        data()
    except KeyboardInterrupt:
        if da!= None:
            da.close()
