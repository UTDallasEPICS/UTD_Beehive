from flask import Flask, render_template
##from sense_emu import SenseHat

app = Flask(__name__)

@app.route('/')

def index():
   ## sense = SenseHat()

    celcius = 32 ##round(sense.get_temperature(), 1)
    fahrenheit = 68 ##round(1.8 * celcius + 32, 1)
    humidity = 54.2##round(sense.get_humidity(), 1)
    pressure = 789##round(sense.get_pressure(), 1)

    return render_template('SensorSite.html', celcius=celcius, fahrenheit=fahrenheit, humidity=humidity, pressure=pressure)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')