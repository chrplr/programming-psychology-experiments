#!/usr/bin/env python
"""
Single dot random walk
"""

from random import randint
from expyriment import design, control, stimuli, misc

RADIUS = 10
SPEED = 10

exp = design.Experiment(name="Experiment")
control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment

control.initialize(exp)

dot = stimuli.Circle(RADIUS, misc.constants.C_WHITE)

control.start()

while True:
    dot.present()
    dx, dy = randint(-SPEED, SPEED), randint(-SPEED, SPEED)
    dot.move((dx, dy))
    exp.keyboard.process_control_keys()  # stop if 'ESC' is pressed

control.end()

