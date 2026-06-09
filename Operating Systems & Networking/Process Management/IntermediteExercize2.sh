#!/bin/bash

# Start processes
sleep 60 &
PID_A=$!

top &
PID_B=$!

nano &
PID_C=$!

echo "PIDs:"
echo "A: $PID_A"
echo "B: $PID_B"
echo "C: $PID_C"

# List processes
ps -e | grep -E "$PID_A|$PID_B|$PID_C"

# Stop process A
kill -STOP $PID_A
sleep 2

# Resume process A
kill -CONT $PID_A
sleep 2

# Stop process B
kill -STOP $PID_B
sleep 2

# Resume process B
kill -CONT $PID_B

# Kill all
kill $PID_A $PID_B $PID_C

ps -e | grep -E "$PID_A|$PID_B|$PID_C"