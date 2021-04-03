
import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template

application = Flask(__name__)
random.seed()  # Initialize the random number generator
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


@application.route('/')
def index():
    fname = 'UTD BeeHive 0.txt'
    list = LastNlines(fname, 1)
    date = addDate(list[0], list[1])
    celcius = float(list[2])
    fahrenheit = celcius * (9 / 5) + 32
    humidity = list[3]
    pressure = list[4]
    return render_template('UTDBeeSite.html', celcius=celcius, fahrenheit=fahrenheit, humidity=humidity, pressure=pressure)


@application.route('/chart-data')
def chart_data():
    def bee_hive_data():
        while True:
            fname = 'UTD BeeHive 0.txt'
            list = LastNlines(fname, 1)
            date = addDate(list[0], list[1])
            celcius = float(list[2])
            fahrenheit = celcius * (9/5) +32
            humidity = list[3]
            pressure = list[4]
            json_data = json.dumps(
                {'time': date, 'value': celcius})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(bee_hive_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    application.run(debug=True, threaded=True)
