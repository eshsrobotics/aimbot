import math

try:
  import wpilib
except ImportError:
  from pyfrc import wpilib

stick = wpilib.Joystick(1)

frontRightMotor = wpilib.Jaguar(1)
frontLeftMotor = wpilib.Jaguar(2)
backLeftMotor = wpilib.Jaguar(3)
backRightMotor = wpilib.Jaguar(4)

class MyRobot(wpilib.SimpleRobot):

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

      forward = -stick.GetY()
      right = stick.GetX()
      clockwise = stick.GetZ()

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

      frontRightMotor.Set(front_right)
      frontLeftMotor.Set(front_left)
      backLeftMotor.Set(back_left)
      backRightMotor.Set(back_right)


def run():
  robot = MyRobot()
  robot.StartCompetition()
  
  return robot

if __name__ == '__main__':
  wpilib.run()
