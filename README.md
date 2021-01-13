# Python-Example

Examples here demonstrate how to acquire data in both ascii and binary modes

**Prerequisites**:

1) Install Python

2) Install Pyserial and Keyboard from command prompt
    - python -m pip install -U pyserial --user
    - python -m pip install -U keyboard --user

3) Firmware 1.35 or higher is recommended https://github.com/dataq-instruments/Firmware_Upgrade. Earlier version of firmware may not work properly in binary mode

4) Understand the protocol, please refer to  https://www.dataq.com/resources/pdfs/misc/Dataq-Instruments-Protocol.pdf

5) Turn 2xxx/1xxx/4xxx into CDC mode: plug the device to USB port, if the LED already blinks Yellow, stop, you are already in CDC mode. If not, once the LED turns blinking Green, push and hold the button immediately (within 5 second time frame), the LED should turn white, hold until LED turns Red, then release the button, now the LED will blink yellow to indicate CDC mode. If you need to exit CDC mode, repeate the same action and a green blinking LED will indicate LibUSB mode.

6) From Windows Device Manager, find out the COM port of the device connected to, and modify the program accordingly<br/>
![alt text](https://www.dataq.com/resources/repository/matlab_devicemanager.png)

**Other Examples**

1) https://github.com/dataq-instruments/Python1110

2) https://github.com/dataq-instruments/Simple-Python-Codes-for-DI-1110

3) https://github.com/dataq-instruments/Python245

4) https://github.com/dataq-instruments/Python

**Note**:

1) If you see error message complaining “failed "import serial module" or "seial doesn't have the attribue of serial", You may have multiple installations of Pythons on your PC, if that's case, please unstall all first before reinstall

2) To single step through PY codes, follow
https://stackoverflow.com/questions/4929251/how-to-step-through-python-code-to-help-debug-issues

