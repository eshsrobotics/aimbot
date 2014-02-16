from mecanum_drive import MecanumDrive
#from intake import Intake

try:
  import wpilib
except ImportError:
  from pyfrc import wpilib

class Aimbot(wpilib.SimpleRobot):

  def __init__(self):
    super().__init__()

    self.drive_stick = wpilib.Joystick(1)
    #self.arm_stick = wpilib.Joystick(2)

    self.front_right_motor = wpilib.Jaguar(2)
    self.front_left_motor = wpilib.Jaguar(1)
    self.back_left_motor = wpilib.Jaguar(3)
    self.back_right_motor = wpilib.Jaguar(4)
    #self.intake_wheels_motor = wpilib.Jaguar(5)
    #self.intake_arm_motor = wpilib.Jaguar(6)

    self.mecanum_drive = MecanumDrive(
        self.front_right_motor,
        self.front_left_motor,
        self.back_right_motor,
        self.back_left_motor,
        self.drive_stick
      )

    #self.intake = Intake(self.intake_wheels_motor,self.intake_wheels_motor,self.arm_stick)

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
      #self.intake.iterate();

      wpilib.Wait(0.04)


def run():
  robot = Aimbot()
  robot.StartCompetition()
  
  return robot

if __name__ == '__main__':
  wpilib.run()
