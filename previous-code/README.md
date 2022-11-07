# UTD_Beehive
Code for EPICS UTD Beehive Project


The code is used for the hives located in the UTD apiaries.

ESP32_Data_Collection_and_Web_Hosting.ino is uploaded into the ESP32's but before that you must select a network and a name for the hive.
At that point ESP32Scraper.py will be used on a machine on the same network to scrape the data from the hive. Inorder to tell it what the hive IP is the Beehive_IP.txt is used for that purpose. From the scraping process a file name {Hive Name}.txt will store all the data. the compressed version of  {Hive Name} Compressed.txt is all the data being compressed at the end of the day. It can be mostly ignored.

MainWebHost.py is the file that is constantly run just as ESP32Scraper.py and its job is to host the webpage to anyone that requests it.

Some of the things that still need to be worked out is a way to archive data by putting the compressed file in another directory folder named the beehive name.
A better way to transmit the data without the use of wifi. Possibly LoRa or MQTT.
A nice feature would be to have the system learn from the data a predict hive complase and so on but that is for something far into the future.

As for the Hardware a prototype has already been created and does work properly it is really just a proof of concept. 

IF THERE ARE ANY QUESTIONS OR IF YALL ARE STUCK WITH MAKING THE CODE WORK I WILL GLADLY HELP JUST CONTACT THE TEAM LEADER FOR THE PROJECT IN Spring 2021.

To use this code you must run the weather.py code. You must also have flask
https://flask.palletsprojects.com/en/1.1.x/installation/

