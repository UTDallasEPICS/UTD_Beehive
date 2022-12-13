#include <Arduino.h>
#include "HX711.h"
#include "soc/rtc.h"
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

#define uS_TO_S_FACTOR 1000000  /* Conversion factor for micro seconds to seconds */
#define TIME_TO_SLEEP  2        /* Time ESP32 will go to sleep (in seconds) */

RTC_DATA_ATTR int numStarts = 0;
const int LOADCELL_DOUT_PIN = 16;
const int LOADCELL_SCK_PIN = 4;
RTC_DATA_ATTR long calibrationFactor = -50357/2267.96;
long offset = -193901;
RTC_DATA_ATTR double weight[9];
const char* ssid = "[WIFI-NAME]";
const char* password =  "[WIFI-PASSWORD]";
char jsonOutput[128];

HX711 scale;

void wake_up_reason()
{
  esp_sleep_wakeup_cause_t wakeup_reason;
  wakeup_reason = esp_sleep_get_wakeup_cause();
  switch(wakeup_reason)
  {
    case ESP_SLEEP_WAKEUP_EXT0 : calibrate(); break;
    default : getWeight(); break;
  }
}

void calibrate()
{
  Serial.println("start cal");
  bool buttonPressed = false;
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale();
  double sum = scale.read_average(10);
	scale.set_offset(sum);
  offset = sum;
  delay(2000);
  while(buttonPressed == false)
  {
    if(digitalRead(15) != 1)
      break;
  }
  long reading = scale.get_units(10);
  calibrationFactor = reading/2267.96;
  Serial.println(calibrationFactor);
  getWeight();
  delay(2000);
  Serial.println("end cal");
}

void getWeight()
{
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(calibrationFactor);
  scale.set_offset(offset);

  weight[numStarts - 1] = scale.get_units(5);
  scale.power_down();
}

void sendData()
{
  Serial.println("sending data");
  WiFi.begin(ssid, password); 
  int count = 0;
  
  while (WiFi.status() != WL_CONNECTED && count < 5) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
    count++;
    if(count == 5)
      return;
  }
  
  Serial.println("Connected to the WiFi network");
  
  for(int i = 0; i < 10; i++)
  {
    postDataToServer(weight[i-1]);
    Serial.println(weight[i-1]);
    weight[i-1] = 0;
  }
  Serial.println("done");
}

void setup(){
  Serial.begin(9600);
  wake_up_reason();

  numStarts++;
  Serial.println(numStarts);
  if (numStarts == 10)
  {
    sendData();
    numStarts = 0;
  }

  esp_sleep_enable_ext0_wakeup(GPIO_NUM_15, 0);
  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
  esp_deep_sleep_start();
}

void loop(){
  
}

void postDataToServer(double weight) {

   if(WiFi.status() == WL_CONNECTED){   
  
  HTTPClient client;   
  
   client.begin("http://[HOST-PORT]:3000/data");  

   client.addHeader("Content-Type", "application/json");  

   const size_t CAPACITY = JSON_OBJECT_SIZE(1);
   StaticJsonDocument<CAPACITY> doc;

   JsonObject object = doc.to<JsonObject>();
   object["x"] = weight;

   serializeJson(doc, jsonOutput);
   int httpCode = client.POST(String(jsonOutput));

   if(httpCode > 0){
     String payload = client.getString();
     Serial.println("\nStatus Code: " + String(httpCode));
     Serial.println(payload);

     client.end();
   }

  else{
    Serial.print("Error on sending POST: ");  
   }
  
 }
 
 else{
  
    Serial.println("Error in WiFi connection");   
  
 }

}
