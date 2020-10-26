from gpiozero import LED
from time import sleep

class Lights:
	def __init__(self):
		self.red = LED(7)
		self.amber = LED(25)
		self.green = LED(8)

	def set(self, level):
		self.red.off()
		self.amber.off()
		self.green.off()

		if level == 0:
			print("level 1 lights")
			self.green.blink()
			sleep(2)
			self.green.on()
		elif level == 1:
			print("level 2 lights")
			self.amber.blink()
			sleep(2)
			self.amber.on()
		elif level == 2:
			print("level 3 lights")
			self.red.blink()
			sleep(2)
			self.red.on()
		else:
			self.red.on()
			self.amber.on()
			self.green.on()

