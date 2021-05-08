//Made by Vanshdeep Singh
#include <WiFi.h> //WiFi.h library provides ESP32 specific WiFi methods we are calling to connect to network.
#include <WebServer.h> //WebServer.h library has some methods available that will help us setting up a server and handle incoming HTTP requests without needing to worry about low level implementation details.
#include <Wire.h> //Wire.h library communicates with any I2C device not just BME280
#include "DHT.h"
#include "HX711.h"


#define calibration_factor -7050.0 //This value is obtained using the SparkFun_HX711_Calibration sket

#define DHT1_PIN 23
#define DHT2_PIN 19
#define DHT3_PIN 18
#define DHT4_PIN 5
#define DHT5_PIN 17
#define LOADCELL_DOUT_PIN  26
#define LOADCELL_SCK_PIN  27
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321


HX711 scale;

DHT dht1(DHT1_PIN, DHTTYPE); // Initialize DHT sensor.
DHT dht2(DHT2_PIN, DHTTYPE); // Initialize DHT sensor.
DHT dht3(DHT3_PIN, DHTTYPE); // Initialize DHT sensor.
DHT dht4(DHT4_PIN, DHTTYPE); // Initialize DHT sensor.
DHT dht5(DHT5_PIN, DHTTYPE); // Initialize DHT sensor.

#define SEALEVELPRESSURE_HPA (1013.25)
float temperaturenode1, temperaturenode2, temperaturenode3, temperaturenode4, temperaturenode5, humiditynode1, humiditynode2, humiditynode3, humiditynode4, humiditynode5, weight;
const char* BeehiveName = "UTD Beehive 0"; //Input Beehive Name


//As we are configuring ESP32 in Station (STA) mode, it will join existing WiFi network. Hence, we need to provide it with your network’s SSID & Password. Next we start web server at port 80.
/*Put your SSID & Password*/

const char* ssid = "WifiName";  // Enter SSID here
const char* password = "WifiPassword";  //Enter Password here
WebServer server(80);






void setup() {
  Serial.begin(115200); //initialize serial communication is here for testing purpose
  delay(1000); //Initialize sensors

  pinMode(DHT1_PIN, INPUT);
  pinMode(DHT2_PIN, INPUT);
  pinMode(DHT3_PIN, INPUT);
  pinMode(DHT4_PIN, INPUT);
  pinMode(DHT5_PIN, INPUT);

  dht1.begin();
  dht2.begin();
  dht3.begin();
  dht4.begin();
  dht5.begin();



  //scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0


  
  Serial.println("Connecting to "); //serial communication is here for testing
  Serial.println(ssid);  //serial communication is here for testing

  //connect to your local wi-fi network
  WiFi.begin(ssid, password);

  //check wi-fi is connected to wi-fi network
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000); //wait for connection
    Serial.print("."); //serial communication is here for testing
  }
  Serial.println(""); //serial communication is here for testing
  Serial.println("WiFi connected..!"); //serial communication is here for testing
  Serial.print("Got IP: ");  Serial.println(WiFi.localIP()); //serial communication is here for testing

  server.on("/", handle_OnConnect);
  server.onNotFound(handle_NotFound);

  server.begin();
  Serial.println("HTTP server started"); //serial communication is here for testing

}
void loop() {
  server.handleClient(); //

}

void handle_OnConnect() {
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(calibration_factor); //This value is obtained by using the SparkFun_HX711_Calibration sketch

  
  temperaturenode1 = dht1.readTemperature(true);
  temperaturenode2 = dht2.readTemperature(true);
  temperaturenode3 = dht3.readTemperature(true);
  temperaturenode4 = dht4.readTemperature(true);
  temperaturenode5 = dht5.readTemperature(true);
  humiditynode1 = dht1.readHumidity();
  humiditynode2 = dht2.readHumidity();
  humiditynode3 = dht3.readHumidity();
  humiditynode4 = dht4.readHumidity();
  humiditynode5 = dht5.readHumidity();
  weight = scale.get_units();
  server.send(200, "text/html", SendHTML(temperaturenode1, temperaturenode2, temperaturenode3, temperaturenode4, temperaturenode5, humiditynode1, humiditynode2, humiditynode3, humiditynode4, humiditynode5, weight));
}

void handle_NotFound() {
  server.send(404, "text/plain", "Not found");
}

String SendHTML(float temperaturenode1, float temperaturenode2, float temperaturenode3, float temperaturenode4, float temperaturenode5, float humiditynode1, float humiditynode2, float humiditynode3, float humiditynode4, float humiditynode5, float weight) {
  String ptr = "<!DOCTYPE html> <html>\n";
  ptr += "<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
  ptr += "<title>UTD Beehives</title>\n";
  ptr += "<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}\n";
  ptr += "body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;}\n";
  ptr += "p {font-size: 24px;color: #444444;margin-bottom: 10px;}\n";
  ptr += "</style>\n";
  ptr += "</head>\n";
  ptr += "<body>\n";
  ptr += "<div id=\"webpage\">\n";
  ptr += "<h1>";
  ptr += BeehiveName;
  ptr += "</h1>\n";

  ptr += "<p>Temperature: ";
  ptr += temperaturenode1;
  ptr += " ";
  ptr += temperaturenode2;
  ptr += " ";
  ptr += temperaturenode3;
  ptr += " ";
  ptr += temperaturenode4;
  ptr += " ";
  ptr += temperaturenode5;
  ptr += "&deg;F</p>";

  ptr += "<p>Humidity: ";
  ptr += humiditynode1;
  ptr += " ";
  ptr += humiditynode2;
  ptr += " ";
  ptr += humiditynode3;
  ptr += " ";
  ptr += humiditynode4;
  ptr += " ";
  ptr += humiditynode5;
  ptr += "%</p>";

  ptr += "<p>Weight: ";
  ptr += weight;
  ptr += "lb</p>";
  ptr += "</div>\n";
  ptr += "</body>\n";
  ptr += "</html>\n";
  return ptr;
}
