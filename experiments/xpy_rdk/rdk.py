#! /usr/bin/env python
# Time-stamp: <2021-04-05 19:00:05 christophe@pallier.org>

import glob
import expyriment
import expyriment.stimuli.extras
from expyriment.stimuli.extras import RandomDotKinematogram


INSTRUCTIONS1 = """ You will see short videos of clouds of moving random dots. 

A subset of this dot coherently move either to the left or to the right.

You task is do indicate, after each video, which direction of motion you perceive.

Press the left arrow for 'LEFT', the right arrow for 'RIGHT'.

Press the space bar to start... """

exp = expyriment.design.Experiment(name="Random Dot Motion")
expyriment.control.initialize(exp)
kb = expyriment.io.Keyboard()

block.shuffle_trials()

bs = expyriment.stimuli.BlankScreen(colour=(0, 0, 0))
fs = expyriment.stimuli.FixCross(size=(25, 25), line_width=3, colour=(127, 127, 127))

trials = [(50, 0, 10), (50, 180, 10)]


# present instructions

instructions1 = expyriment.stimuli.TextScreen("Instructions",
                                              heading_size=60,
                                              text=INSTRUCTIONS1
                                              ).present()
kb.wait_char(' ')


expyriment.control.start()

for ndots, direction, ratio in trials:
    bs.present()  # clear screen
    exp.clock.wait(1000)
    fs.present(update=True)
    stim = RandomDotKinematogram(100, ndots, direction, ratio)
    stim.present_and_wait_keyboard()

expyriment.control.end()
