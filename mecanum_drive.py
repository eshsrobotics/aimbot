import math

class MecanumDrive():

  def __init__(self, front_right, front_left, back_right, back_left, stick):
    self.front_right = front_right
    self.front_left = front_left
    self.back_right = back_right
    self.back_left = back_left
    self.stick = stick

  def iterate(self):
    forward = -self.stick.GetY()
    right = self.stick.GetX()
    clockwise = self.stick.GetZ() * 0.5

    front_left_val = forward + clockwise + right
    front_right_val = forward - clockwise - right
    back_left_val = forward + clockwise - right
    back_right_val = forward - clockwise + right

    maxVal = math.fabs(front_left_val)
    if math.fabs(front_right_val) > maxVal:
      maxVal = math.fabs(front_right_val)
    if math.fabs(back_left_val) > maxVal:
      maxVal = math.fabs(back_left_val)
    if math.fabs(back_right_val) > maxVal:
      maxVal = math.fabs(back_right_val)

    if maxVal > 1:
      front_left_val /= maxVal
      front_right_val /= maxVal
      back_left_val /= maxVal
      back_right_val /= maxVal

    self.front_right.Set(front_right_val)
    self.front_left.Set(front_left_val)
    self.back_left.Set(back_left_val)
    self.back_right.Set(back_right_val)
