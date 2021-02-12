import serial 
import MySQLdb
import time

#establish connection to MySQL. You'll have to change this for your database.
dbConn = MySQLdb.connect("localhost","root","","testing") or die ("could not connect to database")

#open a cursor to the database
cursor = dbConn.cursor()

device = 'COM16' #this will have to be changed to the serial port you are using

try:
    print("Trying...",device)
    arduino = serial.Serial(port=device, baudrate=9600)
except:
    print("Failed to connect on ",device)

j = 1
while j <= 5:
    time.sleep(2)
    j+=1 
    try:
        data = arduino.readline().decode('ascii') # read the data from arduino 
        pieces = data.split("\n") # split data by new liner
        pieces = data.split("\r")

        # print(pieces[0])

        # here we going to insert data to database
        try:
            cursor = dbConn.cursor()
            # print(cursor)
            cursor.execute("INSERT INTO ultrasonicdata (distance) VALUES (%s)",[pieces[0]])
            dbConn.commit() # commit the insert
            cursor.close() # close the cursor

        except MySQLdb.IntegrityError:
            print ("Failed to Insert data ...")
            
        finally:
            cursor.close() # close just incase it failed

    except:
        print("Failed to get data from Arduino")


