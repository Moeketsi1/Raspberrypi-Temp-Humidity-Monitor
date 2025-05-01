# Raspberrypi-Temp-Humidity-Monitor

A Raspberry Pi-based system for real-time temperature and humidity monitoring using a DHT11 sensor. This project features a Python-based GUI for user interaction and logs sensor data to a CSV file for future analysis.

The primary goal of this project is to build a responsive and interactive temperature and humidity monitoring system using a DHT11 sensor connected to a Raspberry Pi. The system logs environmental data with timestamps and presents it via a simple GUI built using Tkinter.

Key Features
  * Real-time monitoring of temperature and humidity

  * CSV data logging with timestamps

  * Simple graphical user interface (GUI)

  * Threaded sensor reading for smooth GUI performance

  * Safe shutdown with GPIO cleanup

Hardware Requirements:
  *  Raspberry Pi (any model with GPIO support)

  * DHT11 temperature & humidity sensor

  * Female-to-female jumper wires

  * SD card with Raspberry Pi OS (32-bit Bullseye legacy preferred)

System Architecture:
 * Components:
  
  * Raspberry Pi – main controller and processing unit

  * DHT11 – digital sensor for temperature & humidity

  * Python Scripts – handles data capture, GUI, logging

  * CSV File – stores timestamped readings for analysis

How It Works: 
 * The DHT11 sensor reads temperature and humidity every second.

 * Readings are validated, displayed on the GUI, and saved with timestamps in s_results.csv.

 * A separate thread handles the sensor reading, keeping the GUI responsive.

 * When the application exits, all threads are safely terminated and GPIO pins are reset.
