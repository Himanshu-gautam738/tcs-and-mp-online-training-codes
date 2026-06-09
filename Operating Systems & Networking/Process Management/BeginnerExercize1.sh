#!/bin/bash

ps -e

ps -eo pid,comm,stat | head -n 10

top -n 1 | head -n 15