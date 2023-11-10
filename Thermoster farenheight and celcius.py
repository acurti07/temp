import machine
import time
import math

# Define the ADC pin
adc = machine.ADC(machine.Pin(27))

# Define the LED control pins
led_pins = [machine.Pin(pin, machine.Pin.OUT) for pin in [13, 14, 15, 16, 17, 18, 19]]  # Replace with appropriate GPIO pins

led_temp_ranges = {
    (0, 18): 0,    # 0 LEDs on for temperature less than 60°C
    (18, 20): 1,   # 1 LED on for 60-65°C range
    (20, 25): 2,   # 2 LEDs on for 65-70°C range
    (25, 30): 3,   # 3 LEDs on for 70-75°C range
    (30, 100): 7,  # 7 LEDs on for 75-100°C range
}

# Thermistor parameters
R0 = 10000  # Resistance at a known temperature (in ohms)
T0 = 19     # Known temperature (in degrees Celsius)
Beta = 3950 # Beta value of the thermistor

# Read and convert the thermistor data
def read_thermistor():
    raw_value = adc.read_u16()
    
    # Avoid division by zero or very low readings
    if raw_value <= 0:
        return -1  # You can use a negative value to indicate an error
    
    voltage = (raw_value / 65535.0) * 3.3
    resistance = R0 / ((3.3 / voltage) - 1)

    temperature = 1.0 / ((1.0 / (T0 + 273.15)) + ((1.0 / Beta) * math.log(resistance / R0))) - 273.15
    return temperature

#Farenheight=((temperature* 2) +30)

def set_leds(temperature):
    for temp_range, num_leds in led_temp_ranges.items():
        if temp_range[0] <= temperature < temp_range[1]:
            for i, led in enumerate(led_pins):
                led.value(i < num_leds)  # Turn on LEDs up to the specified number
            break
    else:
        for led in led_pins:
            led.value(0)  # Turn off all LEDs if temperature is outside the defined ranges

while True:
    temp = read_thermistor()
    faren = 2*temp+30
    if temp >= 0:  # Check for valid temperature readings
        print("Temperature: {:.2f}°C".format(temp))
        print("Temperature: {:.2f}*F".format(faren))
        set_leds(temp)  # Control LEDs based on the temperature
    else:
        print("Error: Invalid ADC reading")
        for led in led_pins:
            led.value(0)  # Turn off all LEDs in case of an error
    time.sleep(1)  # Delay for reading at an interval
    

mqtt_host="io.adafruit.com"
mqtt_username="Aidan_curtin"
Mqtt_password="aio_aMYU03Uo63sxJWShTdEuZA0Fi0qN"
mqtt_publish_topic1="Aidan_curtin/feeds/temp-feed"
mqtt_client_id="Aidan"

mqtt_client = MQTTClient(
    client_id=mqtt_client_id,
    server=mqtt_host,
    user=mqtt_username,
    password=mqtt_password
    )
mqtt_client.publish(mqtt_publish_topic1, str(temp))
mqtt_client.publish(mqtt_publish_topic2, str(faren))

mqtt_client.connect()
