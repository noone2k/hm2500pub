#!/bin/bash
#
#
#

HOST=BROKER_IP

DEV_TYPE=HMB-4
DEV_MAC=XXXXXXXXXXXX

TOPIC_PUB=hame_energy/$DEV_TYPE/App/$DEV_MAC/ctrl
TOPIC_SUB=hame_energy/$DEV_TYPE/device/$DEV_MAC/ctrl

declare -A shorts_diz
shorts_diz[p1]="PV 1 - State     "
shorts_diz[p2]="PV 2 - State     "
shorts_diz[w1]="PV 1 - Power     "
shorts_diz[w2]="PV 2 - Power     "
shorts_diz[pe]="Battery - %      "
shorts_diz[vv]="Device - Version "
shorts_diz[cs]="Charge           "
shorts_diz[cd]="Discharge        "
shorts_diz[am]="AM               "
shorts_diz[o1]="OUT 1 - State    "
shorts_diz[o2]="OUT 2 - State    "
shorts_diz[do]="DOD              "
shorts_diz[lv]="Threshold        "
shorts_diz[cj]="Scene            "
shorts_diz[kn]="Battery - kWh    "
shorts_diz[g1]="OUT 1 - Power    "
shorts_diz[g2]="OUT 2 - Power    "
shorts_diz[b1]="Powerpack 1      "
shorts_diz[b2]="Powerpack 2      "
shorts_diz[tl]="Temp - Min       "
shorts_diz[th]="Temp - Max       "
shorts_diz[tc]="Temp - Alarm - C "
shorts_diz[tf]="Temp - Alarm - D "
shorts_diz[fc]="FC41D - Version  "

### V2
shorts_diz[md]="Discharge mode   "
shorts_diz[d1]="Time1 enabled    "
shorts_diz[e1]="Time1 start time "
shorts_diz[f1]="Time1 end time   "
shorts_diz[h1]="Time1 power      "
shorts_diz[d2]="Time2 enabled    "
shorts_diz[e2]="Time2 start time "
shorts_diz[f2]="Time2 end time   "
shorts_diz[h2]="Time2 power      "
shorts_diz[d3]="Time3 enabled    "
shorts_diz[e3]="Time3 start time "
shorts_diz[f3]="Time3 end time   "
shorts_diz[h3]="Time3 power      "
shorts_diz[sg]="Sensor connected "
shorts_diz[sp]="Sensor Range ?   "
shorts_diz[st]="Sensor Value     "

### V2 ~ fw 215
shorts_diz[id]="ID               "
shorts_diz[a0]="Powerpack 0 %    "
shorts_diz[a1]="Powerpack 1 %    "
shorts_diz[a2]="Powerpack 2 %    "
shorts_diz[l0]="Load State 0     "
shorts_diz[l1]="Load State 1     "
shorts_diz[sv]="Device Subversion"

### V2 ~ fw 216
shorts_diz[c0]="C0 ???           "
shorts_diz[c1]="C1 ???           "

### V2 ~ fw 216 - split 15
shorts_diz[ws]="WS ???           "
shorts_diz[r3]="R3 ???           "
shorts_diz[r4]="R4 ???           "
shorts_diz[r5]="R5 ???           "
### V2 ~ fw 216 - split 16
shorts_diz[m1]="M1 ???           "
shorts_diz[m2]="M2 ???           "
shorts_diz[i1]="I1 ???           "
shorts_diz[i2]="I2 ???           "
shorts_diz[e1_]="E1 ???           "
shorts_diz[e2_]="E2 ???           "


break_loop=0
m_array=()
OLD_IFS=$IFS
IFS=','

while [ $break_loop != 1 ]; do
        ANSWER=`mosquitto_sub -C 1 -h $HOST -t $TOPIC_SUB`
        [ ${#ANSWER} -le 100 ] && DIZ_=1
        read -ra m_array <<< "$ANSWER"
        echo "- " $ANSWER " ( ${#ANSWER} )"

        if [[ $ANSWER == a0* ]]; then
                echo "Zellinfos"
                for i in "${m_array[@]}"; do
                    short=`echo $i | sed -e 's/=.*//'`
                    [[ $short == a* ]] && short="${short/a/"intern "}"
                    [[ $short == b* ]] && short="${short/b/"extra1 "}"
                    [[ $short == c* ]] && short="${short/c/"extra2 "}"
                    value=`echo $i | sed -e 's/.*=//'`
                    echo -e "$short : $value"
                done
        else
                DIZ_=0
                for i in "${m_array[@]}"; do
                    short=`echo $i | sed -e 's/=.*//'`
                    value=`echo $i | sed -e 's/.*=//'`
                    DIZ=${shorts_diz[$short]}
                    [ $DIZ_ -eq 1 ] && [ "$short" == "e1" ] && DIZ=${shorts_diz[$short"_"]}
                    [ $DIZ_ -eq 1 ] && [ "$short" == "e2" ] && DIZ=${shorts_diz[$short"_"]}
                    echo -e "$short - $DIZ : $value"
                done
        fi
        echo "----------- done -----------"
        [ "$ANSWER" == "exit" ] && break_loop=1
done

IFS=$OLD_IFS
