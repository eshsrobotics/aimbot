states = {
  lower_feeder: LowerFeederState,
  retract_thrower: RetractThrowerState
}

current_state = :lower_feeder

def iterate do
  states[current_state].iterate()

  if states[current_state].transition?
    current_state++
end
