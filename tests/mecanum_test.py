def test_mecanum_y(robot, wpilib):

  class TestController(object):

    loop_count = 0
    stick_prev = 0

    def IsOperatorControl(self, tm):

      self.loop_count += 1

      expected = -self.stick_prev

      assert robot.frontRightMotor.value == expected
      assert robot.frontLeftMotor.value == expected
      assert robot.backLeftMotor.value == expected
      assert robot.backRightMotor.value == expected

      robot.stick.y = (tm % 2.0) - 1.0
      self.stick_prev = robot.stick.y

      return not self.loop_count == 1000

  wpilib.internal.set_test_controller(TestController)
  wpilib.internal.enabled = True

  robot.OperatorControl()

def test_mecanum_x(robot, wpilib):

  class TestController(object):

    loop_count = 0
    stick_prev = 0

    def IsOperatorControl(self, tm):

      self.loop_count += 1

      assert robot.frontRightMotor.value == -self.stick_prev
      assert robot.frontLeftMotor.value == self.stick_prev
      assert robot.backLeftMotor.value == -self.stick_prev
      assert robot.backRightMotor.value == self.stick_prev

      robot.stick.x = (tm % 2.0) - 1.0
      self.stick_prev = robot.stick.x

      return not self.loop_count == 1000

  wpilib.internal.set_test_controller(TestController)
  wpilib.internal.enabled = True

  robot.OperatorControl()

def test_mecanum_z(robot, wpilib):

  class TestController(object):

    loop_count = 0
    stick_prev = 0

    def IsOperatorControl(self, tm):

      self.loop_count += 1

      expected = self.stick_prev * 0.5

      assert robot.frontRightMotor.value == -expected
      assert robot.frontLeftMotor.value == expected
      assert robot.backLeftMotor.value == expected
      assert robot.backRightMotor.value == -expected

      robot.stick.z = (tm % 2.0) - 1.0
      self.stick_prev = robot.stick.z

      return not self.loop_count == 1000

  wpilib.internal.set_test_controller(TestController)
  wpilib.internal.enabled = True

  robot.OperatorControl()