# Raspberry Pi Clock Project

## Overview

This project uses a Raspberry Pi to control a motor using keyboard input and timing. It simulates a clock, running at a user-set speed.


## Hardware Required

* 28BYJ-48 Stepper Motor
* ULN2003 Motor Driver Module
* Raspberry Pi
* T-board (GPIO extension board)
* Breadboard


## Assembly Instructions

### Motor + Driver

* Plug the stepper motor into the **white connector** on the ULN2003 driver board.

### Power

* Connect:

  * `+` to 5V on Raspberry Pi
  * `-` to GND on Raspberry Pi

### Control Pins

Connect driver inputs to GPIO:

| Driver Pin | Raspberry Pi GPIO |
| ---------- | ----------------- |
| IN1        | GPIO17            |
| IN2        | GPIO18            |
| IN3        | GPIO27            |
| IN4        | GPIO22            |

### GPIO Extension (T-board)

* Use a ribbon cable to connect the T-Cobbler to the Raspberry Pi
* Make sure:

  * The **red stripe aligns with Pin 1** (near the SD card slot)
  * The cable orientation matches the **"J" column** on the breadboard


## CAD Files

* Available as:

  * Fusion archive files
  * STL files

### Parts to print:

* `StepperMotorArmV2`
* `clockBody`

### Notes:

* Other arms in CAD files are compatible with different motors
* A test body is included for experimenting with motor peg spacing in CAD files


## Starting the Program

### 1. Set up your Raspberry Pi

* Connect your Raspberry Pi (with Raspberry Pi OS or simular installed) to:

  * Monitor
  * Keyboard
  * Mouse
* Power it on and open the Terminal.

### 2. Open the Terminal

* Click the terminal icon in the top menu bar
  OR
* Press: `Ctrl + Alt + T`

### 3. Navigate to your file

Use the `cd` command to go to the folder containing your script:

```bash
cd /path/to/your/file
```

### 4. Run the program

```bash
python3 main.py
```


## Using the Program

* Follow the instructions printed in the terminal.
* Use the following during calibration:

  * **Left Arrow** to rotate motor left
  * **Right Arrow** to rotate motor right
* Use the following  afterwards:

  * 1 to rotate the clock hand at one rotation per minute
  * 2 to rotate the clock hand at one rotation per hour
  * 3 to rotate the clock hand at one rotation every 12 hours
* Press **Enter repeatedly** or **Ctrl + C** to stop the program at any time.


## More Information

For images and additional details, visit:

https://www.notion.so/Raspberry-Pi-Clock-34dec355cc71804cb621e4a4db88a392?source=copy_link

