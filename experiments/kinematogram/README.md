Note:

To install the `DotCLoud` and `RandomDotKinematogram` classes, you must install "expyriment stimuli extras", by running:

    expyriment -D
	
and choosing the "master" branch

if you encounter an error:

	.expyriment/extras/expyriment_stimuli_extras/randomdotkinematogram/_randomdotkinematogram.py", line 251, in present_and_wait_keyboard
	from ... import _internals
	ImportError: attempted relative import beyond top-level package
	
Then replace `from ...` by `from expyriment` on line 251 of `_randomdotkinematogram.py`
