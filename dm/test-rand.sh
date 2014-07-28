#!/bin/bash

i=0
j=0
while [ 1 ]
do
    #echo $j
    #i=$(($i+1))
    #if [ "$j" -eq "0" ]
    #then
    #j=1
    #else
    #j=0
    #fi
    echo $(( ( RANDOM % 100 )  - 49 )) $(( ( RANDOM % 100 )  - 49 )) $(( ( RANDOM % 100 )  - 49 )) $(( ( RANDOM % 100 )  - 49 )) $(( ( RANDOM % 100 )  - 49 )) $(( ( RANDOM % 100 )  - 49 ))
    #sleep .035
    sleep 0.1
done
