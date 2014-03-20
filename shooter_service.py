from datetime import datetime, timedelta

LOWERING_TOTAL_PERIOD = timedelta(seconds=1.6)
LOWERING_PERIOD = timedelta(seconds=0.5)
LOWERING_SERVO_PERIOD = timedelta(seconds=1)

SHOOTING_TOTAL_PERIOD = timedelta(seconds=0.8)
SHOOTING_SERVO_DOWN_PERIOD = timedelta(seconds=0.4)
SHOOTING_ARM_UP_PERIOD = timedelta(seconds=0.2)

class ShooterService():
  def __init__(self,main_motor,servo,stick):
    self.loweringNextTotal = datetime.now()
    self.loweringNextArm = datetime.now()
    self.loweringNextServo = datetime.now()
    self.shootingTotal = datetime.now()
    self.shootingServoDown = datetime.now()
    self.shootingArmUp = datetime.now()
    self.servo_enabled = False

  def iterate(self):
    if self.loweringNextTotal > datetime.now():
      self.main_motor.Set(-0.5)

      if self.loweringNextArm < datetime.now() and self.loweringNextServo < datetime.now():
        self.loweringNextServo = datetime.now() + LOWERING_SERVO_PERIOD

    if self.loweringNextServo > datetime.now():
      self.servo_enabled = True

    if self.shootingTotal > datetime.now():
      print("shooting iteration")

      if self.shootingServoDown < datetime.now() and self.shootingArmUp < datetime.now():
        print("enabling arm up")
        self.shootingArmUp = datetime.now() + SHOOTING_ARM_UP_PERIOD

    if self.shootingServoDown > datetime.now():
      print("servo down")
      self.main_motor.Set(-0.5)
      self.servo_enabled = False

    if self.shootingArmUp > datetime.now():
      print("shooting arm up")
      self.main_motor.Set(1)

    if self.servo_enabled:
      self.servo.Set(LOWERING_SERVO_TOP_VALUE)
    else:
      self.servo.Set(LOWERING_SERVO_BOTTOM_VALUE)

  def lower(self):
    self.loweringNextArm = datetime.now() + LOWERING_PERIOD
    self.loweringNextTotal = datetime.now() + LOWERING_TOTAL_PERIOD

  def shoot(self):
    self.shootingServoDown = datetime.now() + SHOOTING_SERVO_DOWN_PERIOD
    self.shootingTotal = datetime.now() + SHOOTING_TOTAL_PERIOD
