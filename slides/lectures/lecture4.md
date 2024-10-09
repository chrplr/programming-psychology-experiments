# Illusory line motion

Program the stimulus shown at <https://www.youtube.com/watch?v=hA2Ag1LGJ80>

See Jancke, Dirk, Frédéric Chavane, Shmuel Naaman, and Amiram Grinvald. 2004. “Imaging Cortical Correlates of Illusion in Early Visual Cortex.” Nature 428 (6981): 423–26. https://doi.org/10.1038/nature02396.

---
# Double buffering 

![](double_buffering40.png)


Remark: we usually  pass the option `pygame.DOUBLEBUF` to `pygame.display.set_mode()`

Programming an animation will follow the following temporal logic::

    #draw picture1 in the backbuffer
    #flip the backbuffer to front buffer, which will be displayed to screen

    #draw picture2 in the backbuffer 
    #wait for some time
    #flip the backbuffer to front buffer

    #draw picture3 in the backbuffer
    #wait for some time
    #flip the backbuffer to front buffer


---
# vertical synchro

To avoid tearing, the swap between the backbuffer and frontbuffer mut be synchronized with the vertical refresh of the screen, to avoid seeing and overlap between the two buffers on the screen. This is called **V-sync** and should be enable in your video driver properties to prevent tearing.



Run <https://github.com/chrplr/programming-psychology-experiments/blob/main/experiments/timing_checks/xpy_tearing_test.py>

If the line is broken, the video card and the screen are not synchronized.


If you have vertical enable, `pygame.display.flip()` will ait untile the next refresh to return. 

Run <https://github.com/chrplr/programming-psychology-experiments/blob/main/experiments/timing_checks/rotating_disk/rotating_disk_pygame.py>

On the terminal, the time elapsed between to frame is printed.

---
# Reaction times

Goto to chapter **Reaction times** of <https://programming-psychology-experiments.rtfd.io/>


1. run `simple-detection-visual-pygame.py` and check your results saved in the file `reaction_times.csv` 

2. look at the code. Can you understand it?

3. Try to modify it to display the target cross at one of two random locations, left or the right of the center of the screen.

---
# same using expyriment

Got to `xpy_simple_reaction_times`

1. run `python simple-detection-visual-pygame.py` 

2. Look at the code.

Do the exercices in the document  (until parity decision)

---
# A remark on response devices

The keyboard or the mouse are not very precise to measure reaction times.

See <https://github.com/chrplr/arduino_leonardo_reponse_key> for a simple solution.
