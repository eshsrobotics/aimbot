SERVO_TOP_VALUE = 1 #needs to be actually found
SERVO_BOTTOM_VALUE = 0 #needs to be actually found
class Intake():
  def __init__(self,first_motor,second_motor,servo,stick):
    self.first_motor = first_motor
    self.second_motor = second_motor
    self.servo = servo
    self.servo_enabled = False
    self.stick = stick

  def iterate(self):
    if self.stick.GetRawButton(5):
      self.servo_enabled = True
    elif self.stick.GetRawButton(4):
      self.servo_enabled = False

    if self.servo_enabled:
      self.servo.Set(SERVO_TOP_VALUE)
    else:
      self.servo.Set(SERVO_BOTTOM_VALUE)
    
    #Stuff to control main motors