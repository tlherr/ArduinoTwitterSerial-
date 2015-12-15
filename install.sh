#!/bin/bash


version=$(python -V 2>&1 | grep -Po '(?<=Python )(.+)')
if [[ -z "$version" ]]
then
    echo "No Python!" 
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    export PATH=/usr/local/bin:/usr/local/sbin:$PATH
    source ~/.bash_profile
    brew install python
fi

pip install python-twitter pyserial
wget https://raw.githubusercontent.com/tlherr/ArduinoTwitterSerial/master/main.py
python main.py
