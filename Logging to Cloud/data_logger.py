import serial
import time
import schedule
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# main function


def main():
    arduino = serial.Serial('COM25', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values.append(float(decoded_values))

    print(f'Collected readings from Arduino: {list_values}')

    # call function for other processing
    date_time_array = get_the_date_and_time()
    push_data_to_cloud(list_values, date_time_array)

    global counter
    counter += 1

    arduino_data = 0
    list_values.clear()
    arduino.close()
    print('Connection closed')
    print('<----------------------------->')


# obtain date and time
def get_the_date_and_time():
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    dt_array = dt_string.split(' ')
    return dt_array


# push data to google sheet
def push_data_to_cloud(push_data, date_time_list):
    scope = ['https://spreadsheets.google.com/feeds' +
             ' ' + 'https://www.googleapis.com/auth/drive']

    credit_sample = ServiceAccountCredentials.from_json_keyfile_name(
        "credit.json", scope)
    client = gspread.authorize(credit_sample)
    sheet = client.open("Logging Data Arduino").sheet1

    # existing_data = sheet.get_all_records()
    data_to_append = [date_time_list[0], date_time_list[1], push_data[0]]
    sheet.append_row(data_to_append)
    print('Readings pushed to cloud')


# ---- Main Code ----
list_values = []
counter = 0

print('Program started')

schedule.every(5).seconds.do(main)

while True:
    schedule.run_pending()

    if counter >= 60:
        break

    time.sleep(1)

print('Data collected Successfully')
