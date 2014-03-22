import states

class Autonomous():
  def __init__(self, shooter_service, arm_motor, front_left, front_right,
          back_left, back_right):
    self.states = [
      #states.LowerFeeder(arm_motor),
      #states.Stop(),
      #states.RetractThrower(shooter_service),
      states.Stop(),
      states.MoveForward(front_left, front_right, back_left, back_right),
      #states.Stop(),
      #states.Throw(shooter_service),
      #states.Stop(),
      #states.RetractThrower(shooter_service),
      #states.Stop(),
      #states.MoveForward(front_left, front_right, back_left, back_right),
    ]
    self.state = 0

  def iterate(self):
    if self.state >= len(self.states):
      return

    self.states[self.state].iterate()

    if self.states[self.state].transition():
      self.states[self.state].end()
      self.state += 1

  def reset(self):
    self.state = 0
