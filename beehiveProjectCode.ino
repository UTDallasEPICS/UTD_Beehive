/**
 *
 * HX711 library for Arduino - example file
 * https://github.com/bogde/HX711
 *
 * MIT License
 * (c) 2018 Bogdan Necula
 *
**/
#include "HX711.h"
#include "DHT.h"


// HX711 circuit wiring
//Constants
#define DHTPIN 10     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino


//Variables
int chk; // might not need this didn't check
float hum;  //Stores humidity value
float temp; //Stores temperature value
const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 7;
float celcius;
float fahrenheit;
float voltage;
float sensorValue;
const int temperatureSensorPin = A0;


HX711 scale;

void setup() {
  Serial.begin(38400);
  dht.begin();
  Serial.println("HX711 Demo");

  Serial.println("Initializing the scale");

  // Initialize library with data output pin, clock input pin and gain factor.
  // Channel selection is made by passing the appropriate gain:
  // - With a gain factor of 64 or 128, channel A is selected
  // - With a gain factor of 32, channel B is selected
  // By omitting the gain factor parameter, the library
  // default "128" (Channel A) is used here.
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);

  Serial.println("Before setting up the scale:");
  Serial.print("read: \t\t");
  Serial.println(scale.read());      // print a raw reading from the ADC

  Serial.print("read average: \t\t");
  Serial.println(scale.read_average(20));   // print the average of 20 readings from the ADC

  Serial.print("get value: \t\t");
  Serial.println(scale.get_value(5));   // print the average of 5 readings from the ADC minus the tare weight (not set yet)

  Serial.print("get units: \t\t");
  Serial.println(scale.get_units(5), 1);  // print the average of 5 readings from the ADC minus tare weight (not set) divided
            // by the SCALE parameter (not set yet)

  scale.set_scale(2280.f);                      // this value is obtained by calibrating the scale with known weights; see the README for details
  scale.tare();               // reset the scale to 0

  Serial.println("After setting up the scale:");

  Serial.print("read: \t\t");
  Serial.println(scale.read());                 // print a raw reading from the ADC

  Serial.print("read average: \t\t");
  Serial.println(scale.read_average(20));       // print the average of 20 readings from the ADC

  Serial.print("get value: \t\t");
  Serial.println(scale.get_value(5));   // print the average of 5 readings from the ADC minus the tare weight, set with tare()

  Serial.print("get units: \t\t");
  Serial.println(scale.get_units(5), 1);        // print the average of 5 readings from the ADC minus tare weight, divided
            // by the SCALE parameter set with set_scale

  Serial.println("Readings:");
}

void loop() {
   /* obtains the raw data for the temperature sensor */
  sensorValue = analogRead(temperatureSensorPin);
  
  /* find the voltage going through the sensor */
  
  voltage = sensorValue * 3.3; // multiply sensorValue by 5 because we have 5 volts connected to it
  voltage /= 1024.0;
  
  /* calculate the temperature */
  
  celcius = (voltage - 0.5) * 100;
  fahrenheit = (9.0/5) * celcius + 32;
  
  /* print temperatures */
  
  Serial.print("Celcius: ");
  Serial.println(celcius);
  Serial.print("Fahrenheit: ");
  Serial.println(fahrenheit);
  Serial.println();
  //Read data and store it to variables hum and temp
  hum = dht.readHumidity();
  //Print temp and humidity values to serial monitor
  Serial.print("Humidity: ");
  Serial.println(hum);
  Serial.println();
  Serial.print("one reading:\t");
  Serial.print(scale.get_units(), 1);
  Serial.print("\t| average:\t");
  Serial.println(scale.get_units(10), 1);
  delay(1000);
  scale.power_down();             // put the ADC in sleep mode
  delay(5000);
  scale.power_up();
}
