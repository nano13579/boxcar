# Firmware

## Notes

To flash RP2040 hold down the bootloader button while powering on. If using Arduino IDE to upload a sketch, the device should automatically go into bootloader mode and should appear as an external drive in your computer. 

Before uploading motor control and accelerometer code make sure to configure HC-05's as master/slave using the program in final/ATcommands.cpp. While plugging your system into power, hold down the button on the HC-05 - this enables AT mode. Open the Serial Monitor and select "Both NL & CR" from the dropdown menu. 

Once you are done with the following steps you can boot both devices normally and upload other firmware as the communication preferences between HC-05's should be saved.

### Steps to set HC-05 as slave:

Enter `AT` into the Serial Monitor - response should be 'OK'

Enter `AT+ROLE=0` which will set the module as slave - response should be 'OK'

Enter `AT+ADDR?` which will return the AT address of the module (necessary for sending data from m to s) - response should look something like 123.45.hello


### Steps to set HC-05 as master:

Enter `AT` again - response 'OK'

Enter `AT+ROLE=1` sets to master - response 'OK'

Enter `AT+CMODE=0` which enable connection through an address - response 'OK'

Enter `AT+BIND=123,45,hello` (slave AT address here with commas) enables communication with the specific address listed - response 'OK'
