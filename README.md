# Ultrasonic Distance Measurement Project

## Project Title: Ultrasonic Distance Measurement with OLED Display

### Overview
This project involves using an ultrasonic sensor to measure distance and display the results on an OLED display using a Raspberry Pi 4 Model B. The ultrasonic sensor detects the distance to an object, and the OLED provides a visual representation of that measurement.

### Components Required
- **Raspberry Pi 4 Model B**
- **Ultrasonic Sensor (e.g., HC-SR04)**
- **OLED Display (128x64)**
- **Breadboard**
- **Jumper Wires**

### Circuit Connections

#### Ultrasonic Sensor (HC-SR04)
- **VCC**: Connect to 5V on Raspberry Pi (Pin 2)
- **GND**: Connect to GND on Raspberry Pi (Pin 6)
- **TRIG**: Connect to GPIO 23 (Pin 16)
- **ECHO**: Connect to GPIO 24 (Pin 18)

#### OLED Display (128x64)
- **GND**: Connect to GND on Raspberry Pi (Pin 6)
- **VCC**: Connect to 3.3V on Raspberry Pi (Pin 1)
- **SDA**: Connect to GPIO 2 (Pin 3)
- **SCL**: Connect to GPIO 3 (Pin 5)

### Software Requirements
Make sure to install the required Python packages. You can do this by running the following commands in the terminal:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install adafruit-circuitpython-ssd1306
pip3 install adafruit-circuitpython-busdevice
