from gpiozero import LED
from gpiozero import Button
from time import sleep

button = Button (2)

leds: []
pinsleds : [ 17, 16, 25, 24 ]
count = 0
numcount = 0

for pin in pinsleds:
    newled = LED (pin)
    leds.append(newled)

while True:
	button.wait_for_press()
	count = count + 1
	if count > 10:
		count = 0
	numcount = count 
	for i in range(4):
		if (numcount % 2) != 0:	# evaluó el bit menos significativo
			leds[i].on
		else:
			leds[i].off
		numcount = numcount // 2	# desplazo un bit a la derecha
	sleep(1)
