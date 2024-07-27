#!/bin/bash
#
# b2500 - mqtt test

HOST=BROKER_IP

DEV_TYPE=HMB-4
DEV_MAC=XXxxXXxxXXxx


TOPIC_PUB=hame_energy/$DEV_TYPE/App/$DEV_MAC/ctrl
TOPIC_SUB=hame_energy/$DEV_TYPE/device/$DEV_MAC/ctrl

### status abrufen
MSG="cd=01" 		# status abrufen

### lade einstellungen
#MSG="cd=03,md=0"	# load/unload simultan
#MSG="cd=03,md=1"	# load -> unload

### entlade einstellungen
#MSG="cd=04,md=0"	# out1 off / out2 off
#MSG="cd=04,md=1"        # out1 on / out2 off
#MSG="cd=04,md=2"        # out1 off / out2 on
#MSG="cd=04,md=3"        # out1 on / out2 on

### dod
#MSG="cd=05,md=100"	
### threshold
#MSG="cd=06,md=999" 

### time ( > v1 )
#MSG="cd=07,md=0"	# timed mode*
#MSG="cd=07,md=1"	# adaptive ( stromzaehler )*

### set time
#MSG="cd=08,......."	# set time, to be done ....*
#MSG="cd=09,wy= ...."	# set timezone, to be done ...*

### restart / reset / misc
#MSG="cd=10"		# software restart 
#MSG="cd=11"		# factory reset*
#MSG="cd=30"		# error code

#MSG=$@

mosquitto_pub -h $HOST -t $TOPIC_PUB -m $MSG

