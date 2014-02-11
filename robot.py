from mecanum_drive import MecanumDrive

try:
  import wpilib
except ImportError:
  from pyfrc import wpilib

class MyRobot(wpilib.SimpleRobot):

  def __init__(self):
    super().__init__()

    self.stick = wpilib.Joystick(1)

    self.frontRightMotor = wpilib.Jaguar(1)
    self.frontLeftMotor = wpilib.Jaguar(2)
    self.backLeftMotor = wpilib.Jaguar(3)
    self.backRightMotor = wpilib.Jaguar(4)

    self.mecanum_drive = MecanumDrive(self.frontRightMotor, self.frontLeftMotor, self.backRightMotor, self.backLeftMotor, self.stick)

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

      self.mecanum_drive.iterate()

      wpilib.Wait(0.04)


def run():
  robot = MyRobot()
  robot.StartCompetition()
  
  return robot

if __name__ == '__main__':
  wpilib.run()
