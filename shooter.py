SERVO_TOP_VALUE = 1 #needs to be actually found
SERVO_BOTTOM_VALUE = 0 #needs to be actually found
class Shooter():
  def __init__(self,main_motor,encoder,servo,stick):
    self.main_motor = main_motor
    self.encoder = encoder
    self.servo = servo
    self.servo_enabled = False
    self.stick = stick

  def iterate(self):
    if self.stick.GetRawButton(5):
      self.servo_enabled = True
    elif self.stick.GetRawButton(4):
      self.servo_enabled = False
    print encoder
    if self.servo_enabled:
      self.servo.Set(SERVO_TOP_VALUE)
    else:
      self.servo.Set(SERVO_BOTTOM_VALUE)
    
    #Stuff to control main motor