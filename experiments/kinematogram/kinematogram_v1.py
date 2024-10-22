#!/usr/bin/env python
"""
random dots kinematogram
"""

from random import randint, sample
from expyriment import design, control, stimuli, misc
import expyriment.stimuli.extras

from expyriment.stimuli.extras import RandomDotKinematogram

exp = design.Experiment(name="Experiment")
#control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment

control.initialize(exp)

p = 0.5
direction = 180
ndots  = 300
DURATION = 5000

k = RandomDotKinematogram(400, ndots, direction, p, dot_lifetime=DURATION)
k.make_frame()

control.start()

while True:
    key, rt = k.present_and_wait_keyboard(duration=DURATION)
    exp.data.add([key, rt])
    exp.screen.clear()
    exp.screen.update()
    
    exp.clock.wait(2000)
    k.reset(100, sample([0, 180], k=1)[0], p)

control.end()

