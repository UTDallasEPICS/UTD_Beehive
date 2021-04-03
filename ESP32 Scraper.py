##Created By Vanshdeep Singh
## I will add in comments I promise :)

from urllib.request import urlopen
import datetime
import time


def saveToFile(beehiveName, beehivetemperature, beehivehumidity, beehivepressure):
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    DataGrab = currentTime + " " + beehivetemperature + " " + beehivehumidity + " " + beehivepressure
    fileNameForBeehive = beehiveName + ".txt"
    beeHive = open(fileNameForBeehive, "a")
    beeHive.write(DataGrab + "\n")
    beeHive.close()


def scrape(ip):
    url = ip
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    start_index = html.find("<title>") + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    print(title)

    start_index = html.find("Temperature: ") + len("Temperature: ")
    end_index = html.find("&deg;C")
    temperature = html[start_index:end_index]
    print(temperature)

    start_index = html.find("Humidity: ") + len("Humidity: ")
    end_index = html.find("%")
    humidity = html[start_index:end_index]
    print(humidity)

    start_index = html.find("Pressure: ") + len("Pressure: ")
    end_index = html.find("hPa")
    pressure = html[start_index:end_index]
    print(pressure)
    saveToFile(title, temperature, humidity, pressure)


while bool("True"):
    HiveIPList = open("Beehive_IP.txt", "r")
    for line in HiveIPList:
        IpAddress = line.strip()
        IpAddress = "http://" + IpAddress
        time.sleep(1)  ## Set delay till next scrape of MCU
        try:
            scrape(IpAddress)
        except:
            print("The IP " + IpAddress + " is unresponsive!")
            IpAddress = line.strip()
    HiveIPList.close()

