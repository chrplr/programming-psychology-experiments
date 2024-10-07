**********************
Dynamic visual stimuli
**********************

.. contents::


Animated movies are just a succession of still pictures. If the rate of presentation is fast enough, the brain creates an illusion of continuity. 

With pygame, we use the double buffering mode (set by the option ``DOUBLEBUF`` in the call to ``pygame.display.set_mode()``) to draw the next image in a backbuffer while the current one is in the front buffer (see fdigure below). It is only when we call ``pygame.display.flip()`` that the image in th backbuffer is sent to the front buffer, which will then be displayed at the next screen refresh.


   .. figure:: images/double_buffering40.png
      :alt: Double Buffering () 

      General cycle of a stimulus presentation on a computer monitor with double buffering. The graphics card (graphics processing unit = GPU) processes a new drawing command from the application. The images are then rendered by the GPU and stored in a double buffering process. (A) In a first step, the new image is rendered into an invisible back buffer. The old image is still stored in the front buffer and displayed on the monitor. (B) In a second step, the back and front buffers are swapped. (C) In a third step, the monitor reads out and displays the content of the front buffer while a new image can already be rendered to the backbuffer (Ref: Poth, Christian H., Rebecca M. Foerster, Christian Behler, Ulrich Schwanecke, Werner X. Schneider, and Mario Botsch. 2018. “Ultrahigh Temporal Resolution of Visual Presentation Using Gaming Monitors and G-Sync.” Behavior Research Methods 50 (1): 26–38. https://doi.org/10.3758/s13428-017-1003-6.)

To avoid tearing, the swap between the backbuffer and frontbuffer mut be synchronized with the vertical refresh of the screen, to avoid seeing and overlap between the two buffers on the screen. This is called **V-sync** and should be enable in your video driver properties to prevent tearing.
      
Programming an animation will follow the following temporal logic::

    #draw picture1 in the backbuffer
    #flip the backbuffer to front buffer, which will be displayed to screen

    #draw picture2 in the backbuffer 
    #wait for some time
    #flip the backbuffer to front buffer

    #draw picture3 in the backbuffer
    #wait for some time
    #flip the backbuffer to front buffer

    ...


      
Walker
------


Program an animation of a walker like the one displayed on https://lazyfoo.net/tutorials/SDL/14_animated_sprites_and_vsync/index.php


You will need to extract the sprites from the following picture: 

.. figure:: images/foo.png

	    
then display them in a loop. 

  For a solution, checkout :download:`animation/walker.py <../stimuli/animation/walker.py>`


Illusory line-motion
--------------------

Illusory line motion (ILM) refers to a situation in which flashing a light at one end of a bar prior to the bar's instantaneous presentation results in the percept of motion. 

.. figure:: images/ilm.jpg
   
   Illusory line-motion

Exercise (*):  Program the stimulus, that is, first draw a square, wait for a few milliseconds using the function `pygame.time.wait()`, then draw a rectangle overlapping with the initial square.   

  Check out :download:`visual-illusions/line-motion.py <../stimuli/visual-illusions/line-motion.py>`


Flash-lag illusion
------------------

* Download  :download:`visual-illusions/flash-lag.py <../stimuli/visual-illusions/flash-lag.py>` and run it. Do not look at the code yet. 

* Do you feel that the moving square's x position coincides with the flashing square or not? If you want to read about the `Flash-lag illusion <https://en.wikipedia.org/wiki/Flash_lag_illusion>`__.

Exercise:

1. Create a movie of a square moving horizontally, back and forth. The
   principle is simple: you just need to create a loop where you
   display a square at coordinates `x, y` ,wait a few milliseconds, then clear
   the screen, and increment or decrement the `x` coordinate by a fixed amount.
   This strategy is explained in details at http://programarcadegames.com/index.php?lang=en&chapter=introduction_to_animation

   Check out out version :download:`visual-illusions/moving_square.py <../stimuli/visual-illusions/moving_square.py>`

2. Add the presentation of a flashing square then the moving square passes the middle line, to generate the flash-lag illusion.

Now, you can look at the code in :download:`visual-illusions/flash-lag.py <../stimuli/visual-illusions/flash-lag.py>`


Dynamic version of the Ebbinghaus-Titchener
-------------------------------------------

-  Watch `this video <https://www.youtube.com/watch?v=hRlWqfd5pn8>`__.

-  Program a version where the outer circles (inducers) grow and shrink in size.

-  Check out :download:`visual-illusions/ebbinghaus-dynamic.py <../stimuli/visual-illusions/ebbinghaus-dynamic.py>`


Lilac Chaser
------------

The `Lilac Chaser`_ is a dynamic version of the Troxler fill-in illusion.  

.. _Lilac Chaser: https://en.wikipedia.org/wiki/Lilac_chaser

Exercise (\*\*): Program the Lilac Chaser stimulus, with 12 rose disks (you can use full disks without any blurring). Try different colors.

For a possible solution, check out :download:`visual-illusions/lilac_chaser.py <../stimuli/visual-illusions/lilac_chaser.py>`

(Optional exercise for advanced students: add blurring to the disks to make a stimulus similar to that of the wikipedia page `Lilac Chaser`_. Then, for a solution, check out :download:`visual-illusions/lilac_chaser_blurred.py <../stimuli/visual-illusions/lilac_chaser_blurred.py>`)


