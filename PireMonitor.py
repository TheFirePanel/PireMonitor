#####################################################
#                PireMonitor Beta 1.0               #
#               Designed by Zach Fleck              #
# https://bitbucket.org/TheAlmightyZach/piremonitor #
#####################################################

#Save an Event Log
import logging
logging.basicConfig(filename='Fire_Monitor.log',level=logging.DEBUG)

#Ready GPIO Ports
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #This is GPIO 23, Physical Pin is Pin 16!
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #This is GPIO 24, Physical Pin is Pin 18!
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) #This is GPIO 25, Physical Pin is Pin 22!

#Ready Date/Time Info
import time

def getTime():
    return time.asctime( time.localtime(time.time()))

#Ready Email Server and Settings
import smtplib
server = smtplib.SMTP('smtp.EXAMPLE.com', 587)
server.ehlo()
server.starttls()
myEmail = "EMAIL@EXAMPLE.COM"
toEmail = "8888888888@CARRIER.COM"  #This email is the example if you want texts, ANY email will work here!
server.login(myEmail, "EMAIL_PASS")

#Email Functions                    ***Replace placeholder address here in all messages! (Find and Replace may be helpful!)***
def fireAlarmActive():
    FAAMessage = 'Subject: {}\n\n{}'.format("Fire Alarm Active", "A Fire Alarm Signal has been received at 123 EXAMPLE ST. MYTOWN, STATE. ZIPCODE")
    server.sendmail(myEmail, toEmail, FAAMessage)

def fireAlarmRestore():
    FARMessage = 'Subject: {}\n\n{}'.format("Fire Alarm Restored", "A Fire Alarm has been restored at 123 EXAMPLE ST. MYTOWN, STATE. ZIPCODE")
    server.sendmail(myEmail, toEmail, FARMessage)

def troubleMonitorAlarm():
    TMAMessage = 'Subject: {}\n\n{}'.format("Trouble Monitor Alarm", "A Trouble Monitor Alarm Signal has been received from 123 EXAMPLE ST. MYTOWN, STATE. ZIPCODE")
    server.sendmail(myEmail, toEmail, TMAMessage)

def troubleMonitorRestore():
    TMRMessage = 'Subject: {}\n\n{}'.format("Trouble Monitor Restored", "A Trouble Monitor has been restored at 123 EXAMPLE ST. MYTOWN, STATE. ZIPCODE")
    server.sendmail(myEmail, toEmail, TMRMessage)

def supervisoryAlarmActive():
    SAAMessage = 'Subject: {}\n\n{}'.format("Supervisory Monitor Active", "A Supervisory Signal has been received from 123 EXAMPLE ST. MYTOWN, STATE. ZIPCODE")
    server.sendmail(myEmail, toEmail, SAAMessage)

def supervisoryAlarmRestore():
    SARMessage = 'Subject: {}\n\n{}'.format("Supervisory Monitor Restored", "A Supervisory Signal has been restored at 123 EXAMPLE ST. MYTOWN, STATE. ZIPCODE")
    server.sendmail(myEmail, toEmail, SARMessage)

#Log System Monitor Online
logging.info('Online on %s', getTime())

#Set Default Status to normal
fireStatus = False
troubleStatus = False
supervisoryStatus = False

while True:
    #Respond to Full Fire Alarm
    if GPIO.input(23) == GPIO.LOW and fireStatus == False:
        fireStatus = True
        logging.warning("Fire Alarm Active on %s", getTime())
        fireAlarmActive()
    elif GPIO.input(23) == GPIO.HIGH and fireStatus == True:
        fireStatus = False
        logging.warning("Fire Alarm Restore on %s", getTime())
        fireAlarmRestore()

    #Respond to Trouble Alarm
    if GPIO.input(24) == GPIO.LOW and troubleStatus == False:
        troubleStatus = True
        logging.warning("Trouble Monitor Alarm on %s", getTime())
        troubleMonitorAlarm()
    elif GPIO.input(24) == GPIO.HIGH and troubleStatus == True:
        troubleStatus = False
        logging.warning("Trouble Monitor Restore on %s", getTime())
        troubleMonitorRestore()
        
    #Respond to Supervisory Alarm
    if GPIO.input(25) == GPIO.LOW and supervisoryStatus == False:
        supervisoryStatus = True
        logging.warning("Superviosry Monitor Alarm on %s", getTime())
        supervisoryAlarmActive()
    elif GPIO.input(25) == GPIO.HIGH and supervisoryStatus == True:
        supervisoryStatus = False
        logging.warning("Supervisory Monitor Restore on %s",getTime())
        supervisoryAlarmRestore()
        
GPIO.cleanup()     #On Exit