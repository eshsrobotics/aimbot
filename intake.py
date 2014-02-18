class Intake():

	def __init__(self,wheels,arm,stick):
		self.wheels = wheels
		self.arm = arm
		self.stick = stick

	def iterate(self):
		self.arm.Set(self.stick.GetY())
		wheels = 0

		if self.stick.GetRawButton(3):
			wheels = 1
		elif self.stick.GetRawButton(4):
			wheels = -1
		self.wheels.Set(wheels);
