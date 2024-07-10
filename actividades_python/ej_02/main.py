from gpiozero import LED
from time import sleep

ledVERDE = LED(13)
ledROJO = LED(19)
ledAZUL = LED(26)

while True:
	sleep(0.25)
	ledVERDE.on()
#prender el led verde por 0,25seg.
	sleep(0.25)
	ledVERDE.off()
	ledAZUL.on()
# tras 0,5 seg, se enciende el led azul.
	sleep(0.25)
	ledVERDE.on()
	sleep(0.25)
	ledVERDE.off()
	ledAZUL.off()
	ledROJO.on()
#despues pasar 1 seg se apagan los 2 led´s anteriores y se enciende el rojo 
	sleep(0.25)
	ledVERDE.on()
	sleep(0.25)
	ledVERDE.off()
	ledAZUL.on()
	sleep(0.25)
	ledVERDE.on()
	sleep(0.25)
#pasan 2 seg y se apagan todos los led´s
	ledVERDE.off()
	ledAZUL.off()
	ledROJO.off()
