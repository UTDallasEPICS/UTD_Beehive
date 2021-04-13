
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


def collectallfunction(filenameforbeehive):
    datapoint = "["
    with open(filenameforbeehive) as file:
        for readline in file:
            # For Python3, use print(line)
            readlist = readline.split()
            datapoint = datapoint + "('" + readlist[0] + " " + readlist[1] + "'," + readlist[2] + ")" +  ", "
        datapoint = datapoint[:-2]
        datapoint = datapoint + "]"
    return datapoint




    #Grabs the date and temp
    # stores date and temp in this format ('date', temp)
    #does this for whole file
    #put into list and append
    #return list


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
    data = [('04-01-2021', 150),('04-02-2021', 140),('04-03-2021', 150)]
    print(type(data))
    str = collectallfunction(fname)
    print(str)
    #data = str
    #print(data)
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template('UTDHiveSite.html', fahrenheit=fahrenheit, humidity=humidity, weight=weight, labels=labels,values=values)





if __name__ == '__main__':
    application.run(host="0.0.0.0")
