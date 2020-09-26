import serial
import time
import schedule


def main_func():
    arduino = serial.Serial('COM25', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values.append(float(decoded_values))

    print(f'Collected readings from Arduino: {list_values}')

    arduino_data = 0
    list_values.clear()
    arduino.close()
    print('Connection closed')
    print('<----------------------------->')


# ----Main Code----
list_values = []

print('Program Started')

# Setting up Arduino
schedule.every(1).seconds.do(main_func)

while(True):
    schedule.run_pending()
    time.sleep(1)
