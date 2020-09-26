import csv
import os.path
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def writing_to_csv_file(cdt):
    if os.path.isfile('Logging to Arduino.csv'):
        print('file exists')
        with open('Logging to Arduino.csv', mode='a', newline='') as f:  # a for append
            thewriter = csv.writer(f)

            for i in range((len(cdt))):
                thewriter.writerow(
                    [cdt[i]['Date '], cdt[i]['Time'], cdt[i]['Distance']])
    else:
        # create new file
        print('file does not exist')
        with open('Logging to Arduino.csv', mode='w', newline='') as f:
            thewriter = csv.writer(f)

            for i in range(len(cdt)):
                thewriter.writerow(
                    [cdt[i]['Date '], cdt[i]['Time'], cdt[i]['Distance']])
    print('CSV file created')


def pull_data_from_cloud():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    credits_sample = ServiceAccountCredentials.from_json_keyfile_name(
        "credit.json", scope)
    client = gspread.authorize(credits_sample)
    sheet = client.open("Logging Data Arduino").sheet1
    data = sheet.get_all_records()
    print('Obtained data from cloud')
    return data


cloud_data = pull_data_from_cloud()
writing_to_csv_file(cloud_data)
