#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
  
const char* ssid = "";
const char* password =  "";
char jsonOutput[128];
  
void setup() {
  
  Serial.begin(115200); 
  WiFi.begin(ssid, password); 
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  
  Serial.println("Connected to the WiFi network");
  
}
  
void loop() {
  
  
  postDataToServer(127); //pass in weight parameter
  
  delay(10000); 
  
}

void postDataToServer(int weight) {

   if(WiFi.status() == WL_CONNECTED){   
  
  HTTPClient client;   
  
   client.begin("http://{PORT}/data");  

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
