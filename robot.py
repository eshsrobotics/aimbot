import math

try:
  import wpilib
except ImportError:
  from pyfrc import wpilib

class MyRobot(wpilib.SimpleRobot):

  def __init__(self):
    super().__init__()

    self.frontRightMotor = wpilib.Jaguar(1)
    self.frontLeftMotor = wpilib.Jaguar(2)
    self.backLeftMotor = wpilib.Jaguar(3)
    self.backRightMotor = wpilib.Jaguar(4)
    self.stick = wpilib.Joystick(1)

  def Autonomous(self):
  
    self.GetWatchdog().SetEnabled(False)
    while self.IsAutonomous() and self.IsEnabled():
      wpilib.Wait(0.01)

  def OperatorControl(self):
    
    dog = self.GetWatchdog()
    dog.SetEnabled(True)
    dog.SetExpiration(0.25)

    while self.IsOperatorControl() and self.IsEnabled():
      dog.Feed()

      forward = -self.stick.GetY()
      right = self.stick.GetX()
      clockwise = self.stick.GetZ() * 0.5

      front_left = forward + clockwise + right
      front_right = forward - clockwise - right
      back_left = forward + clockwise - right
      back_right = forward - clockwise + right

      maxVal = math.fabs(front_left)
      if math.fabs(front_right) > maxVal:
        maxVal = math.fabs(front_right)
      if math.fabs(back_left) > maxVal:
        maxVal = math.fabs(back_left)
      if math.fabs(back_right) > maxVal:
        maxVal = math.fabs(back_right)

      if maxVal > 1:
        front_left /= maxVal
        front_right /= maxVal
        back_left /= maxVal
        back_right /= maxVal

      self.frontRightMotor.Set(front_right)
      self.frontLeftMotor.Set(front_left)
      self.backLeftMotor.Set(back_left)
      self.backRightMotor.Set(back_right)

      wpilib.Wait(0.04)


def run():
  robot = MyRobot()
  robot.StartCompetition()
  
  return robot

if __name__ == '__main__':
  wpilib.run()
