# Setup

1) You need Python and Jupyter. The easiest way to have both of these things is to install anaconda.

2) Once you have anaconda installed, for the Louvain algorithm, you need the Louvain python package. You install packages with the conda package manager that comes with anaconda. However, there are two ways to handle this--the easy way and the right way. For purposes of this project, it probably doesn't matter which way you do it, but for purposes of learning the proper way to handle this kind of stuff if you end up pursuing a career in software engineering in Python, it makes sense to get in the habit of doing it the right way.

## the easy way

`conda install python-louvain`

This will install the package globally, and you're done.

## the right way

The right way means creating a new, isolated environment in which to install packages. This is best practice because different projects have different packages needed, and different packages as well as different versions of packages conflict with each other. So on any given project, you want to create a Python environment specifically for that project.

First you need to create a new Python environment to work in:

`conda create -n louvain anaconda`

This creates a new Python environment called "louvain" and installs the default packages that come with anaconda into that environment.

Now that the environment is created, you need to switch to that environment:

`conda activate louvain`

Now that you are within the louvain environment, go ahead and install the louvain package:

`conda install python-louvain`

## running it

Now that you have the package installed, you need to run a jupyter notebook. You do this by navigating to wherever you cloned the github repo to and running:

`jupyter notebook`

From there you can open the notebook and run the cells.

# Remarks

If you did opt to do it the right way, you must remember that you need to activate your project environment before running the jupyter notebook. Otherwise, when you try to call any of the functions within the louvain library, it will fail. Because as far as Python is concerned, that package isn't even installed.

So my typical workflow would be:

`conda activate louvain`

`cd /home/flynn/drive/school/reseach/similarity/`

`git pull` (more on this later)

`jupyter notebook`