import math

try:
  import wpilib
except ImportError:
  from pyfrc import wpilib

SPEED_LIMIT = 1.5

stick = wpilib.Joystick(1)

class MyRobot(wpilib.SimpleRobot):
  
  def __init__(self):
    super().__init__()

    self.stick = wpilib.Joystick(1)
    
    self.frontRightMotor = wpilib.Jaguar(1)
    self.frontLeftMotor = wpilib.Jaguar(2)
    self.backLeftMotor = wpilib.Jaguar(3)
    self.backRightMotor = wpilib.Jaguar(4)

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

      forward = -self.stick.GetY() / SPEED_LIMIT
      right = self.stick.GetX() / SPEED_LIMIT
      clockwise = self.stick.GetZ() / SPEED_LIMIT

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

def run():
  robot = MyRobot()
  robot.StartCompetition()
  
  return robot

if __name__ == '__main__':
  wpilib.run()
