
import json
import time

from flask import Flask, Response, render_template

application = Flask(__name__)
#Check how many beehives there are
def addDate(YMD, time):
    fullDate = YMD + " " + time
    return fullDate

def LastNlines(fname, N):
    # opening file using with() method
    # so that file get closed
    # after completing work
    with open(fname) as file:
        # loop to read iterate
        # last n lines and print it
        for line in (file.readlines()[-N:]):
            x = line.split()

            return x





@application.route('/') # This displays the main parts of the website
def index():
    fname = 'UTD Beehive 0.txt'
    list = LastNlines(fname, 1)
    print(list)
    date = addDate(list[0], list[1])
    print(date)
    fahrenheit = float(list[2])
    humidity = list[6]
    weight = list[12]

    return render_template('UTDBeeSite.html', fahrenheit=fahrenheit, humidity=humidity, weight=weight, )


@application.route('/<UTDBeehive>')
def UTDBeehive(UTDBeehive):
    fname = UTDBeehive + ".txt"
    list = LastNlines(fname, 1)
    #print(list)
    date = addDate(list[0], list[1])
    #print(date)
    fahrenheit = float(list[2])
    humidity = list[6]
    weight = list[12]

    date = []
    temperaturenode1 = []
    temperaturenode2 = []
    temperaturenode3 = []
    temperaturenode4 = []
    temperaturenode5 = []
    humiditynode1 = []
    humiditynode2 = []
    humiditynode3 = []
    humiditynode4 = []
    humiditynode5 = []
    weightnode = []

    with open(fname) as file:
        for readline in file:

            readlist = readline.split()
            str = readlist[0] + " " + readlist[1]
            date.append(str)
            temperaturenode1.append(float(readlist[2]))
            temperaturenode2.append(float(readlist[3]))
            temperaturenode3.append(float(readlist[4]))
            temperaturenode4.append(float(readlist[5]))
            temperaturenode5.append(float(readlist[6]))
            humiditynode1.append(float(readlist[7]))
            humiditynode2.append(float(readlist[8]))
            humiditynode3.append(float(readlist[9]))
            humiditynode4.append(float(readlist[10]))
            humiditynode5.append(float(readlist[11]))
            weightnode.append(float(readlist[12]))




    return render_template('UTDHiveSite.html', fahrenheit=fahrenheit, humidity=humidity, weight=weight, date=date,temperaturenode1=temperaturenode1,temperaturenode2=temperaturenode2,temperaturenode3=temperaturenode3,temperaturenode4=temperaturenode4,temperaturenode5=temperaturenode5,humiditynode1=humiditynode1,humiditynode2=humiditynode2,humiditynode3=humiditynode3,humiditynode4=humiditynode4,humiditynode5=humiditynode5,weightnode=weightnode)





if __name__ == '__main__':
    application.run(host="0.0.0.0")
