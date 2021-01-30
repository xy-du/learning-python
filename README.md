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

* I do not consider the branches in this repo carry the meaning that branches should do. You will see that they are
  basically sequential, and the reason behind this is that at the beginning, I want give different part of the
  development process of this repo some tag-like things, but as time goes by, I realise that I often have to use the
  code from a early time, so totally separated branches seems not a wise choice. And yes, I can keep merging into the
  master, but that will be just simple fast forward, so I think, why bother? :)

* Compare every commit with the one before it to see the increment made in current one is a good way to review. Say, you
  are using pycharm. Just open the Git tab and browse all the commits. When you click a commit, the changed file in that
  commit will show, click the file you will see the changes made in that file, which is the self-contained code snippet.

* If you try to run .py files, there something you need to know. In the early stage of this project, you can see all the
  output in one .py file. But later, I find that this makes it hard to identify the output of certain piece of code in
  that file, so when I made some addition in a commit, I commented all the output of earlier commits in the same file.
  And sometimes, the file will not be able to run since there are errors, this is intentional, this is when you should
  select certain piece of the code and run them in the python console(right click on the code you want to run and you
  will see it, option+shift+E in pyCharm on macOS), don't worry, when this is the case, there will be indications.