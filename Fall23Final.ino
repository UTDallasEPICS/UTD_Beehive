#include "DHT.h"

// avoid pins 0, 2 , 5, 12, 15 (strapping pins)
//Constants
// #define DHTPINNorth 13     // what pin we're connected to
// #define DHTPINWest 14
#define DHTTYPE DHT22   // DHT 22 (AM2302)


#define DHT_SENSOR_PIN_1  13 // ESP32 pin GIOP21 connected to DHT22 sensor

#define DHT_SENSOR_PIN_2 14 // Choose an empty port to connect another sensor to!

#define DHT_SENSOR_PIN_3 27 // Choose an empty port to connect another sensor to!

#define DHT_SENSOR_PIN_4 26 // Choose an empty port to connect another sensor to!


DHT dht1(DHT_SENSOR_PIN_1, DHTTYPE);
DHT dht2(DHT_SENSOR_PIN_2, DHTTYPE);
DHT dht3(DHT_SENSOR_PIN_3, DHTTYPE);
DHT dht4(DHT_SENSOR_PIN_4, DHTTYPE);


float humidity; 
float temperature;
float tempAverage;
float humidityAverage;


// Calibrating the load cell
#include "HX711.h"

// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 19;
//18, 19, 26, 27
const int LOADCELL_SCK_PIN = 18;
int i;
HX711 scale;
int zero;

void setup() {
  // DHT setup
  Serial.begin(115200);
  
  dht1.begin();
  dht2.begin();
  dht3.begin();
  dht4.begin();

// weight sensor setup
 // Serial.begin(115200);
  Serial.println("HX711 Demo");
  Serial.println("Initializing the scale");
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(10);
  scale.tare();    
}

void loop() {
  // dht code
  delay(2000); 
    Serial.println();

humidity = (dht1.readHumidity() + dht2.readHumidity() + dht3.readHumidity() + dht4.readHumidity())/4;
temperature = (dht1.readTemperature() + dht2.readTemperature() + dht3.readTemperature() + dht4.readTemperature())/4;

    Serial.print("Humidity: ");
    Serial.print(humidity);
    Serial.print(" %, Temp: ");
    Serial.print(temperature);
    Serial.println(" Celsius");
    delay(3000); //Delay 3 sec.

    // hx711 code
    int sum = 0;
    int avg = 0;
  Serial.println("Put known weight over the scale");
  delay(1000);
  for(int i = 0; i <= 10; i++)
  {
    sum += scale.get_units(10);
  }
  avg = abs(sum/10);
  Serial.println(avg);
  Serial.println(" lbs");
  delay(1000); 

}
