#!/usr/bin/env python
"""
random dots kinematogram
"""

from random import randint, sample
from expyriment import design, control, stimuli, misc
import expyriment.stimuli.extras

from expyriment.stimuli.extras import RandomDotKinematogram

exp = design.Experiment(name="Experiment")
control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment

control.initialize(exp)

p = 0.8
direction = 90  # in degrees (0=up)
ndots  = 100
DURATION = 5000

k = RandomDotKinematogram(200, ndots, direction, p, dot_lifetime=DURATION)

control.start()

while True:
    key, rt = k.present_and_wait_keyboard(duration=DURATION)
    exp.data.add([key, rt])
    exp.screen.clear()
    exp.screen.update()
    
    exp.clock.wait(2000)
    k.reset(ndots, direction, p)

control.end()

