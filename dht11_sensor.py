import RPi.GPIO as GPIO
import dht11
import time
import datetime
import csv
import tkinter as tk
from tkinter import messagebox
import threading

# GPIO setup
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)

# GPIO pin 17
sensor = dht11.DHT11(pin=17)

#reading of sensor function 
def sensor_reading():
    while not exit_event.is_set():  
        try:
            time.sleep(1)  # wait 
            s_reading = sensor.read()
            if s_reading.is_valid():
                time_mark = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                temp = s_reading.temperature
                humidity = s_reading.humidity

                # Print sensor data
                print(f"Time: {time_mark}")
                print(f"Temperature: {temp}C")
                print(f"Humidity: {humidity}%")

                # Send sensor data to CSV file
                with open("s_results.csv", mode="a", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([time_mark, temp, humidity])

            else:
                print("Sensor reading not found.")

        except Exception as e:
            print(f"Error: {e}")

def cleanup():
    GPIO.cleanup()

def finish():
    if messagebox.askokcancel("Exit", "The sensor reading will now end."):
        exit_event.set()  # Signal the thread to stop
        data_read.join()  # Wait for the thread to end
        cleanup()
        root.destroy()

# GUI setup
root = tk.Tk()
root.title('Temp/Humidity Sensor')

t_button = tk.Button(root, text='Click to test', command=lambda: messagebox.showinfo("Note", "Sensor Reading begins."))
t_button.pack(pady=20)

exit_button = tk.Button(root, text='Exit', command=finish)
exit_button.pack(pady=20)

# Start the sensor reading 
exit_event = threading.Event()  
data_read = threading.Thread(target=sensor_reading, daemon=True)
data_read.start()

root.protocol("WM_DELETE_WINDOW", finish)
root.mainloop()
