import serial

# Define the serial port settings
port = '/dev/ttyS0'  # Change to the appropriate port, e.g., '/dev/ttyUSB0' or '/dev/ttyAMA0'
baud_rate = 115200  # Match this with your ESP32's baud rate

try:
    # Open a serial connection
    ser = serial.Serial(port, baud_rate)
    
    while True:
        # Read data from ESP32
        data = ser.readline().decode('utf-8').strip()
        if data:
            print(f'Received: {data}')

        # Send data to ESP32
        message = input("Enter a message to send: ")
        ser.write((message + '\n').encode('utf-8'))

except KeyboardInterrupt:
    # Close the serial connection on Ctrl+C
    ser.close()
except Exception as e:
    print(f"An error occurred: {str(e)}")
    ser.close()
