# Created By Vanshdeep Singh
import datetime
import math
import os
import time
from urllib.request import urlopen


def truncate(number, decimals=0):  # Compress the decimal places to 2 instead of 10
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


def addvalues(sensordata, linesread):  # Function that adds sensor values together
    sum = 0
    for w in sensordata:
        sum = float(w) + sum
    sum = sum / linesread  # Does total sensor value divide by how many data points
    return sum


def compressdata(filenameforbeehive, beehivename):  # Compressed the data if a new day is detected
    linesread = 1  # Used to find the total and divide by is to get the average
    beehive = open(filenameforbeehive, "r")  # Open beehive file
    firstline = beehive.readline().split()  # Read the first line of that file and split it into strings and put into list
    temperaturenode1 = [firstline[2]]  # Now it grabs each value and stores them in separate lists
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

    nextline = beehive.readline().split()  # Grab next line nad put into another list.
    while firstline[0] == nextline[
        0]:  # Compare the first values which are the dates and see if they match. If they do then start adding the values into the lists we just created
        linesread += 1  # Add up so we can get average
        temperaturenode1.append(
            nextline[2])  # This for example is just adding the next lines temperature node 1 value into the list
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
        nextline = beehive.readline().split()  # Grab next line and repeat

    else:  # Once the dates are no longer matching then add each list together but they also have to be converted from str to float.
        beehive.close()  # Close beehive file
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
        datadump = firstline[0] + " " + str(t1) + " " + str(t2) + " " + str(t3) + " " + str(t4) + " " + str(
            t5) + " " + str(
            h1) + " " + str(h2) + " " + str(h3) + " " + str(h4) + " " + str(h5) + " " + str(
            w1)  # Information that will be dumped into hive name compressed.tx file
        beehivename = beehivename + " Compressed.txt"  # This is now the new file for the compressed data
        beehivecompressed = open(beehivename, "a")  # append to the end of file
        beehivecompressed.write(datadump + "\n")  # dump data
        beehivecompressed.close()  # Close compressed file
        os.remove(filenameforbeehive)  # Delete the normal beehive file to basically delete the log
        ##Add code here to make it so it saves the recent data
        print("Compressed Data!")


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


def savetofile(beehivename, beehivetemperature, beehivehumidity,
               beehiveweight):  # Takes in values that need to be saved
    currenttime = datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S")  # Current time all the way to the second. This gets saved into the log
    currentdate = datetime.datetime.now().strftime(
        "%Y-%m-%d")  # Only the current date. This gets used to know if a new day has occured at which point the system will compress and delete extra data. compressdata function explains it more
    filenameforbeehive = beehivename + ".txt"  # Creates the Beehive file name based on what the website says it is
    try:
        lastlineoffile = lastline(filenameforbeehive,
                                  1)  # Function that grabs the last line of the beehive file IF it exist
        saveddate = lastlineoffile[
            0]  # Saves the first value which is the Date saved. This is used for the compressdata function
        datadump = currenttime + " " + beehivetemperature + " " + beehivehumidity + " " + beehiveweight  # Create string to dump into end of file. We have to still save the information because when it compresses the system needs a diffrent date to know when to stop compressing
        if (datadump.find('nan') != -1):
            print("Sensor Reading Null!")
            return

        else:
            if currentdate != saveddate:  # if the current real time date IS NOT the same as the most recently saved date then Begin compression
                print("New Day Detected!")
                beehive = open(filenameforbeehive, "a")  # open file and append
                beehive.write(datadump + "\n")  # save the data
                beehive.close()  # close the file
                compressdata(filenameforbeehive, beehivename)  # Start compression function
                beehive = open(filenameforbeehive, "a")  # open file and append
                beehive.write(datadump + "\n")  # save the data
                beehive.close()  # close the file
            else:  # If current real time date IS the same then just save normally
                print("Same Day Detected!")
                beehive = open(filenameforbeehive, "a")  # open file and append
                beehive.write(datadump + "\n")  # save the data
                beehive.close()  # close the file
    except:
        print("File Not Found Creating New File Being Made. This Might Be Because The Data Was Recently Compressed")
        datadump = currenttime + " " + beehivetemperature + " " + beehivehumidity + " " + beehiveweight  # Create string to dump into end of file.
        beehive = open(filenameforbeehive, "a")  # open file and append
        beehive.write(datadump + "\n")  # save the data
        beehive.close()  # close the file


def scrape(ipaddress):  # Takes in the IP address of the Beehive that it needs to scrape
    url = ipaddress
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    start_index = html.find("<h1>") + len(
        "<h1>")  # Filter to grab the Beehive Name. This gets used to set the file name of the hive
    end_index = html.find("</h1>")
    beehivename = html[start_index:end_index]
    name = "Working on " + beehivename
    print(name)

    start_index = html.find("Temperature: ") + len("Temperature: ")  # Filter to grab the Temperature Nodes
    end_index = html.find("&deg;F")
    temperature = html[start_index:end_index]

    start_index = html.find("Humidity: ") + len("Humidity: ")  # Filter to grab the Humidity Nodes
    end_index = html.find("%")
    humidity = html[start_index:end_index]

    start_index = html.find("Weight: ") + len("Weight: ")  # Filter to Grab the Weight of the hive
    end_index = html.find("lb")
    weight = html[start_index:end_index]

    savetofile(beehivename, temperature, humidity, weight)  # Function that sends information to be saved

def getnextip():
    HiveIPList = open("Beehive_IP.txt", "r")  # open Beehive Ip list. This holds all IP's that the beehives are on.
    for line in HiveIPList:  # For statment reads each line of the beehive ip file
        IpAddress = line.strip()  # Grabs the line
        IpAddress = "http://" + IpAddress  # Turns it into a URL

        try:  # Try statement in case the IP is unresponsive
            scrape(IpAddress)  # Function that beings the scraping process
            time.sleep(2)  # Set delay for the next IP it scrapes. Only change if it is collecting data to fast or want to make it run slower to save battery life if they are solar powered
        except:
            print("The IP " + IpAddress + " is unresponsive!")  # If ip fails tell user.
            IpAddress = line.strip()  # Gets next line in ip list
    HiveIPList.close()  # Once at the end of list the while loop will being the process again


while bool("True"):  # Will run forever
    getnextip()
