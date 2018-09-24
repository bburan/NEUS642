Your Jupyter server has two main folders for class:

* notebooks - This is your personal copy of the notebooks for the course. You can edit and revise the notebooks as needed. Inside this folder will be a separate folder for each week. Each class will have two notebooks. The one ending in `_student.ipynb` is the one you should open for class. The one ending in `_answers.ipynb` is the one that contains all the answers.

* shared_notebooks - This is a shared folder so you can easily share your work with the rest of your team. All files in this folder are immediately viewable, and editable, by the rest of the class. When working on the draft of your notebook, please make a subfolder in the format `YYMMDD` for the week you are presenting. Jupyter notebooks are not meant to be simultaneously edited, so coordinate with your teammates to ensure that you aren't trying to edit the files at the same time. If you do, you almost certainly will lose some work.

Each week at the beginning of class, you will need to copy the notebooks and data for that class to your personal `notebooks` folder. To do so, open a terminal and type:

	NEUS642_update_notebooks

By default, the update script will not overwrite existing files. If you ever want to revert to the original copy of the notebook, you can do so by renaming (or deleting) the notebook you want to revert and then running `NEUS642_update_notebooks` again.

As you develop your notebook you may find that a particular library you need isn't installed (i.e., you get an `ImportError`). Please send Brad a message on Gitter (@bburan) and he will install it for you.
