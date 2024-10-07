***************************
Creating and playing sounds
***************************

Install the `simpleaudio` module::

        pip install simpleaudio

Then run the quick check with ipython::

        import simpleaudio.functionchecks as fc 
        fc.LeftRightCheck.run() 

Check out `simpleaudio's tutorials <https://simpleaudio.readthedocs.io/en/latest/tutorial.html>`__

The module :download:`sound_synth.py <../stimuli/sound/sound_synth.py>` provides several functions to load, create, and play sounds. 

Exercise (\*\*) Using functions from the `sound_synth` module, write a script that loads the file ``cymbal.wav`` and plays it 10 times, at a rhythm of one per second. (Warning: a basic knowledge of numpy arrays is necessary to concatenate the samples).

Check a solution at :download:`cycle.py <../stimuli/sound/cycle.py>`


Shepard tone
------------

Watch `this video <https://www.youtube.com/watch?v=LVWTQcZbLgY
>`__ about *Shepard tones*.

Exercise (\*\*\*): Program a Shepard tone.


Sound localisation from binaural dephasing
------------------------------------------

Exercise (\*\*) Take the channel of a mono sound and create a stereo sound. Then dephase the two channels by various delays, and listen to the results.

Hints: load the sound file into a one dimensional numpy array, make a copy of the array and shift it, assemble the two arrays in a bidimensional array (matrix) and save it as a stereo file

If you know nothing about Numpy_, you may find useful tutorials on the web, e.g. at https://github.com/paris-saclay-cds/data-science-workshop-2019/blob/b370d46044719281932337ca4154e1b0b443ad97/Day_1_Scientific_Python/numpys/numpy_intro.ipynb


Pulsation (Povel & Essen, 1985)
-------------------------------

Exercise (\*\*\*) Create rhythmic stimuli such as the ones described in `Povel and Essen (1985) Perception of Temporal Patterns <http://www.cogsci.ucsd.edu/~creel/COGS160/COGS160_files/PovelEssens85.pdf>`__


