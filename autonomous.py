import states

class States:
  LowerFeeder, RetractThrower, MoveForward, Stop, Throw, ThrowCleanup = range(6)

class Autonomous():
  def __init__(self, shooter_service, arm_motor, front_left, front_right,
          back_left, back_right):
    self.states = [
      states.LowerFeeder(arm_motor),
      states.RetractThrower(shooter_service),
      states.MoveForward(front_left, front_right, back_left, back_right),
      states.Stop(),
      states.Throw(shooter_service),
      states.RetractThrower(shooter_service),
    ]
    self.state = States.LowerFeeder

  def iterate(self):
    if self.state >= len(self.states):
      return

    self.states[self.state].iterate()

    if self.states[self.state].transition():
      self.states[self.state].end()
      self.state += 1

  def reset(self):
    self.state = States.LowerFeeder
