# NEUS 642: Python Programming in Experimental Neuroscience

<!-- vim-markdown-toc GFM -->

* [Time and location](#time-and-location)
* [Course staff](#course-staff)
* [Overview](#overview)
* [Preparing for the course](#preparing-for-the-course)
* [Assessment](#assessment)
	* [Grading](#grading)
	* [Developing an exercise](#developing-an-exercise)
* [Python](#python)
	* [Python server](#python-server)
	* [Installing Python](#installing-python)
	* [Code editors](#code-editors)
	* [Course-specific resources](#course-specific-resources)
	* [Other resources](#other-resources)

<!-- vim-markdown-toc -->

## Time and location
* Time: Tuesdays from 1 to 3pm during the winter 2020 semester (January 7 through March 17).
* Location: Vollum 4M.

## Course staff
### Course directors:
* *Brad Buran, Ph.D.*. Research instructor in the Oregon Hearing Research Center (buran@ohsu.edu).
* *Stephen David, Ph.D.*. Assistant professor in the Oregon Hearing Research Center (davids@ohsu.edu).

### Teaching assistants:
* Emily Leff (leff@ohsu.edu).
* Alexandria Lassetter (lassetta@ohsu.edu).
* Alexander Tomlinson (tomlinsa@ohsu.edu)

## Overview
NEUS 642 is a hands-on course on the basics of Python programming for analysis of neuroscience-related data. By the end of the course, students will have learned basic programming tasks, including loading and manipulating data sets, signal processing, image processing, and plotting. The course will be highly interactive. Students (with the support of TAs and instructors) will be expected to design and lead exercises during the class, and they are encouraged to bring their own data and/or analysis problem to the course. The course is open to students of all skill levels; however, a basic knowledge of programming is encouraged.

## Preparing for the course
Before we meet for the first time, please do the following:

* Sign up for our [NEUS642 Slack workspace](neus642.slack.com). If you haven't already received the invite, please contact one of the course staff for assistance.

* Find a laptop you can bring to class. Each class will have an interactive, hands-on exercise developed by you or one of your classmates. You'll be working on the exercise using your laptop.

* [Install Anaconda Python](#installing-python). If you have trouble with installing Anaconda Python before the first day of class, you can contact the course staff on Slack for assistance.

* If you're not already familiar with Python, please start learning Python 3. You can work through the [suggested online courses and/or read the eBook](#python).

* If you're already familiar with Python, but have only used Python 2, please familiarize yourself with the [differences between Python 2 and 3](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html). Support for Python 2 sunset on January 1, 2020.

* Work through the five days of the [Python NeuroBootcamp](https://github.com/dasaderi/python_neurobootcamp). You can [download](https://github.com/dasaderi/python_neurobootcamp/archive/master.zip) the notebooks to your computer and run them using Jupyter Notebook (which comes with Anaconda Python). If you have any trouble or questions, you can post them to the Slack channel. As a bonus, you may work through the notebooks from the [fall 2018 semester of NEUS642](https://github.com/bburan/NEUS642/notebooks/2018).

* Think about a dataset that you would like to work on for the class. At some point during the course, you will be asked to develop an exercise based on this dataset (either individually or in a small group of two or three). I may reach out to some of you in the weeks leading up to the course and ask you to prepare your exercise in advance so that we have exercises for the first few weeks of class.

## Assessment

### Grading
This is a pass/no pass course with two credits. Grading will be based on the following:

* Class attendance and participation in discussions
* Preparation of an exercise for at least one session

### Developing an exercise
All exercises will follow the format established in the [Python Neurobootcamp](https://github.com/dasaderi/python_neurobootcamp)(days 2 through 4) and [last year's course](https://github.com/bburan/NEUS642/notebooks/2018).

Material for this course will be made freely available as a learning resource for future scientists, both at OHSU and elsewhere. Therefore, we ask that all datasets and materials be licensed under a [Creative Commons](https://creativecommons.org) license and the [BSD license](https://opensource.org/licenses/BSD-3-Clause).

You'll be asked to develop a two-hour exercise based on a dataset you'd like to work with. This dataset can be from your own work or obtained from a lab. The exercise will be formatted as a Jupyter Notebook and uploaded to the [NEUS642 webpage](https://github.com/bburan/NEUS642) prior to the start of class. If you require additional third-party packages for running the exercise, please check with the course instructors so that instructions for installing the packages can be provided to students in advance.

All exercises must contain sufficient background to the problem that gives your classmates sufficient background to understand the problem. Your classmates are neuroscientists, but will need some additional, domain-specific knowledge to understand the problem. Do not skip this step, or you will lose your classmates!

First, identify a dataset you'd like to work with. If you need help identifying a dataset pertinent to your area of interest, please contact a TA or course instructor. The dataset should be of reasonable size (i.e., no 10 gigabyte confocal images). You may need to do some post-processing of the data to get the file down to a reasonable size.

Next, think of a reasonable problem that you can walk the class through in two hours. The exercise should load the data, perform some processing and/or summary of the data and then plot the results. 

Now, write the code to perform these steps and generate your plot. Once the code works, break it down into individual cells for a Jupyter Notebook. Above each code cell, add a Markdown cell explaining what's happening in the block below. Identify four or five cells that may serve as exercises. You'll remove the code from these cells and add some explanation above the blank cell instructing the class what problem needs to be solved before they can move onto the next step. They will then have 5-15 minutes (depending on the complexity of the problem) to try and figure out the code that solves the problem.

Throughout the entire process, you will be expected to consult with the TAs and course organizers to ensure that your exercise is of appropriate level and scope for the class. It's better to be a little short than to go over time!

## Python
All students are expected to have a basic knowledge of programming. If you haven't worked with Python before, please take an online introductory course prior to the start of class such as those offered by [codecademy](URL=https%3a%2f%2fwww.codecademy.com%2flearn%2flearn-python) and [udacity](https://www.udacity.com/course/intro-to-computer-science--cs101). [A Byte of Python](https://python.swaroopch.com/) is a free eBook; however, you will need your own copy of Python to run and test the code.

We will be using Python 3.7 for the course. Some of you may be familiar with older versions of Python such as Python 2.7. However, many popular third-party packages that you may use in your research (e.g., Numpy, Scipy and Pandas) [longer support Python 2](https://python3statement.org). If you have been using Python 2, take a few minutes to familiarize yourself with the [differences between Python 2 and 3](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html).

### Python server
There are several ways to write and run Python code. For this class, we will use [Jupyter notebooks](https://jupyter.org). Notebooks are documents that contain live code, equations, visualizations and narrative text. Prior to each class you will need to download the files and potentially update some packages.

We have a [cheat sheet](cheatsheet.md) for using the Jupyter notebooks.

### Installing Python
These days I recommend the [Anaconda Python Distribution](https://www.anaconda.com) since it is free to use (both for commercial and academic use), can be installed on computers without administrative privileges and makes it easy to install various third-party Python packages. To get started with your own copy of Python::

* [Download](https://www.anaconda.com/download) the installer and run it. Select all default options. When it asks you whom to install for, select "Just Me" (the recommended option). You can skip the option to install Microsoft VsCode.

* On Windows the installer will create several new shortcuts in your start menu (under `Anaconda3 (64-bit)`):

    * Anaconda Navigator - A GUI for managing Anaconda Python (including installing and upgrading third-party libraries). It also offers a launcher for key applications such as Jupyter Notebook, Jupyter Lab and Spyder).
	* Anaconda Prompt - A command line prompt that allows you to install and upgrade third-party libraries (an alternative to the GUI offered via Anaconda Navigator).
	* Jupyter Notebook - A local version of the notebook server that we're using.
	* Spyder - An integrated desktop environment for Python.

### Code editors
You need a way to write Python code. The best way to do this is to use a dedicated code editor. There are many options out there, so if you already have a preferred one feel free to use it. For new programmers, I suggest the following options (which can be launched from the Anaconda Navigator application):

* [Spyder IDE](https://www.spyder-ide.org). This provides you with a Matlab-like integrated development environment including a file editor, interactive Python prompt and variable browser. This should already have been installed with Anaconda Python. If it's not already installed, you can open up the Anaconda prompt and type `conda install spyder`.

* [Jupyter Notebook](https://jupyter.org). This will allow you to run a local version of the Jupyter notebook server that we are using for the course. You will also be able to download the course notebooks and work with them on your own computer if you have Jupyter installed. If it's not already installed, you can open up the Anaconda prompt and type `conda install jupyter`. If you can get this up and running, it may be the most stress-free option for working on the notebooks when off-campus as you will not need to deal with remote login issues and internet access.

* [JupyterLab](https://blog.jupyter.org/jupyterlab-is-ready-for-users-5a6f039b8906). This is the next-generation user interface for Jupyter and will likely supplant Jupyter's Notebook interface. It allows you to open multiple file types (including notebooks) side-by-side. Although this is still beta software, it will likely replace the standard Jupyter Notebook server by the end of 2018.

### Course-specific resources
* [NEUS642 on Slack](https://neus642.slack.com) - Our online chatroom. The course staff will try to monitor this when we can. Use this for asking questions.
* [NEUS642 on Github](https://github.com/bburan/NEUS642) - The source code repository for the class. All new files and updates will be posted here.

### Other resources
There are many resources available online for learning Python. [Here are
a few](resources.md).
