# Raspberry Pi TAP Controller

## Introduction
This project involves creating a Python-based JTAG TAP controller using a Raspberry Pi. 
The aim is to utilize the GPIO pins of the Raspberry Pi to interface with a Digilent Nexys3 board, leveraging the JTAG protocol for debugging and testing silicon devices.
This document provides all necessary details to set up, configure, and operate the Raspberry Pi for this purpose.

## Prerequisites
### Hardware
- Raspberry Pi (Any model that supports GPIO)
- Micro SD card (8GB recommended)
- Ethernet cable or WiFi USB dongle
- HDMI cable for display
- Digilent Nexys3 board
  
### Software
- Raspbian or any compatible Linux distribution
- Python 3 and associated libraries

## Setup Instructions
1. Operating System Installation
Download and install Raspbian on the Raspberry Pi. Installation guide available here.
2. Network Configuration
Connect your Raspberry Pi to the internet via Ethernet or WiFi. Detailed steps can be found here.
3. Enable SSH
Enable SSH on your Raspberry Pi to allow remote access. Follow the instructions here.
4. GPIO Setup
Configure the GPIO pins as required for the project. Instructions are available here.

## Project Configuration
1. Clone Project Repository
Obtain the project files from the course website and extract them on your Raspberry Pi.
2. Install Required Python Libraries
Open a terminal and run the following commands:

`sudo apt-get update
sudo apt-get install python3 python3-pip
sudo pip3 install RPi.GPIO colorama
`
3. Run the TAP Controller Script
Navigate to the project directory and execute the main script:

`cd path/to/project
python3 tap_controller.py
`
## Usage
After setting up the project as described above, execute the script to interact with the Nexys3 board via the JTAG interface. 
The script provides a CLI for sending commands and receiving responses from the board.

## Troubleshooting
- Ensure all physical connections are secure and correctly configured.
- Verify network settings if remote access is not functioning.
- Refer to the Adafruit tutorials linked above for detailed troubleshooting steps.

## Conclusion
This README provides guidance on setting up and running the Raspberry Pi TAP Controller project. 
It is designed to assist users in interfacing with a Nexys3 board for educational and debugging purposes. 
For further assistance, consult the project documentation or reach out: rmuttha@pdx.edu.



  
