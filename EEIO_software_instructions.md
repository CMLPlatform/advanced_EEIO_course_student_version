# Software management recommendations in preparation to the lectures’ practical exercises

## 1. Jupyter Notebooks

During the practical exercises, we will use Jupyter notebooks to facilitate explanation of the code and breakdown of sections and exercises. You are not obliged to use Jupyter as the exercises can also be performed in any other Integrated Development Environment (IDE) such as Spyder or Visual Studio. However, we do recommend you familiarize yourself and try to use Jupyter because it will make it easier for you to follow instructions, and it is an important tool to know because of its broad use in many contexts, from tutorials to the development of interactive reports.

**You can access Jupyter Notebooks or Jupyter Lab through the Anaconda Navigator.**

To gain a better understanding of Jupyter notebooks, you can read or watch the following resource:

- Nice intro with use contexts and tutorial: <https://www.dataquest.io/blog/jupyter-notebook-tutorial/>
- Cut and dry guide: <https://realpython.com/jupyter-notebook-introduction/>
- Comprehensive video tutorial: <https://www.youtube.com/watch?v=HW29067qVWk>
- Additional information: <https://jupyter.org/>

## 2. Virtual Environments

Virtual environments allow you to have multiple isolated python installations independent from each other, thereby avoiding package conflicts across software and facilitating transfer and reuse of software. In practical terms, they are folders in which a specific python version is installed together with any of its packages. When you are using platforms such as Anaconda, or an IDE such as spyder or Visual Studio, their default settings will always use either a **base** environment or whatever python installation comes with your operating system. This can create problems such as conflicts with third party application or other software projects you may be working today or older ones. For these reasons, we recommend you work on a new virtual environment and not the base environment that comes by default with Anaconda. It’s always good practice to use a different environment than the base environment or the one that may come preinstalled in your operating system.

To learn more:

- How to create virtual environments in anaconda: <https://docs.anaconda.com/navigator/tutorials/manage-environments/>
- Comprehensive overview and instructions for virtual environments <https://realpython.com/python-virtual-environments-a-primer>
- Why you need virtual environment <https://realpython.com/python-virtual-environments-a-primer/#why-do-you-need-virtual-environments>

## 3. Accessing the exercises

All Jupyter Notebooks are provided through brightspace but if you want you can also access them on their original GitHub repository at this url: <https://github.com/CMLPlatform/advanced_EEIO_course_student_version>

If you want to work with the original repository instead of the snippets of code through Github Gist, keep on reading the following Git optional instructions.

### 3.1 Git optional instructions:

While you can download the exercises directly from brightSpace, we recommend you familiarize yourself with git procedures instead, as these are fundamental skills in good software management practices.

If you don’t have it already, you will need to create a github account: <https://github.com/join>

All these procedures can be perfomed both in Github desktop or in any terminal such as Anaconda Prompt, Windows PowerShell or Linux Bash Shell

**Step 1:** Open your terminal or Github desktop app (bash on Linux or PowerShell in windows)

**Step 2:** If git is not already installed on your machine, you should install git by using the following procedures <https://github.com/git-guides/install-git> or installing Github desktop <https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/>

**Step 3:** Once you installed git you will need first to fork the repository (i.e., make a copy) <https://docs.github.com/en/get-started/quickstart/fork-a-repo> . You will find the forked repository on your own Github page

**Step 4:** Clone (i.e., download) your forked repository locally so that you can work on the code on your computer <https://github.com/git-guides/git-clone> . By clicking on the green code button in your repository you will see the options you have to clone

In the terminal: git clone [.git link to the repository]

#### If at the end of the exercise you want to save your work

**Step 5:** Check first what files were changed in your repository

On the terminal: git status

**Step 6:** Adding or removing files that you want to commit (i.e., save)

In the terminal if you want to add files that have been changed: git add [name of the file]
If you want to remove files that have been changed: git rm [name of the file] (or git rm --cached [name of the file] if you want to eliminate the file only on github)

**Step 7:**

- Commit your work by typing
- git commit -m “Short comment on what you changed”

**Step 8:**

Finally add your changes to your remote (i.e., online) repository by typing
- git push

**Step 9:**

- Every week, we will update the original repository so you will need to sync your fork by performing these procedures <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork>
