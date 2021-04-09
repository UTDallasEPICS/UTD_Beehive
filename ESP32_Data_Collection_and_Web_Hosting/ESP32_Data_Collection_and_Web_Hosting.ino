#include <WiFi.h> //WiFi.h library provides ESP32 specific WiFi methods we are calling to connect to network.
#include <WebServer.h> //WebServer.h library has some methods available that will help us setting up a server and handle incoming HTTP requests without needing to worry about low level implementation details.
#include <Wire.h> //Wire.h library communicates with any I2C device not just BME280


#define SEALEVELPRESSURE_HPA (1013.25)
float temperaturenode1, temperaturenode2, temperaturenode3, temperaturenode4, temperaturenode5, humiditynode1, humiditynode2, humiditynode3, humiditynode4, humiditynode5, weight;



//As we are configuring ESP32 in Station (STA) mode, it will join existing WiFi network. Hence, we need to provide it with your network’s SSID & Password. Next we start web server at port 80.
/*Put your SSID & Password*/

const char* ssid = "MannHouseHold";  // Enter SSID here
const char* password = "Vanshdeep6266!";  //Enter Password here
WebServer server(80);






void setup() {
  Serial.begin(115200); //initialize serial communication is here for testing purpose
  delay(1000); //Initialize sensors



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
  temperaturenode1 = rand() % (40 - 20 + 1) + 20;
  temperaturenode2 = rand() % (40 - 20 + 1) + 20;
  temperaturenode3 = rand() % (40 - 20 + 1) + 20;
  temperaturenode4 = rand() % (40 - 20 + 1) + 20;
  temperaturenode5 = rand() % (40 - 20 + 1) + 20;
  humiditynode1 = rand() % rand() % (60 - 40 + 1) + 40;
  humiditynode2 = rand() % rand() % (60 - 40 + 1) + 40;
  humiditynode3 = rand() % rand() % (60 - 40 + 1) + 40;
  humiditynode4 = rand() % rand() % (60 - 40 + 1) + 40;
  humiditynode5 = rand() % rand() % (60 - 40 + 1) + 40;
  weight = rand() % (250 - 100 + 1) + 100;
  server.send(200, "text/html", SendHTML(temperaturenode1, temperaturenode2, temperaturenode3, temperaturenode4, temperaturenode5, humiditynode1, humiditynode2, humiditynode3, humiditynode4, humiditynode5, weight));
}

void handle_NotFound() {
  server.send(404, "text/plain", "Not found");
}

String SendHTML(float temperaturenode1, float temperaturenode2, float temperaturenode3, float temperaturenode4, float temperaturenode5, float humiditynode1, float humiditynode2, float humiditynode3, float humiditynode4, float humiditynode5, float weight) {
  String ptr = "<!DOCTYPE html> <html>\n";
  ptr += "<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
  ptr += "<title>UTD Beehive 0</title>\n";
  ptr += "<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}\n";
  ptr += "body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;}\n";
  ptr += "p {font-size: 24px;color: #444444;margin-bottom: 10px;}\n";
  ptr += "</style>\n";
  ptr += "</head>\n";
  ptr += "<body>\n";
  ptr += "<div id=\"webpage\">\n";
  ptr += "<h1>UTD Beehive 0</h1>\n";
  ptr += "<p>Temperature Node 1: ";
  ptr += temperaturenode1;
  ptr += "&deg;C</p>";
  ptr += "<p>Temperature Node 2: ";
  ptr += temperaturenode2;
  ptr += "&deg;C</p>";
  ptr += "<p>Temperature Node 3: ";
  ptr += temperaturenode3;
  ptr += "&deg;C</p>";
  ptr += "<p>Temperature Node 4: ";
  ptr += temperaturenode4;
  ptr += "&deg;C</p>";
  ptr += "<p>Temperature Node 5: ";
  ptr += temperaturenode5;
  ptr += "&deg;C</p>";
  ptr += "<p>Humidity Node 1: ";
  ptr += humiditynode1;
  ptr += "%</p>";
  ptr += "<p>Humidity Node 2: ";
  ptr += humiditynode2;
  ptr += "%</p>";
  ptr += "<p>Humidity Node 3: ";
  ptr += humiditynode3;
  ptr += "%</p>";
  ptr += "<p>Humidity Node 4: ";
  ptr += humiditynode4;
  ptr += "%</p>";
  ptr += "<p>Humidity Node 5: ";
  ptr += humiditynode5;
  ptr += "%</p>";
  ptr += "<p>Weight: ";
  ptr += weight;
  ptr += "kg</p>";
  ptr += "</div>\n";
  ptr += "</body>\n";
  ptr += "</html>\n";
  return ptr;
}
