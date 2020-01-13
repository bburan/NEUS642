# Tools for course staff

We use `nbstripout` and `nbdime` to help manage Jupyter Notebooks. You can install them:

	pip install nbstripout
	pip install nbdime
	cd <path to NEUS642 repository>
	nbstripout --install

You'll need to work closely with the students to help them develop their Jupyter notebooks. A number of tools are available to help you with the process. First, ensure that the students are familiar with the formatting instructions in the `cheatsheet`. Once they send you a notebook for review, you can edit it as needed. You should follow these steps:

* Create a new folder with the date of the class in the NEUS642 repository (e.g., `2020/200114`).
* Copy their notebook to that folder, ensure it ends in `- base.ipynb`.
* Run `nbstripout` on the notebook to remove the output (e.g., `nbstripout "notebook - base.ipynb"`).
* Commit the notebook (e.g., `git add "notebook - base.ipynb"; git commit`).
* Now, edit the notebook using Jupyter.
* Run the script, `bin/NEUS642_format_notebook "2020/201114/notebook - base.ipynb"` to create the formatted versions. The latest version of the script automatically calls `nbstripout`, so you do not need to perform this step separately.
* Review the formatted versions. Report any bugs in the script to Brad. Edit the base version of the notebook as needed to fix the formatting (you need to ensure Jupyter Notebook is saving your changes via `File -> Save and Checkpoint` before running the `NEUS642_format_notebook` script).
* Once you are happy with the notebook and are ready to send your feedback to the students, commit the notebook to the Git repository.
* Generate a nice HTML-formated diff so the students can easily see what you've changed. 

To generate the HTML-formatted diff you'll need the Git hash for the commit of the original notebook (provided by the students) and your edited version of the notebook. To look up the Git hash:

	git log

It will give you the following output:

	commit 618c2c9428f14574190cabf092c44dc903bdec88 (HEAD -> master, origin/master, origin/HEAD)
	Author: Brad Buran <bburan@alum.mit.edu>
	Date:   Mon Jan 13 12:11:19 2020 -0800

		Edited version of 20014

	commit d00dfa718bb3152299d85de44ea69765cca3a8cf
	Author: Brad Buran <bburan@alum.mit.edu>
	Date:   Mon Jan 13 10:11:46 2020 -0800

		Initial commit of 200114

Find the commits. You only need the first six digits of the comit hash (which
looks like `d00dfa718bb3152299d85de44ea69765cca3a8cf`). In this example, the commit hash for the student's version is `d00dfa` and the edited version is `618c2c`). Generate the HTML diff using:

	nbdiff-web d00dfa 618c2c "notebook - base.ipynb" --show-unchanged

A browser will open with a nicely-formatted diff. You can export this to a HTML file that can be emailed to the students. They can save the HTML file to their computer and open it in any browser.
