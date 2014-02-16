class Intake():
	def __init__(self,wheels,arm,stick):
		self.wheels = wheels
		self.arm = arm
		self.stick = stick
	def iterate(self):
		self.arm.set(stick.GetY())
		wheels_val = 0
		if stick.GetRawButton(3):
			wheels = 1
		elif stick.GetRawButton(4):
			wheels = -1
		self.wheels.set(wheels_val);
		#buttonState = stick.GetRawButton(4)