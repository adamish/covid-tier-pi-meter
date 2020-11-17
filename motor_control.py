
from gpiozero import Button
from gpiozero import LED
from time import sleep

class Motor:

    def __init__(self, motor_pin1, motor_pin2, encoder_pin):
        self.counter = 0
        self.encoder = Button(encoder_pin)
        self.encoder.when_pressed=self.rise
        self.encoder.when_released=self.rise

        self.m1 = LED(motor_pin1)
        self.m2 = LED(motor_pin2)
        self.target = 0

    def rise(self):
        self.counter = self.counter + 1
        self.target_check()

    def fall(self):
        self.counter = self.counter + 1
        self.target_check()

    def forwards(self):
        self.m1.on()
        self.m2.off()

    def stop(self):
        self.m1.off()
        self.m2.off()

    def backwards(self):
        self.m1.off()
        self.m2.on()

    def goto(self, target):
        self.counter = 0
        self.target = abs(target)
        if target > 0:
            self.forwards()
        else:
            self.backwards()

    def target_check(self):
        print("counter " + str(self.counter))
        if self.counter >= self.target:
            self.stop()

motor = Motor("GPIO7", "GPIO8", "GPIO25")
while True:
    motor.goto(4)
    sleep(7)

sleep(10000)
