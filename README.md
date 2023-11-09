The Pyscript code is a code that uses the CSV image processing library in order to upload the most abundant color in a recorded image to an airtable. 
This data comes in tnhe fourm of either red, blue, or green.
This data is then processed in the thermistor code. Wherein a get request (which I coukldnt figure out) gets information from airtable
in order to adjust the uploaded thermistor readings acordingly. I however opted to make the thermistor operate differently, and made it record and 
publish both the farenheight and celcius measurments of the thermistor. Based on the recorded temperature, a series of LED's light up to display
a range of temperatures. The pico housing the thermistor code then uploads the farenheight or celcius information to adafruit dashboard, where a 
graphic is constructed, and recorded data is published. 

The Mqtt thermistor code was MQTT code ran on the pico to allow the system as a whole to operate. It utalized an MQTT library. 
