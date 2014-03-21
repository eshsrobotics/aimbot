def test_autonomous(robot, wpilib):
  wpilib.internal.enabled = True
  wpilib.internal.on_IsAutonomous = lambda tm: tm < 100000
  robot.Autonomous()

def test_disabled(robot):
  robot.Disabled()
