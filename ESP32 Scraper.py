# Created By Vanshdeep Singh
# I will add in comments I promise :)

from urllib.request import urlopen
import datetime
import time
import math
import os

def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


def addvalues(sensordata, linesread):
    sum = 0
    for w in sensordata:
        sum = float(w) + sum
    sum = sum / linesread
    print(sum)
    return sum


def compressdata(filenameforbeehive, beehivename):
    linesread = 1
    beehive = open(filenameforbeehive, "r")
    firstline = beehive.readline().split()
    temperaturenode1 = [firstline[2]]
    temperaturenode2 = [firstline[3]]
    temperaturenode3 = [firstline[4]]
    temperaturenode4 = [firstline[5]]
    temperaturenode5 = [firstline[6]]
    humiditynode1 = [firstline[7]]
    humiditynode2 = [firstline[8]]
    humiditynode3 = [firstline[9]]
    humiditynode4 = [firstline[10]]
    humiditynode5 = [firstline[11]]
    weight = [firstline[12]]

    nextline = beehive.readline().split()
    print("saved into list")
    print(firstline[0])
    print(nextline[0])
    while firstline[0] == nextline[0]:
        linesread += 1
        temperaturenode1.append(nextline[2])
        temperaturenode2.append(nextline[3])
        temperaturenode3.append(nextline[4])
        temperaturenode4.append(nextline[5])
        temperaturenode5.append(nextline[6])
        humiditynode1.append(nextline[7])
        humiditynode2.append(nextline[8])
        humiditynode3.append(nextline[9])
        humiditynode4.append(nextline[10])
        humiditynode5.append(nextline[11])
        weight.append(nextline[12])
        nextline = beehive.readline().split()

    else:
        t1 = truncate(addvalues(temperaturenode1, linesread), 2)
        t2 = truncate(addvalues(temperaturenode2, linesread), 2)
        t3 = truncate(addvalues(temperaturenode3, linesread), 2)
        t4 = truncate(addvalues(temperaturenode4, linesread), 2)
        t5 = truncate(addvalues(temperaturenode5, linesread), 2)
        h1 = truncate(addvalues(humiditynode1, linesread), 2)
        h2 = truncate(addvalues(humiditynode2, linesread), 2)
        h3 = truncate(addvalues(humiditynode3, linesread), 2)
        h4 = truncate(addvalues(humiditynode4, linesread), 2)
        h5 = truncate(addvalues(humiditynode5, linesread), 2)
        w1 = truncate(addvalues(weight, linesread), 2)
        datadump = firstline[0] + " " + str(t2) + " " + str(t3) + " " + str(t4) + " " + str(t5) + " " + str(
            h1) + " " + str(h2) + " " + str(h3) + " " + str(h4) + " " + str(h5) + " " + str(w1)

        try:
            beehivename = beehivename + " Compressed.txt"
            beehivecompressed = open(beehivename, "a")
            beehivecompressed.write(datadump + "\n")

            beehivecompressed.close()
            beehive.close()
            os.remove(filenameforbeehive)
            print("deleted data")
        except:
            print("failed")


def lastline(fname, n):  # This function grabs the last line in the file and then sends it back
    # opening file using with() method
    # so that file get closed
    # after completing work
    with open(fname) as file:
        # loop to read iterate
        # last n lines and print it
        for lastlineinfile in (file.readlines()[-n:]):
            x = lastlineinfile.split()
            file.close()
            return x


def savetofile(beehivename, beehivetemperature, beehivehumidity, beehiveweight):
    currenttime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    currentdate = datetime.datetime.now().strftime("%Y-%m-%d")
    filenameforbeehive = beehivename + ".txt"
    try:
        lastlineoffile = lastline(filenameforbeehive, 1)
        saveddate = lastlineoffile[0]


        if currentdate != saveddate:
            print("Not the same date!")
            datadump = currenttime + " " + beehivetemperature + " " + beehivehumidity + " " + beehiveweight
            beehive = open(filenameforbeehive, "a")
            beehive.write(datadump + "\n")
            beehive.close()
            compressdata(filenameforbeehive, beehivename)
        else:
            print("Current and saved date are the same!")
            datadump = currenttime + " " + beehivetemperature + " " + beehivehumidity + " " + beehiveweight
            beehive = open(filenameforbeehive, "a")
            beehive.write(datadump + "\n")
            beehive.close()
    except:
        print("Saving Sensor data into system")
        datadump = currenttime + " " + beehivetemperature + " " + beehivehumidity + " " + beehiveweight
        beehive = open(filenameforbeehive, "a")
        beehive.write(datadump + "\n")
        beehive.close()


def scrape(ipaddress):
    url = ipaddress
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    start_index = html.find("<h1>") + len("<h1>")
    end_index = html.find("</h1>")
    beehivename = html[start_index:end_index]
    print(beehivename)

    start_index = html.find("Temperature: ") + len("Temperature: ")
    end_index = html.find("&deg;C")
    temperature = html[start_index:end_index]
    print(temperature)

    start_index = html.find("Humidity: ") + len("Humidity: ")
    end_index = html.find("%")
    humidity = html[start_index:end_index]
    print(humidity)

    start_index = html.find("Weight: ") + len("Weight: ")
    end_index = html.find("kg")
    weight = html[start_index:end_index]
    print(weight)
    savetofile(beehivename, temperature, humidity, weight)


while bool("True"):
    HiveIPList = open("Beehive_IP.txt", "r")
    for line in HiveIPList:
        IpAddress = line.strip()
        IpAddress = "http://" + IpAddress

        try:
            scrape(IpAddress)
            #time.sleep(2)  # Set delay till next scrape of MCU
        except:
            print("The IP " + IpAddress + " is unresponsive!")
            IpAddress = line.strip()
    HiveIPList.close()
