#!/bin/bash

# Process data
pid=("P1" "P2" "P3")
arrival=(0 2 4)
burst=(5 3 4)

n=3
current_time=0

echo "PID  AT  BT  ST  CT"

for ((i=0;i<n;i++))
do
    if [ $current_time -lt ${arrival[$i]} ]
    then
        current_time=${arrival[$i]}
    fi

    start=$current_time
    completion=$((current_time + burst[$i]))

    echo "${pid[$i]}   ${arrival[$i]}   ${burst[$i]}   $start   $completion"

    current_time=$completion
done