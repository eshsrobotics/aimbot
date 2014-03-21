from datetime import datetime, timedelta

class LowerFeeder():

  def __init__(self, arm):
    self.OPERATION_TIME = timedelta(seconds=1)
    self.LOWER_TIME = timedelta(seconds=0.3)

    self.started = False
    self.arm = arm

  def iterate(self):
    if not self.started:
      print('started lower feeder state')
      self.started = True
      self.timestop = datetime.now() + self.OPERATION_TIME
      self.lower_timestop = datetime.now() + self.LOWER_TIME

    if datetime.now() > self.lower_timestop:
      self.arm.Set(-0.5)

  def end(self):
    self.started = False

  def transition(self):
    return datetime.now() > self.timestop

class RetractThrower():
  def __init__(self, shooter_service):
    self.shooter_service = shooter_service
    self.started = False

  def iterate(self):
    if not self.started:
      print('started retract thrower state')
      self.shooter_service.lower()
      self.started = True

    self.shooter_service.iterate()

  def end(self):
    self.started = False

  def transition(self):
    return not self.shooter_service.lowering

class MoveForward():

  def __init__(self, front_left, front_right, back_left, back_right):
    self.OPERATION_TIME = timedelta(seconds=1)
    self.SPEED = 1

    self.started = False
    self.front_left = front_left
    self.front_right = front_right
    self.back_left = back_left
    self.back_right = back_right

  def iterate(self):
    if not self.started:
      print('started move forward state')
      self.started = True
      self.timestop = datetime.now() + self.OPERATION_TIME

    self.front_right.Set(self.SPEED)
    self.front_left.Set(-self.SPEED)
    self.back_left.Set(-self.SPEED)
    self.back_right.Set(self.SPEED)

  def end(self):
    self.started = False
    self.front_right.Set(0)
    self.front_left.Set(0)
    self.back_left.Set(0)
    self.back_right.Set(0)

  def transition(self):
    return datetime.now() > self.timestop

class Stop():
  def __init__(self):
    self.OPERATION_TIME = timedelta(seconds=2)
    self.started = False

  def iterate(self):
    if not self.started:
      print('started stop state')
      self.started = True
      self.timestop = datetime.now() + self.OPERATION_TIME
      
  def end(self):
    self.started = False

  def transition(self):
    return datetime.now() > self.timestop

class Throw():
  def __init__(self, shooter_service):
    self.started = False
    self.shooter_service = shooter_service

  def iterate(self):
    if not self.started:
      print('started throw state')
      self.shooter_service.shoot()
      self.started = True

    self.shooter_service.iterate()
      
  def end(self):
    self.started = False

  def transition(self):
    return self.shooter_service.shooting
