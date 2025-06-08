avrdude -c stk500v1 -b 19200 -P /dev/ttyACM0 -p t85 -U flash:w:/home/milhas/.var/app/cc.arduino.IDE2/cache/arduino/sketches/D2F017C87D1E9D0E3BF83EB13CA91CFE/key_v2.ino.hex -U lfuse:w:0xe2:m -U hfuse:w:0xdd:m -U efuse:w:0xfe:m

rm -rf /home/milhas/.var/app/cc.arduino.IDE2/cache/arduino/sketches/D2F017C87D1E9D0E3BF83EB13CA91CFE/key_v2.ino.hex