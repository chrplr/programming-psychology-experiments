# Software installation

:::{note}
* First, you should determine your computer's Operating System (Windows, MacOSX, Ubuntu Linux, ...) and its version, as well as the processor type (intel/amd or arm). This information can be found in the "about" or "properties" tab of the system parameters section. 

* You should be connected to the Internet and have about 3~4 GB of free space on your disk to install all the software.

:::


## Visual Studio Code

Download and install the code editor *Visual Studio Code* from <https://code.visualstudio.com/download> (*unless you already have a code editor that you are happy with*, e.g. sublime text, notepad++, spyder, pycharm, ...)

You can accept all default options proposed during the installation.

## R and Rstudio


*R* is a programming language specialized for statistical data analyses; Download and install it from <https://cran.rstudio.com/> (accepting all the default options proposed by the installer)

*Rstudio* is an *Integrated Developpement Environment* for R which greatly
simplifies the use of RMarkdown. You can download and install the
free version of RStudio Desktop from <https://posit.co/download/rstudio-desktop/>  (accepting all the default options)


## Praat speech editor

Download the speech editor *Praat* from <https://www.fon.hum.uva.nl/praat/>. 

If you are a Windows user, you must extract the program (`praat.exe`) from the zip file. When you click on its icon to launch Praat, Windows Defender may warn you that it is threat. Do not worry and run it anayway. 


## Git

Install the version control software *Git*, following the instructions at 
<https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>

Under Windows, you will download the Git for Windows installer from <https://git-scm.com/download/win>

:::{note} Windows only.
   **IMPORTANT**: During the installation:
   
   - In "Choosing the default Editor used by Git", select `Use Notepad`
   - In "Adjusting your PATH environment", select `Use Git and optional Unix tools...`
   - In "Configuring the Terminal emulator", select `Use MinTTY`   
 
     You can keep the defaults for all other options.

:::

### git local configuration

After the installation, start `Git bash` if you are under Windows or open a terminal if you are under MacOSX or Linux (MacOS: type `terminal` in the Spotlight search field; Linux: press `Ctrl-Alt-T` ), and type the following lines, after replacing `firstname`, `lastname` and `your_email` by your personal information:



    git config --global user.name "firstname lastnames" 
    git config --global user.email "your_email" 
    git config --global core.editor nano




You can now close the terminal by typing the command `exit` or, faster, by pressing `Ctrl-D`, or by just closing its window.


## Python

1. Unless Python3, version >= 3.8, is already installed on your computer, download and install it from <http://www.python.org>. 

Important. Make sure to select 'Add python.exe to PATH' when running the installer under Windows.

2. Check that you can start Python from a command line.

    * Windows:
	
	    Start `Git Bash`. This should open a terminal with a blinking cursor, type the following command line: 
	   
	   ```
	   echo "alias python='winpty python.exe'" >> ~/.bash_profile
	   ```
	   
	   and press `Enter` to execute the command.
	   
	   Close Git Bash, and reopen it again (this runs the `.bash_profile` script).

	
	   Type `python` on the command line, then press `enter`.

       If you computer displays
      ```
      python: command not found
	  ```
	  
       then you must add the location (folder) of `python.exe` to the `PATH` environment variable. Instructions to do this are provided at <https://realpython.com/add-python-to-path/>
  

       Otherwise, you should see a display like:

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



## Basic python libraries


Open a terminal (`Git bash` in Windows), and type:

```
pip install ipython jupyter numpy matplotlib pandas seaborn
```

## Pygame

[Pygame](http://www.pygame.org) is a python module to program simple video games 
In a Terminal, type:
```
pip install pygame
```


## Expyriment

[Expyriment](http://www.experiment.org) is a Python module to program psychology experiments


To install the latest development version, type:

```
python -m pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --pre expyriment
```

Then,  run:

```
expyriment -D
```

And type `master` when given a choice to select a branch. 

:::{note} (only for advanced python users): you might want to create a virtual environment for expyriment (with conda, pyenv, uv...)
:::
