# Sound manipulation

Open Praat (<https://www.fon.hum.uva.nl/praat/>).

1. Select and Run `New/Create Sound as Pure Tone`, then View/Edit 
2. Select and Run `New/Create Sound from Formula`


3. Create a 200ms long white noise (Formula=`randomUniform(-.8, .8)`) and save it as `noise.wav`
4. Create a pure tone with freq 440 and amplitude 0.05, and save it as `signal.wav` 
5. add signal and noise sound and save the result as `noise_signal.wav`

------

# Signal detection experiment

At each trial, either `noise.wav` or `noise_signal.wav` is played

The participant must press one of to keys (forced choice) indicating whether he hear the ignal of note. 

- Compute Hit Rate (hr) and False Alarms rate (fa) 

- Computer d' and beta fro signal detection theory (see <https://www.pallier.org/pdfs/aprime.pdf>)

---

# Segmenting and extracting audio stimuli with Praat


Follow the tutorial at
<https://kvonholzen.github.io/Tutorials_Audio_Praat_segmentation.html>


