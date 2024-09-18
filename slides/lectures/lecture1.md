# Experimental Approaches (CORE-101)

   - learn to build experimental psychology experiments:  how to create visual and auditory stimuli, to present them at precise times record participants' responses and analyse them.
   - learn tools to do reproducible science (github, markdown, ...)
   - improve  your programming skills (clean code, ...)

   Format: Practical tutorials. 
   
   *Prerequisites*: moderate knowledge of programming

---

# The programming language choice

![](images/python-logo.png)

**Python** is a good compromise.

1. It is general purpose
2. It is quite readable
3. It is popular and there is a lot of help on the web
4. Free
   
Note: We will use Python 3 (>3.8)

**Javascript** for online (web) experiments

---


# Menu of the day

* How to use Python from the command line: how to work with a text editor and the command line to create/run python scripts.

* Draw static figures using the [pygame](http://www.pygame.org) library



# Basic skills to work with Python

## Basic command line skills

- Open a Terminal (see <https://pcbs.readthedocs.io/en/latest/first-things-first.html#learn-how-to-open-a-terminal>


- use the commands `cd`, `ls`, `pwd`, `mkdir` to navigate the directory structure. 

---

# interactive Python

type `ipython` then press `Enter`

```
2 ** 5
2 ** 64
```

```
import turtle
turtle.circle(50)
turtle.forward(100)
turtle.circle(50)

turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.heading()
```

```
import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0, 30, num=3001)
plt.plot(t, np.sin(t))
```

---

## Running a Python script downloaded from the Internet

- Download python scripts from internet, e.g. <https://github.com/chrplr/PCBS/raw/master/games.zip> (unzip it)


        $ cd Downloads  # or whatever folder where you downloaded games.zip
        $ cd games
        $ ls
        computer-guess-a-number.py  hammurabi.py  human-guess-a-number.py  koch.py  matches.py
        $ python koch.py
        $ python matches.py


---


# Create python script with  a code editor


E.g. Visual Studio Code (but could be any text editor or python IDE)

Open Visual Studio Code from your start menu, o from the command line:

```
$ code hello.py
```

Enter the line 

```
print("Hello PCBS")
```

Save the file, and run

```
$ python hello.py
```


See <https://pcbs.readthedocs.io/en/latest/running-python.html>


---

# Visual stimulus creation

https://programming-psychology-experiments.readthedocs.io/en/latest/stimulus-creation.html
