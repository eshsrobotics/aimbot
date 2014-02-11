def test_autonomous(robot, wpilib):
  wpilib.internal.enabled = True
  robot.Autonomous()


def test_disabled(robot):
  robot.Disabled()