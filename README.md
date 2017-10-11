# IntruderDetectionSystem

## Hardware requirements:
1. RPi 3 Model B <br/>
2. Minimum 4GB SD card <br/>
3. Wifi adapter (Optional) <br/>
4. HC-SR04 Module (Ultrasonic sensor) <br/>
5. BISS0001 module (PIR sensor) <br/>
6. Buzzer Alarm Beeper <br/>
7. 1000 Ohm, 330 Ohm and 470 Ohm resistors <br/>
8. Jumper wires <br/>
<br/>

## Software requirements:
1. Flask (micro web framework) <br/>
2. Twilio (cloud communications platform) <br/>
3. Android Studio <br/>
4. Python and related dependencies <br/>
<br/>

## Detailed explanation
The system uses a Passive Infrared Radiation (PIR) motion sensor to detect the presence of a person within a certain range. Once detected, it triggers the ultrasonic sensor to record the distance of the intruder, lights up LEDs, sounds an alarm and notifies the authorized user through a phone call and SMS. <br/>
Raspberry Pi 3 is used to interface the multiple components using the GPIO module of the Rpi Python library. PIR sensor detects the change in infrared radiation when a warm blooded moving object is in its detection range. According to the change in infrared radiation, there will be a voltage signal generated which is then used to turn on the ultrasonic sensor, sound an alarm and turn on the lighting system (LED). Flask micro web framework was installed in the R-Pi to capture and record the distance when the ultrasonic sensor gets turned on. Thus, this saves power consumption and the memory space of the recording system as the LED and ultrasonic sensor are triggered only when PIR sensor detects an object, thus the system starts recording only when the ultrasonic sensor is turned on. Hence, saving memory space. An Android app has been integrated with the system so that users can monitor activity and get alerts in the form of phone calls and text messages.
