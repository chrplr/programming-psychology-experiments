#!/usr/bin/env python
"""
Single dot random walk
"""

from random import randint
from expyriment import design, control, stimuli, misc

N = 100
RADIUS = 3
SPEED = 8
XMAX, YMAX = 300, 300
P_COHERENT = .5
PROB_CHANGE_DIR = .05

exp = design.Experiment(name="Experiment")
control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment

control.initialize(exp)

start_positions = [(randint(-XMAX, XMAX),randint(-YMAX, YMAX)) for _ in range(N)]
dots = [stimuli.Circle(RADIUS, misc.constants.C_WHITE, 0, pos)  for pos in start_positions]
speeds = [[randint(-SPEED, SPEED),randint(-SPEED, SPEED)] for p in start_positions]

control.start()

while True:
    exp.screen.clear()

    for d in dots:
        d.present(clear=False, update=False)
    exp.screen.update()
    
    exp.data.add(exp.clock.time)

    # move and change speed
    for i, (d, s)  in enumerate(zip(dots, speeds)):
        if 100 * (i/N) < P_COHERENT:
            s = speeds[0]

        d.move(s)

        # bouncing
        x, y =  d.position
        if abs(x) > XMAX:
            speeds[i][0] = -speeds[i][0]
        if abs(y) > YMAX:
            speeds[i][1] = -speeds[i][1]

        # random speed change    
        if randint(0, 100) < PROB_CHANGE_DIR * 100:
            speeds[i] = [randint(-SPEED, SPEED), randint(-SPEED, SPEED)]

    exp.keyboard.process_control_keys()  # stop if 'ESC' is pressed

control.end()

