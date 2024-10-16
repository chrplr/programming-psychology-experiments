#!/usr/bin/env python
"""
dotloud
"""

from random import randint
from expyriment import design, control, stimuli, misc
import expyriment.stimuli.extras

from expyriment.stimuli.extras import DotCloud

exp = design.Experiment(name="Experiment")
control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment

control.initialize(exp)

c = DotCloud()
c.make(100, 2)

control.start()

while True:
    c.present()
    c.move((1, 1))
    exp.keyboard.process_control_keys()  # stop if 'ESC' is pressed

control.end()

