# learning-python

Introduction
--------------

This project is a record of my python learning process. Each commit is a code snippet, most of which are self-contained.
Generally speaking, different branches represent different topics, and the commits contained therein have a certain
continuity.

Book
--------------
[*Fluent Python: Clear, Concise, and Effective Programming*](
https://www.amazon.com/Fluent-Python-Concise-Effective-Programming/dp/1491946008)

Heads-Up
--------------

* At the beginning, it's some basic knowledge, so I did not use different branches and just develop on the master .
  later on I develop on different branches but didn't merge them into the master for a while. After that, I merged all
  the branches into mater and begin the normal develop-and-merge process.

* Compare every commit with the one before it to see the increment made in current one is a good way to review. Say, you
  are using pycharm. Just open the Git tab and browse all the commits. When you click a commit, the changed file in that
  commit will show, click the file you will see the changes made in that file, which is the self-contained code snippet.

* import statement should on the top of every file, yes. But here in this repo, you will see import in the middle of a
  file and I am sorry for that, it's just convenient for write and review since it's close to where it's used.

* If you try to run .py files, there is something that you need to know. In the early stage of this project, you can see
  all the output in one .py file. But later, I found that this makes it hard to identify the output of certain piece of
  code in that file, so when I made changes, I commented all the output of earlier commits in the same file. And
  sometimes, the file will not be able to run since there are errors and this is intentional, that's when you should
  select certain piece of the code and run them in the python console(right click on the code you want to run and you
  will see it, option+shift+E in pyCharm on macOS), don't worry, when this is the case, there will be
  indications.Another scenarios you will see is that at early stage, many small pieces of code are all writen in one
  file but later, the code contained in one file became more topic-focused.