from datetime import datetime, timedelta

LOWERING_SERVO_TOP_VALUE = 0.4 #needs to be actually found
LOWERING_SERVO_BOTTOM_VALUE = 0.1 #needs to be actually found

LOWERING_TOTAL_PERIOD = timedelta(seconds=1.6)
LOWERING_PERIOD = timedelta(seconds=0.5)
LOWERING_SERVO_PERIOD = timedelta(seconds=1)

SHOOTING_TOTAL_PERIOD = timedelta(seconds=0.8)
SHOOTING_SERVO_DOWN_PERIOD = timedelta(seconds=0.4)
SHOOTING_ARM_UP_PERIOD = timedelta(seconds=0.2)

class Shooter():
  def __init__(self,main_motor,encoder,servo,stick,shooter_service):
    self.main_motor = main_motor
    self.encoder = encoder
    self.servo = servo
    self.servo_enabled = False
    self.stick = stick
    self.counter = 0
    self.loweringNextTotal = datetime.now()
    self.loweringNextArm = datetime.now()
    self.loweringNextServo = datetime.now()
    self.shootingTotal = datetime.now()
    self.shootingServoDown = datetime.now()
    self.shootingArmUp = datetime.now()
    self.shooting = False
    self.shooter_service = shooter_service

  def iterate(self):
    self.main_motor.Set(0)

    if self.stick.GetRawButton(11):
      self.lowering = True
      self.main_motor.Set(-0.5)

    if self.stick.GetRawButton(5):
      self.servo_enabled = True
    elif self.stick.GetRawButton(6):
      self.servo_enabled = False

    if self.stick.GetRawButton(2):
      self.main_motor.Set(self.stick.GetY())

    if self.stick.GetTrigger():
      self.main_motor.Set(1)

    if self.stick.GetRawButton(11):
      self.shooter_service.lower()

    if self.stick.GetRawButton(12):
      self.shooter_service.shoot()

    if self.servo_enabled:
      self.servo.Set(LOWERING_SERVO_TOP_VALUE)
    else:
      self.servo.Set(LOWERING_SERVO_BOTTOM_VALUE)

    self.counter += 1

    #Stuff to control main motor
