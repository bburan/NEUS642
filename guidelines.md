# General guidelines for a good presentation

The focus is on ensuring the students *learn* something about Python or reinforce concepts they already know. The goal is not to teach them how to do a particular analysis (although learning that will be incidental). If the focus of the presentation is on the analysis with minimal time spent introducing new concepts (e.g., `for`, `if else`, `while`, `with`, tuple unpacking, etc.), then you are likely to lose the students. At that point, they won't learn anything (either Python-related or related to your analysis).

Over the years we have noticed the following guidelines result in a successful presentation:

## Build up to more complex concepts slowly. 

If you want the class to create a function, work through the various operations of the function (e.g., loading the file and performing the calculation) in a sequence of exercises. Once they know how to perform the operations, then you can ask them to create the function in an exercise. While the solution for the exercise where you create the function will typically be a matter of cut-and-pasting the answers to the previous exercises, it still is a good learning exercise.

## Give a way to check their answer

This can be as simple as giving them some information about what the answer should look like (e.g., it should be a 2D array of shape (16, 32)) or a screenshot of the result.

## Include bonus exercises where possible

There can be quite a bit of downtime in between exercises for some those who finish early. Bonus exercises give them something to do while others catch up. The rest of the notebook should not depend on successful completion of the bonus exercises.

## Minimize the ability to create errors

Often an answer cell will be run multiple times while coming up with the answer. This can result in cumulative effects of running code on the result, e.g.,

	result = result[:-1]

will continue chopping one value off of the sequence each time it is executed. Try to identify potential cases where cumulative runs will continue modifying the variable and give explicit instructions to avoid this. For example, "please take all but the last value and store it in a new variable, `new_result`".

## Be explicit about what you want done

It's OK to provide a template for the answer (e.g., cut and paste this code and then fill in the missing parts). This is especially ueful when introducing new concepts (e.g., functions, loops, etc.). Sometimes showing the expected output helps illustrate what you want done.

# Common issues encountered

## The student gets a different result than expected

If the error is in the answer being discussed, it is often obvious what the problem is. However, sometimes the error occurs in a much earlier answer and is not detected for a variety of reasons. So, if you're stumped, make sure that the previous answers are correct. Also, remember that executing a cell multiple times may result in getting the wrong answer, so you sometimes need to "reset" by re-running from the beginning of the notebook. 

