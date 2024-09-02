# Software installation

First, you should determine your computer's Operating System (Windows, MacOSX, Ubuntu Linux, ...) and its version, as well as the processor type (intel/amd or arm). This information can be found in the "about" or "properties" tab of the system parameters section. 

Note: you should be connected to the Internet and have about 3~4 GB of free space on your disk to install all the software.

## Visual Studio Code

Unless you already have a code editor that you are happy with, download and install [VS Code](https://code.visualstudio.com/).


## Praat sound editor

See <https://www.fon.hum.uva.nl/praat/>


## Git

Follow the instructions at 
<https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>




## Python and libraries

1. Unless Python (version >= 3.8) is already installed on your computer, download and install it from <http://www.python/org>

2. Make sure you can start Python from a command line (in a Terminal).

   * Linux or Mac:

   Open a terminal (MacOS: type `terminal` in the Spotlight search field; Linux: pressing `Ctrl-Alt-T` ), and type `python` then press 'Enter'.

   This should display something like:

```{console}
Python 3.12.0 (main, Dec  7 2023, 17:39:28) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

   Type `quit()` and press `Enter` to exit python interpreter.


   * Windows

   After installing Python, make sure to add its location to the PATH environemetn variable: see <https://phoenixnap.com/kb/add-python-to-path> or <ttps://www3.ntu.edu.sg/home/ehchua/programming/howto/Environment_Variables.html>.
  
   Open a Terminal (start `Git Bash`) and type `python` on the command line.

   This should display something like:

```{console}
Python 3.12.0 (main, Dec  7 2023, 17:39:28) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

   Type `quit()` and press `Enter` to exit python interpreter.

3. Open a terminal (launch `git bash` in Windows) and type:

```{console}
pip install ipython matplotlib numpy pandas 
```

Then, to install the latest developemtn version of [expyriment](http://www.experiment.org):

```{console}
python -m pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --pre expyriment
```


