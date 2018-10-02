Your Jupyter server has two main folders for class:

* notebooks - This is your personal copy of the notebooks for the course. You can edit and revise the notebooks as needed. Inside this folder will be a separate folder for each week. Each class will have two notebooks. The one ending in `student.ipynb` is the one you should open for class. The one ending in `answers.ipynb` is the one that contains all the answers.

* shared_notebooks - This is a shared folder so you can easily share your work with the rest of your team. All files in this folder are immediately viewable, and editable, by the rest of the class. When working on the draft of your notebook, please make a subfolder in the format `YYMMDD` for the week you are presenting. Jupyter notebooks are not meant to be simultaneously edited, so coordinate with your teammates to ensure that you aren't trying to edit the files at the same time. If you do, you almost certainly will lose some work.

Collaborative editing
---------------------
When trying to collaboratively edit notebooks using the shared folder, we recommend that you make a copy of the notebook you're editing rather than editing the same notebook in place. Once you've finished editing the notebook, let the others on your team know the name of the notebook you just created.

As you develop your notebook you may find that a particular library you need isn't installed (i.e., you get an `ImportError`). Please send Brad a message on Gitter (@bburan) and he will install it for you.

Class notebooks
---------------
Each week at the beginning of class, you will need to copy the notebooks and data for that class to your personal `notebooks` folder. To do so, open a terminal and type:

	NEUS642_update_notebooks

By default, the update script will not overwrite existing files. If you ever want to revert to the original copy of the notebook, you can do so by renaming (or deleting) the notebook you want to revert and then running `NEUS642_update_notebooks` again.

Formatting your notebook
------------------------
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
