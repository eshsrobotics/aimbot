from datetime import datetime, timedelta
import time, threading

LOWERING_SERVO_TOP_VALUE = 0.4 #needs to be actually found
LOWERING_SERVO_BOTTOM_VALUE = 0.1 #needs to be actually found

LOWERING_TOTAL_PERIOD = timedelta(seconds=1.6)
LOWERING_PERIOD = timedelta(seconds=0.5)
LOWERING_SERVO_PERIOD = timedelta(seconds=1)

SHOOTING_TOTAL_PERIOD = timedelta(seconds=0.8)
SHOOTING_SERVO_DOWN_PERIOD = timedelta(seconds=0.4)
SHOOTING_ARM_UP_PERIOD = timedelta(seconds=0.2)

class Shooter():
  def __init__(self,main_motor,encoder,servo,stick):
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
      self.loweringNextArm = datetime.now() + LOWERING_PERIOD
      self.loweringNextTotal = datetime.now() + LOWERING_TOTAL_PERIOD

    if self.loweringNextTotal > datetime.now():
      self.main_motor.Set(-0.5)

      if self.loweringNextArm < datetime.now() and self.loweringNextServo < datetime.now():
        self.loweringNextServo = datetime.now() + LOWERING_SERVO_PERIOD

    if self.loweringNextServo > datetime.now():
      self.servo_enabled = True

    if self.stick.GetRawButton(12):
      print("enabling shooting")
      self.shootingServoDown = datetime.now() + SHOOTING_SERVO_DOWN_PERIOD
      self.shootingTotal = datetime.now() + SHOOTING_TOTAL_PERIOD

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

    self.counter += 1

    #Stuff to control main motor
  
  def shootingArmDown(self):
    self.main_motor.Set(-0.5)
    threading.Timer(0.5, self.shootingServoDown)

  def shootingServoDown(self):
    self.main_motor.Set(-0.5)
    self.servo_enabled = False
    threading.Timer(1, self.shootingArmUp)

  def shootingArmUp(self):
    self.main_motor.Set(1)
    threading.Timer(1, self.shootingReset)

  def shootingReset(self):
    self.main_motor.Set(0)
