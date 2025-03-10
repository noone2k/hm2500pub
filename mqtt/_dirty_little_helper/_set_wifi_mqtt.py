#!/usr/bin/python3

import asyncio
import bleak
import struct
#maybe ;)
import time


# settings to transmit to the B2500 ( maybe config / cmd-line ... needed not that often :) )
mac_address = '94:70:6C:XX:XX:XX'  # <- mui importante ! :)
wifi_ssid = 'internaltest'
wifi_pass = 'lassmichrein'
mqtt_host = '192.168.10.XXX'
mqtt_port = '1883'
mqtt_user = 'noone'
mqtt_pass = 'noone'

### not used ... look down cmd_X ... better build a lib, leave the todo for someone else ;)
#a_wifi = bytearray([0x73,0x06,0x23,0x05])
#a_mqtt = bytearray([0x73,0x06,0x23,0x20])
#a_reboot = bytearray([0x73,0x06,0x23,0x25,0x01])

UUID0 = "0000ff00-0000-1000-8000-00805f9b34fb"
UUID1 = "0000ff01-0000-1000-8000-00805f9b34fb"
UUID2 = "0000ff02-0000-1000-8000-00805f9b34fb"

dbg_print=True

def cmd_simple(ble_cmd, ble_cmd_parm, internal_console_dbg):
    rdat = [0x73, 0x06, 0x23, ble_cmd]

    for b in ble_cmd_parm:
        rdat.append(ord(b))
        #print(f"COMMAND: {b:02x} - {b} - {chr(b)}") 

    rlen = len(rdat)
    rdat[1] = rlen 

    rxor = 0
    for i in range(rlen):
        rxor = rxor ^ rdat[i]

    rdat.append(rxor)

    if dbg_print: 
        for b in rdat:
            print(f"COMMAND: {b:02x} - {b} - {chr(b)}") 

    return rdat

cmd_wifi   = cmd_simple(0x05,wifi_ssid + "<.,.>" + wifi_pass,1)
cmd_mqtt   = cmd_simple(0x20,"0<.,.>" + mqtt_host + "<.,.>" + mqtt_port + "<.,.>" + mqtt_user + "<.,.>" + mqtt_pass + "<.,.>",1)
cmd_reboot = [0x73, 0x06, 0x23, 0x25, 0x01, 0x72]


async def run():
    # Connect to the B2500 device
    async with bleak.BleakClient(mac_address) as client:
        ##### SET WIFI
        #print(a_wifi)
        #await client.write_gatt_char(UUID1, cmd_wifi)

        # maybe rush both commands with a delay ...
        #time.sleep(30)

        ##### SET MQTT
        #print(cmd_mqtt)
        #await client.write_gatt_char(UUID1, cmd_mqtt)
        #time.sleep(30)

        ##### REBOOT TEST
        print(cmd_reboot)
        await client.write_gatt_char(UUID1, cmd_reboot)
        
asyncio.run(run())

