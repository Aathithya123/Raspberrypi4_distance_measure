import time
import board
import busio
import adafruit_ssd1306
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont


TRIG = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
i2c = busio.I2C(board.SCL, board.SDA)
oled_width = 128
oled_height = 64
oled = adafruit_ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0)
oled.show()
font = ImageFont.load_default()

def measure_distance():
    GPIO.output(TRIG, False)
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

try:
    while True:
        distance = measure_distance()
        print(f"Distance: {distance} cm")
        oled.fill(0)
        image = Image.new("1", (oled_width, oled_height))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), f"Distance: {distance} cm", font=font, fill=255)
        oled.image(image)
        oled.show()
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
