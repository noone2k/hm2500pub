#!/bin/bash
#
#
#

HOST=BROKER_IP

DEV_TYPE=HMB-4
DEV_MAC=XXxxXXxxXXxx

TOPIC_PUB=hame_energy/$DEV_TYPE/App/$DEV_MAC/ctrl
TOPIC_SUB=hame_energy/$DEV_TYPE/device/$DEV_MAC/ctrl

TOPICX="b2500/#"
TOPIC0=hame_energy/#
TOPIC1=hame_energy/HMB-4/#
TOPIC2=hame_energy/HMB-4/App/$DEV_ID/ctrl
TOPIC3=hame_energy/HMB-4/device/$DEV_ID/ctrl/#

mosquitto_sub -v -h $HOST -t $TOPIC0

