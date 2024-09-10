# Software installation

:::{note}
* First, you should determine your computer's Operating System (Windows, MacOSX, Ubuntu Linux, ...) and its version, as well as the processor type (intel/amd or arm). This information can be found in the "about" or "properties" tab of the system parameters section. 

* You should be connected to the Internet and have about 3~4 GB of free space on your disk to install all the software.

:::


## Visual Studio Code

Download and install the code editor *Visual Studio Code* from <https://code.visualstudio.com/download> (*unless you already have a code editor that you are happy with*, e.g. sublime text, notepad++, spyder, pycharm, ...)



## R and Rstudio


*R* is a programming language specialized for statistical data analyses; Download and install it from <https://cran.rstudio.com/> (accepting all the default options proposed by the installer)

*Rstudio* is an *Integrated Developpement Environment* for R which greatly
simplifies the use of RMarkdown. You can download and install the
free version of RStudio Desktop from <https://posit.co/download/rstudio-desktop/>  (accepting all the default options)


## Praat speech editor

Download and install the speech editor *Praat* from <https://www.fon.hum.uva.nl/praat/>


## Git

Install the version control software *Git*, following the instructions at 
<https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>


:::{note} Windows only.
   **IMPORTANT**: When proposed to adjust the PATH environment variable,  tick the box "Use Git and optional unix tools from the command line prompt". (You can accept all the other defaults).
:::

### configuration

After the installation, start `Git bash` if you are under Windows or open a terminal if you are under MacOSX or Linux (MacOS: type `terminal` in the Spotlight search field; Linux: press `Ctrl-Alt-T` ), and type the following lines, after replacing `firstname`, `lastname` and `your_email` by your personal information:



    git config --global user.name "firstname lastnames" 
    git config --global user.email "your_email" 
    git config --global core.editor nano


You can now close the terminal by typing the command `exit` or, faster, by pressing `Ctrl-D`, or by just closing its window.


## Python

1. Unless Python3, version >= 3.8, is already installed on your computer, download and install it from <http://www.python.org>

2. Make sure you can start Python from a command line.

    * Windows:

       After installing Python, make sure to add the location (folder) of `python.exe` to the `PATH` environement variable, following the instructions at <https://realpython.com/add-python-to-path/>
  
       Then, start `Git Bash`. This should open a terminal with a blinking cursor. Type `python` then press `enter`. This should display something like:

      ```
      Python 3.12.0 (main, Dec  7 2023, 17:39:28) [GCC 11.4.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.
      >>> 
      ```

      Type `quit()` and press `Enter` to exit python interpreter.



   * Mac or Linux:

      Open a terminal (MacOS: type `terminal` in the Spotlight search field; Linux: pressing `Ctrl-Alt-T` ), and type `python` then press 'Enter'.

      This should display something like:

      ```
      Python 3.12.0 (main, Dec  7 2023, 17:39:28) [GCC 11.4.0] on linux
      Type "help", "copyright", "credits" or "license" for more information.
      >>> 
      ```

    Type `quit()` and press `Enter` to exit python interpreter.

    If you computer displayed
      ```
      python: command not found
	  ```
    then ask for help to the professors.


## Basic python libraries


Open a terminal (`Git bash` in Windows), and type:

```
pip install ipython jupyter numpy matplotlib pandas 
```

## Pygame

[Pygame](http://www.pygame.org) is a python module to program simple video games 
In terminal, type:
```
pip install pygame
```


## Expyriment

[Expyriment](http://www.experiment.org) is a Python module to program psychology experiments


To install the latest development version, type:

```
python -m pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --pre expyriment
```


:::{note} (only for advanced python users): you might want to create a virtual environment for expyriment (with conda, pyenv, ...)
:::
