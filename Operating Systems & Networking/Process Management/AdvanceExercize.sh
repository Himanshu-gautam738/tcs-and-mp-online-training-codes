#!/bin/bash

ref=(2 3 2 1 5 2 4 5 3 2 5)
frames=3

declare -a frame
declare -a recent

faults=0
time=0

for page in "${ref[@]}"
do
    found=0

    for ((i=0;i<frames;i++))
    do
        if [ "${frame[$i]}" == "$page" ]
        then
            found=1
            recent[$i]=$time
            break
        fi
    done

    if [ $found -eq 0 ]
    then
        ((faults++))

        if [ ${#frame[@]} -lt $frames ]
        then
            frame+=($page)
            recent+=($time)
        else
            lru_index=0
            min=${recent[0]}

            for ((i=1;i<frames;i++))
            do
                if [ ${recent[$i]} -lt $min ]
                then
                    min=${recent[$i]}
                    lru_index=$i
                fi
            done

            frame[$lru_index]=$page
            recent[$lru_index]=$time
        fi
    fi

    ((time++))

    echo "Frames: ${frame[@]}"
done

echo "Total Page Faults: $faults"