# README #

Let's get started with Youre PireMonitor setup!

### What is this repository for? ###

* The PireMonitor allows you to use your Raspberry Pi to monitor your Fire Alarm System using the dry contacts from your FACP!
* Beta 1.0

### How do I get set up? ###

* On your Raspberry Pi, you need at least 3 GPIO pins available. By default, the assigned GPIO is 23, 24, and 25 (Physical Pins 16, 18, and 22 on RPI 3)
* In order to set this up, you will need to connect the associated GPIO pin, to the COMMON portion of the relay for Fire, Trouble, and Supervisory.
* Connect the associated Normally Open (NO) contact on the relay to Pin 6 on your Pi (Ground)

+ Download and place the Python script on your Raspberry Pi, be sure to edit information in the file. Information you will need to edit is as follows:
	* SMTP Server
	* myEmail
	* toEmail
	* EMAIL\_PASS
	* Addresses in all messages (If you choose to keep the address, you can set the message to whatever you like)

- Run the script! By default it will not print out any messages, but rather save any events in Fire\_Monitor.log in the same directory as the script.
* I recommend using forever to run the script, and also setting it up to boot with the Pi!

### Who do I talk to? ###

* Is it broken? Create a ticket in the "Issues" page and be as specific as possible! I want to help!
* Have suggestions on how to make it better? I want to know! Look at the ideas I have for the project down below!

### What's coming in the future? ###

+ I have some plans of how I want to improve this!
	* Add a way to supervise the GPIO circuits, causing a trouble if a wire is not connected
	* Come up with a more effective method for constantly searching to see if the state of a relay has changed (less ram heavy)
	* Clean up the code, and make install easier if possible!