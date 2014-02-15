class Intake():
	def __init__(self,motor,stick):
		self.motor = motor
		self.stick = stick
	def iterate(self):
		self.motor.set(stick.GetThrottle())
		#buttonState = stick.GetRawButton(4)