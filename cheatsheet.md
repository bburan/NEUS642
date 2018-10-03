# Exajupyter server

Your Jupyter server has two main folders for class:

* notebooks - This is your personal copy of the notebooks for the course. You can edit and revise the notebooks as needed. Inside this folder will be a separate folder for each week. Each class will have two notebooks. The one ending in `student.ipynb` is the one you should open for class. The one ending in `answers.ipynb` is the one that contains all the answers.

* shared_notebooks - This is a shared folder so you can easily share your work with the rest of your team. All files in this folder are immediately viewable, and editable, by the rest of the class. When working on the draft of your notebook, please make a subfolder in the format `YYMMDD` for the week you are presenting. Jupyter notebooks are not meant to be simultaneously edited, so coordinate with your teammates to ensure that you aren't trying to edit the files at the same time. If you do, you almost certainly will lose some work.

## Collaborative editing

When trying to collaboratively edit notebooks using the shared folder, we recommend that you make a copy of the notebook you're editing rather than editing the same notebook in place. Once you've finished editing the notebook, let the others on your team know the name of the notebook you just created.

As you develop your notebook you may find that a particular library you need isn't installed (i.e., you get an `ImportError`). Please send Brad a message on Gitter (@bburan) and he will install it for you.

## Class notebooks

Each week at the beginning of class, you will need to copy the notebooks and data for that class to your personal `notebooks` folder. To do so, open a terminal and type:

	NEUS642_update_notebooks

By default, the update script will not overwrite existing files. If you ever want to revert to the original copy of the notebook, you can do so by renaming (or deleting) the notebook you want to revert and then running `NEUS642_update_notebooks` again.

# Running your own Jupyter notebook

Once you have installed Anaconda Python ([instructions](index.md)), a new program, `Anaconda prompt` should be available (via the Windows start menu or Mac OS equivalent). Launch this prompt. This prompt behaves much like the `Terminal` available via the Jupyter notebook browser. However, the commands that you are familiar with (e.g., `NEUS642_update_notebooks`) will not be available via your local install.

Anaconda Python allows you to run multiple versions of Python (and third-party packages). This is particularly useful if you write a lot of code. For example, if some of your code does not work with a recent version of Python and/or third-party packages, you may wish to stick with an older version until you have the time to update your code. However, you can write new code that takes advantage of features available in newer versions of packages. The way this works is by creating **environments**. An environment defines the version of Python and third-party packages that will be loaded whenever you run your code. By default, Anaconda provides a base environment (called `base`). If you do not specify the environment, then the Python version and third-party packages installed in this environment will be loaded when you run your code.

## Creating a conda environment

Since some of you will likely be playing around with Python outside of class and adding or removing various third-party libraries, we want to create an environment, called `NEUS642`, that contains the set of third party libraries required for running the notebooks. This will ensure that you do not accidentally uninstall or "downgrade" (i.e., install an older version of a package) when playing around with Python outside of class. Let's create this environment. In your Anaconda prompt, type:

	conda create --name NEUS642 python>=3.7 jupyter matplotlib numpy scipy pandas seaborn>=0.9.0 git

It may take a while to run. After thinking for a while, it will present you with a list of all the packages it needs to install and ask for permission. Although we only specified a few packages, these packages have many dependencies and will pull in a large number of other packages. Conda is a package manager. You tell it what you need installed and it will take care of the rest to ensure that all additional dependencies are installed. 

Here, we're creating an environment with the specified name, `NEUS642` and installs seven packages in it. For several of the packages, we have specified a minimum version number. For example, the exercise from October, 2, 2018 requires a function available only in version 0.9.0 or later of `seaborn`. Once you have created your environment, you need to tell Anaconda that you wish to use this environment when you run your code. You can do this by **activating** your environment:

	conda activate NEUS642

Once the environment is activated, you will see (at the beginning of the terminal prompt), the name of the environment. From this point on, whenever you run Python code in this terminal it will default to the versions of libraries installed in this environment. *If you close your Anaconda prompt and open a new one, you will have to re-activate your environment otherwise Anaconda will default to what's installed in the base environment.*

Notice that we included `git` when we created the environment. Git is not a Python package. It's a program that manages source code. The notebooks for class are stored in a Git repository on Github. Let's copy these notebooks to a local folder. First, decide where you'd like to store these notebooks. It's completely up to you. If you aren't sure, then do the following:

	mkdir classes
	cd classes

Now, clone the Git repository:

	git clone https://github.com/bburan/NEUS642

If you used the default folder above, the notebooks will now be available at:

	classes/NEUS642/notebooks

While still in the Anaconda prompt (with the NEUS642 environment active), change to the notebooks folder and launch a Jupyter notebook:

	cd NEUS642/notebooks
	jupyter notebook

A browser tab should automatically open. If it doesn't, go to http://localhost:8888 in your browser.

## Before each class

To copy the new notebooks, open an Anaconda prompt and CD to your NEUS642 folder:

	cd classes/NEUS642
	git pull

We may also have instructions on additional packages and libraries that need to be installed for the week's exercise. Stay tuned to Gitter for details.

## To reopen the Jupyter notebook

Open an Anaconda prompt and run the following:

	cd classes/NEUS642/notebooks
	conda activate NEUS642
	jupyter notebook

A browser tab should then open with the Jupyter notebook.

# Creating a notebook for class

## Formatting

The course staff has a script that will automatically format your notebook in preparation for class. The script will:

* Scan for all markdown headings (lines starting with `#`, `##`, `###`, etc.) and create a table of contents at the top of the file.
* Scan for comments in code cells starting with `# Answer`, deleting everything from `# Answer` to the end of the cell, and insert `# Your answer here`. Note that the cell can contain text *before* the `# Answer` line that will not get deleted.
* Scan for all markdown headings (e.g., `## Exercise`, `### Exercise`, etc.) and auto-number them.

To take advantage of this script, ensure that you use markdown formatting for your headers and do not number your exercises:

    # Main header
	Text goes here

	## Subheader
	Text goes here

	### Exercise
	Text goes here

	# Main header
	Text goes here

	## Exercise
	Text goes here

For your answers, the cell containing the answer should be in the format:

	# Answer
	<code for actual solution>

In the student copy of the notebook, the cell will be converted to:

	# Your answer here

In the teacher copy of the notebook, the cell will be converted to:

	%load "answers/answer001.txt"
	
When presenting your notebook during class, the first time you run the cell it will copy the answer code into the cell. The second time you run the cell, the code will be executed. If you decide to test your version of the teacher notebook before class, the answer cells will be overwritten with the version that has the answer loaded. Please be sure to delete your copy of the teacher notebook and run `NEUS642_update_notebooks` to get the original version of the teacher notebook.
