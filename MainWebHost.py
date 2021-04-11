
import json
import time

from flask import Flask, Response, render_template

application = Flask(__name__)

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
    return render_template('UTDBeeSite.html', fahrenheit=fahrenheit, humidity=humidity, weight=weight)


@application.route('/chart-data')
def chart_data():
    def bee_hive_data():
        while True:
            fname = 'UTD Beehive 0.txt'
            list = LastNlines(fname, 1)
            date = addDate(list[0], list[1])
            fahrenheit = float(list[2])
            fahrenheit1 = float(list[3])
            json_data = json.dumps(
                {'time': date, 'value': fahrenheit})
            json_data1 = json.dumps(
                {'time': date, 'value': fahrenheit1})

            yield f"data:{json_data}\n\n"
            yield f"data1:{json_data1}\n\n"
            time.sleep(5)

    return Response(bee_hive_data(), mimetype='text/event-stream')

@application.route(('/<UTDBeehive>'))
def UTDBeehive(UTDBeehive):
    fname = UTDBeehive + ".txt"
    list = LastNlines(fname, 1)
    print(list)
    date = addDate(list[0], list[1])
    print(date)
    fahrenheit = float(list[2])
    humidity = list[6]
    weight = list[12]
    return render_template('UTDBeeSite.html', fahrenheit=fahrenheit, humidity=humidity, weight=weight)










if __name__ == '__main__':
    application.run(host="0.0.0.0")
