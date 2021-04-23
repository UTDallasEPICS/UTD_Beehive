import json
import time

from flask import Flask, Response, render_template

application = Flask(__name__)


# Check how many beehives there are



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


@application.route('/')  # This displays the main parts of the website
def index():
    # These 7 lines under me will be turned into a dynamic list
    fname = 'UTD Beehive 0.txt'
    list = LastNlines(fname, 1)
    fahrenheit = float(list[2])
    humidity = list[6]
    weight = list[12]
    UTDBeehive = 'UTD Beehive 0'
    return render_template('UTDBeeSite.html', Beehive=UTDBeehive, fahrenheit=fahrenheit, humidity=humidity,
                           weight=weight, )

@application.route('/<UTDBeehive>')
def UTDBeehive(UTDBeehive):
    fname = UTDBeehive + ".txt"
    list = LastNlines(fname, 1)
    fahrenheit = float(list[2])
    humidity = list[6]
    weight = list[12]

    fname = UTDBeehive + " Compressed.txt"
    Cdate = []
    Ctemperaturenode1 = []
    Ctemperaturenode2 = []
    Ctemperaturenode3 = []
    Ctemperaturenode4 = []
    Ctemperaturenode5 = []
    Chumiditynode1 = []
    Chumiditynode2 = []
    Chumiditynode3 = []
    Chumiditynode4 = []
    Chumiditynode5 = []
    Cweightnode = []

    with open(fname) as file:
        for readline in file:
            readlist = readline.split()
            str = readlist[0]
            Cdate.append(str)
            Ctemperaturenode1.append(float(readlist[1]))
            Ctemperaturenode2.append(float(readlist[2]))
            Ctemperaturenode3.append(float(readlist[3]))
            Ctemperaturenode4.append(float(readlist[4]))
            Ctemperaturenode5.append(float(readlist[5]))
            Chumiditynode1.append(float(readlist[6]))
            Chumiditynode2.append(float(readlist[7]))
            Chumiditynode3.append(float(readlist[8]))
            Chumiditynode4.append(float(readlist[9]))
            Chumiditynode5.append(float(readlist[10]))
            Cweightnode.append(float(readlist[11]))
    file.close()
    return render_template('UTDHive.html', Beehive=UTDBeehive, fahrenheit=fahrenheit, humidity=humidity,
                           weight=weight, Cdate=Cdate,
                           Ctemperaturenode1=Ctemperaturenode1, Ctemperaturenode2=Ctemperaturenode2,
                           Ctemperaturenode3=Ctemperaturenode3, Ctemperaturenode4=Ctemperaturenode4,
                           Ctemperaturenode5=Ctemperaturenode5, Chumiditynode1=Chumiditynode1,
                           Chumiditynode2=Chumiditynode2, Chumiditynode3=Chumiditynode3, Chumiditynode4=Chumiditynode4,
                           Chumiditynode5=Chumiditynode5, Cweightnode=Cweightnode)

@application.route('/<UTDBeehive>Temperature')
def UTDBeehiveTemperature(UTDBeehive):
    fname = UTDBeehive + ".txt"
    list = LastNlines(fname, 1)
    fahrenheit = float(list[2])
    humidity = list[6]
    weight = list[12]


    date = []
    temperaturenode1 = []
    temperaturenode2 = []
    temperaturenode3 = []
    temperaturenode4 = []
    temperaturenode5 = []


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
    file.close()

    return render_template('UTDHiveTemperature.html', Beehive=UTDBeehive, fahrenheit=fahrenheit, humidity=humidity,
                           weight=weight, date=date, temperaturenode1=temperaturenode1,
                           temperaturenode2=temperaturenode2, temperaturenode3=temperaturenode3,
                           temperaturenode4=temperaturenode4, temperaturenode5=temperaturenode5)

@application.route('/<UTDBeehive>Humidity')
def UTDBeehiveHumidity(UTDBeehive):
    fname = UTDBeehive + ".txt"
    list = LastNlines(fname, 1)
    fahrenheit = float(list[2])
    humidity = list[6]
    weight = list[12]

    date = []

    humiditynode1 = []
    humiditynode2 = []
    humiditynode3 = []
    humiditynode4 = []
    humiditynode5 = []

    with open(fname) as file:
        for readline in file:
            readlist = readline.split()
            str = readlist[0] + " " + readlist[1]
            date.append(str)
            humiditynode1.append(float(readlist[7]))
            humiditynode2.append(float(readlist[8]))
            humiditynode3.append(float(readlist[9]))
            humiditynode4.append(float(readlist[10]))
            humiditynode5.append(float(readlist[11]))
    file.close()

    return render_template('UTDHiveHumidity.html', Beehive=UTDBeehive, fahrenheit=fahrenheit, humidity=humidity,
                           weight=weight, date=date,
                           humiditynode1=humiditynode1, humiditynode2=humiditynode2, humiditynode3=humiditynode3,
                           humiditynode4=humiditynode4, humiditynode5=humiditynode5)

@application.route('/<UTDBeehive>Weight')
def UTDBeehiveWeight(UTDBeehive):
        fname = UTDBeehive + ".txt"
        list = LastNlines(fname, 1)
        fahrenheit = float(list[2])
        humidity = list[6]
        weight = list[12]

        date = []

        weightnode = []

        with open(fname) as file:
            for readline in file:
                readlist = readline.split()
                str = readlist[0] + " " + readlist[1]
                date.append(str)
                weightnode.append(float(readlist[12]))
        file.close()

        return render_template('UTDHiveWeight.html', Beehive=UTDBeehive, fahrenheit=fahrenheit, humidity=humidity,
                               weight=weight, date=date, weightnode=weightnode)


if __name__ == '__main__':
    application.run(host="0.0.0.0")