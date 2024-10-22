#!/usr/bin/env python
# Time-stamp: <2024-10-20 18:44:35 christophe@pallier.org>
"""
Perception of motion with random dots kinematogram

"""

from random import shuffle
import itertools
from expyriment import design, control, stimuli, misc
from expyriment.stimuli.extras import RandomDotKinematogram


DESIGN = { "probability": [.10, .20, .30, .40, .50],
           "direction": [90, -90]}
N_REPETITIONS = 5
RADIUS = 200
N_DOTS  = 300
MAX_DURATION = 5000
RESP_KEYS = [misc.constants.K_LEFT, misc.constants.K_RIGHT]


INSTRUCTIONS =  """You will see a cloud of moving dots.
If you perceive that a subset of dots is moving towards the RIGHT, press the -> arrow key.
If you perceive that a subset of dots is moving towards the LEFT, press the <- arrow key.

You can quit at any time by pressing 'Esc'.

Press the space bar to start.
"""

#########################################################################################
exp = design.Experiment(name="Motion Perception")
control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment
control.defaults.window_size = 1000, 1000
control.initialize(exp)


b = design.Block()
b.add_trials_full_factorial(DESIGN, copies=N_REPETITIONS)
b.shuffle_trials()
exp.add_block(b)

cross = stimuli.FixCross()

#########################################################################################
control.start()

exp.data.add_variable_names(['direction', 'prob', 'rt', 'key'])

stimuli.TextScreen("Instructions", INSTRUCTIONS).present()
exp.keyboard.wait()

for b in exp.blocks:
    for t in b.trials:
        p = t.get_factor("probability")
        d = t.get_factor("direction")
        stim = RandomDotKinematogram(RADIUS,
                                     N_DOTS,
                                     d,
                                     p,
                                     dot_radius=2,
                                     dot_lifetime=MAX_DURATION)
        cross.present()
        exp.clock.wait(500)
        key, rt = stim.present_and_wait_keyboard(check_keys = RESP_KEYS,
                                                 duration=MAX_DURATION)
    
        exp.data.add([d, p, rt, key])
        exp.screen.clear()
        exp.screen.update()
        exp.clock.wait(2000)

control.end()

