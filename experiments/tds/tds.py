#!/usr/bin/env python
"""
signal detection theory experiment

See <https://docs.expyriment.org/Tutorial.html>

"""

from random import shuffle
from expyriment import design, control, stimuli

exp = design.Experiment(name="Experiment")
control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment

control.initialize(exp)

noise = stimuli.Audio("noise.wav")
signal = stimuli.Audio("signal.wav")

trials = [("noise", noise), ("signal", signal) ] * 20
shuffle(trials)

control.start()

exp.data.add_variable_names(['condition','response'])

exp.screen.clear()
exp.screen.update()

for c, s in trials:
    s.present()
    resp, _ = exp.keyboard.wait_char(["f", "j"])
    exp.data.add([c, resp])

control.end()

