# Git / Web Developer Tools (FWDN 232) — Full Lecture Notes


# Chapter 1: Introduction to Git & Version Control


## Slide 1

Chapter 1: Introduction
Full Stack Web Developer
FWDN 232: Web Developer Tools
Based on slides accompanying the book
Jump Start Git, Second Edition 2020
by Shaumik Daityari

---

## Slide 2

Course main Objectives
The course aims to provide the student with basic knowledge and skills to use version control tools to track and manage changes to code files.

---

## Slide 3

Course Content

---

## Slide 4

Learning Resources

---

## Slide 5

Introduction
Suppose a freshman year in college, started work on his first intranet application.
The files in the main directory of the partially functioning application looked something like.

---

## Slide 6

Introduction
Looking at the file names in this directory, we can see that he used some very similar names, such as exam.php, exam1.php and examfile.php.
The purpose of that naming convention was to create new versions of his application without losing the old, working logic—in case the new ideas failed!
He assumed that, because he understood what each of those files did, it should be fine to have a bunch of similarly named files.

---

## Slide 7

Introduction
However, there were two flaws in that thinking.
Firstly, anyone else examining this code wouldn’t be able to make sense of this mess.
Secondly, after a few months, even he was struggling to recall what each version of these files was for.
Clearly, he needed a better system for managing the various versions of my files.

---

## Slide 8

Introduction
If he had this much trouble working on a small, personal project, imagine how difficult it must have been for larger software projects, with thousands of files and contributors distributed all over the world!
Developers once used emails to coordinate changes among team members.
When they made changes to a project, they would each create a “diff” file with all their changes and email it to the lead developer, who would incorporate them into the project if everything worked properly.

---

## Slide 9

Introduction
When you’re working on the same files as other developers, keeping track of what you’ve changed and trying to merge it with work done by your peers becomes very difficult.
It can result in a lot of confusion and time wasting.

---

## Slide 10

Introduction
Imagine another situation, where you’re working on an idea and your boss wants to see what you’ve already completed.
Ideally, you’d want to be able to do the following:
stash away the changes and revert to the last stable state.
show your boss the latest completed work.
resume your work with the current state once that’s done.
All of the situations described earlier give rise to the need for what’s known as “version control”.

---

## Slide 11

Version Control
Version control (or revision control) is a system that records changes to a file or a group of files and directories over time, so that you can review or go back to specific versions later.

---

## Slide 12

Version Control
Quite literally, version control means maintaining versions of your work—perhaps most commonly in the form of source code, though it can be used for other kinds of work too.
You may like to think of version control as a tool that takes snapshots of your work across time, creating checkpoints.
You can return to those checkpoints any time you want.
Not only are the changes recorded in these checkpoints, but also information about who made the changes, when they made them, and the reasons behind the changes.

---

## Slide 13

Version Control
As mentioned before the first objective of version control—to back up and restore.
Version control eliminates the need to create backup files like what the freshman was doing in his college days (that is, endless duplicates with different names).
Version control also gives you the ability to return to previous states of your work without losing the current state.

---

## Slide 14

Version Control
Version control doesn’t replace the need for a regular backup solution.
The word “backup” above, as noted, refers to the process of creating multiple copies of the same file. Git removes the need for that.
However, this is different from regularly backing up your files to an external source—such as a portable drive or cloud storage—to ensure you don’t lose anything following a disk failure.

---

## Slide 15

Version Control
Version control lets you synchronize your work with peers who are working on the same projects.
In other words, it enables you to collaborate with others without the possibility of someone’s changes overwriting someone else’s work accidentally.
Version control also tracks changes to a project and other data associated with the changes.
It makes the process of debugging your code easy too.

---

## Slide 16

Version Control
Conflicts in files can also be resolved through version control—such as when multiple people have made changes to a file that clash.
A version control system highlights the conflicts and provides an opportunity to fix them.

---

## Slide 17

Version Control
Yet another feature of version control is that it enables work on multiple features of a project at the same time.
This gives great scope for experimentation, trial, and error.
Each feature can be developed independently of the others, and can easily be removed if it doesn’t work out.
Reliable
Multiple files
Meaningful versions
Revert
Review history
Merge
Track responsibility
Work in parallel
Work-in-progress
Features of a version control system

---

## Slide 18

Features of a version control system
Reliable: keep versions around for as long as we need them; allow backups
Multiple files: track versions of a project, not single files
Meaningful versions: what were the changes, why where they made?
Revert: restore old versions, in whole or in part Compare versions

---

## Slide 19

Examples of Version Control in Daily Life
You’ve probably visited the Wikipedia site at some point.
You may even have taken the opportunity to update its content, too—as we’re all invited to do.
When editing a page, you may also have checked its history.
That’s where things get really interesting.
The history page shown in figure above lists changes to that page.  It also records the time of the change, the user who made it, and a message associated with the change.  You can examine the complete details of each edit, and even revert back to an older version of the page.  This is a good example of a simple form of version control.

---

## Slide 20

Examples of Version Control in Daily Life
Google Docs provides another example of version control that you might experience in daily life.
If you check the revision history of a file in Google Docs, shown the figure above, you’ll notice that Google saves the state of your file after every few changes.
You can preview the status of the document in any of those previous states—and choose to revert back to it, if needed.

---

## Slide 21

Version Control Systems: the Options
There are two types of version control systems (VCS), known as
centralized
distributed

---

## Slide 22

Centralized Systems
Centralized systems have a copy of the project hosted on a centralized server, to which everyone connects in order to make changes.
Here, the “first come, first served” principle is adopted: if you’re the first to submit a change to a file, your code will be accepted.

---

## Slide 23

Distributed System
In a distributed system, every developer has a copy of the entire project.
Developers can make changes to their copy of the project without connecting to any centralized server, and without affecting the copies of other developers.
Later, the changes can be synchronized between the various copies.

---

## Slide 24

Version Control Systems: the Options
In the earliest version control systems, files were tracked only locally, and only one person could work on a file at a time.
Examples of these include Source Code Control System (SCCS) and Revision Control System (RCS), which were common in the 1970s and 1980s.
The next step forward was the introduction of client-server version control systems, which enabled multiple authors to work on the same file (although some still worked on the first come, first served basis).
Examples of such systems include the Concurrent Versions System (CVS) and Subversion, which are still in use today.

---

## Slide 25

Version Control Systems: the Options
Since around 2005, distributed systems have gained widespread acceptance, with the emergence of systems such as Git, Mercurial and Bazaar.
VCS Is Not CVS
Don’t confuse the abbreviations VCS (version control system) and CVS (concurrent versions system).
CVS is just one of the many kinds of VCS.

---

## Slide 26

Enter Git
This course is about Git, a distributed version control system.
Git tracks your project history, enabling you to access any version of it back in time.
It also allows multiple people to work on the same project, helping avoid confusion when more than one person tries to edit the same file.

---

## Slide 27

Enter Git
Git was created by Linus Torvalds (who is also known for the Linux kernel), and Junio Hamano is its primary developer.
Git, as described on the Git website, is a source code management (SCM) solution, but essentially it’s just a type of version control system.
The primary objective behind Git was to implement and design a version control system that was distributed, reliable and fast.
While working on Linux, Torvalds needed a version control system to manage the Linux codebase.
BitKeeper was a distributed system at that time, but Torvalds believed that, although BitKeeper was a good option, being a commercial product made it unsuitable for the development of an open-source project like Linux.

---

## Slide 28

Enter Git
Torvalds had three criteria for a version control system: it had to be distributed, efficient and safe from corruption.
There was no open-source, distributed version control system in the mid-2000s that could satisfy all these conditions.
Hence, Git was developed out of necessity.

---

## Slide 29

Git’s Philosophy
Torvalds once explained in a Google Tech Talk his reasons for creating Git. He has very strong views on the subject of version control, and I suggest you go through the talk once to understand the philosophy of Git. In this talk, Torvalds explains that he came up with the name Git because he believes the silliest names are our best creations. However, I recommend that you only watch the talk after you’re comfortable with the basic Git operations, as it’s not a tutorial: it’s aimed at users who have some knowledge of Git or other version control systems.

---

## Slide 30

Advantages of Distributed VersionControl Systems
Torvalds insisted on a distributed system because of the independence it affords to developers.
With a distributed system, you can work on your copy of the code without having to worry about ongoing work on the same code by others.
What makes it even better is that any distributed copy of the project can contain all the history of the project.
A distributed system also lets you work offline, meaning you can make changes without having access to the server that stores the central repository.

---

## Slide 31

Advantages of Distributed VersionControl Systems
Another advantage of distributed systems is that you can sync your repositories among yourselves, bypassing the central location.
Let’s say the access to the main server goes down and you have to collaborate with a colleague.
You can share changes with your colleague and continue to work on the project together, and then later push all your changes to the location everyone has access to.

---

## Slide 32

Advantages of Distributed VersionControl Systems
In a centralized system, anyone who makes a change needs to be given access to the central location.
In contrast, in a distributed system, new developers can make changes to their own repositories without being granted write access, while more experienced contributors can be given write access and the ability to review other contributions before merging them into the repository.
Managing access is easier in distributed systems.

---

## Slide 33

Code Exchange in Centralized and Distributed Systems

---

## Slide 34

Git and GitHub
Since its creation, Git has become immensely popular— not only due to its own merits and the fact that Torvalds created it, but also because of the popular code-sharing site GitHub.
People often confuse Git and GitHub, but they are quite different things.
GitHub provides services that are related to Git.
It’s a website that helps you manage Git-controlled projects.

---

## Slide 35

Git and GitHub
GitHub allows users to put their Git repositories on the cloud, and to perform Git-based operations through a web interface.
It also provides desktop and mobile apps that offer the same services.
GitHub was launched a few years after Git, and remains very popular among enthusiasts of open source.

---

## Slide 36

Git and GitHub

---

## Slide 37

Git and GitHub
There are many other websites like GitHub, such as Bitbucket and GitLab.
GitHub and Bitbucket are cloudbased solutions, but GitLab allows you to set up this functionality on your own servers.
Other, similar services have come and gone, but these options have remained popular over the last few years.

---

## Slide 38

What Have You Learned?
What is version control?
How do we unknowingly use version control in our lives?
What are the types of VCS?
What is Git? What are its capabilities?

---

# Chapter 2: Getting Started with Git


## Slide 1

Chapter 2 Getting Started with Git
Full Stack Web Developer
FWDN 232 : Web Developer Tools
Based on slides accompanying the book
Jump Start Git, Second Edition 2020
by Shaumik Daityari

---

## Slide 2

Installation
The first step is to install Git.
Git’s official website provides detailed instructions on installing Git on your local machine, depending on your operating system.
The easiest way to install Git is through a package manager based on your operating system.
Package managers usually have older but more reliable versions of Git.

---

## Slide 3

Installation
If you’re using Linux, you can install Git through the terminal using a package manager. For the popular Linux distro Ubuntu, Git can be installed using apt-get:
apt-get install git
In macOS, if you have Homebrew, you can install Git using the command line through the following command:
brew install git
If you’re on Windows, the official build of Git can be downloaded from the Git website:
https://git-scm.com/download/win

---

## Slide 4

GUI Tools
For Windows and macOS, you can also install Git as a part of a GUI tool such as GitHub for Desktop and Sourcetree.
We’ll cover GUI tools in detail in Chapter 9.
However, for most parts of this book, we’ll stick to the command-line interface to really understand how Git works.

---

## Slide 5

The Git Workflow
Git doesn’t track all of the files stored on your computer.
You need to instruct Git to track certain files and directories.
This process is called initialization.
The parent directory containing your project—all the files and directories to be tracked by Git—is called a repository.
This repository might contain many files and directories, or even just a single file.

---

## Slide 6

The Git Workflow
There are three basic operations performed by Git on your project :
track,
stage, and
commit.

---

## Slide 7

Track
Once you’ve initialized your repository, you’ll need to add files to your project.
Any files you add are initially untracked by Git.
You need to specify that you want Git to track them.
Git monitors tracked files for changes and ignores untracked files.

---

## Slide 8

Stage
After making the required changes to your files, you need to stage them.
Staging is a way of tagging certain (or all) changes that you want to keep a record of.

---

## Slide 9

Commit
The next step is to create a commit.
A commit is like a photograph that records the current state of your code.
You can go back to a certain commit at a later time, view the status of the repository with respect to that commit, and check the changes that were made in the commit.
The commit records the changes in a repository since the last commit.
You can revert back to any commit at any point of time.
Each commit contains a commit hash that uniquely identifies the commit, the author details, a commit message, and the list of changes in that commit.

---

## Slide 10

Push
Once you’ve committed your files, you may wish to push them to a remote location.
A push refers to the process of sending the changes you’ve made in your local repository to a remote location.
A remote location is a copy of your repository stored on a remote server.

---

## Slide 11

The Git Workflow
Essentially, the flowchart in the following figure illustrates the steps we’ll follow in this chapter.
Push
Initialize

---

## Slide 12

Baby Steps with Git: First Commands
Set Configuration Settings
Create a Git Project
Create Our First Commit

---

## Slide 13

Set Configuration Settings
Before we proceed with using Git in a project, let’s define a few global settings:
git config --global user.name "Shaumik"
git config --global user.email "sdaityari@gmail.com"
git config --global color.ui "auto"
We set the default name and email to be associated with our commits.
We also set the color.ui to "auto" to enable Git to color-code the output of Git commands on the terminal.
The --global setting allows these settings to be applied to any other repository you work on locally.

---

## Slide 14

Set Configuration Settings
If you don’t set the values for name and email, they’re left empty.
When you make a commit, it takes different values depending on the OS or the GUI tool you use.
When you make a commit without setting these parameters, Git will automatically set them based on the username and hostname.
For instance, the name is set to the name of the user that’s logged in to the computer in macOS, whereas in Linux, the name is set to be the username of the active user account.
In both cases, the email is set as username@hostname.

---

## Slide 15

Set Configuration Settings
If you want to check all the configuration settings for your repository, you can run the following command:
git config --list
Also, if you want to edit any of your configuration settings, you can do so by editing the ~.gitconfig file in Linux and macOS, where ~ refers to your home directory.
In Windows, it’s located in your home directory:
C:\Users\<username>\.gitconfig

---

## Slide 16

Create a Git Project
Let’s first create a directory where we’ll store the files for our project:
mkdir my_git_project
cd my_git_project
The first command creates a new directory, and the second changes the active directory to the newly created one.
These two commands work on all operating systems (Windows, macOS, and Linux).

---

## Slide 17

Create a Git Project
So, my_git_project is the parent directory that will contain all the files for this project.
From now on, we’ll refer to it as our project’s repository.
Now that we’re in the repository, we need to initiate Git for that directory using the following command:
git init

---

## Slide 18

Create Our First Commit
Let’s look at the repository again.
Notice the newly created .git directory, the output of which is shown below (line 2).
All information related to Git is stored in this repository.
The .git directory, and its contents, are normally hidden from view:
$ my_git_project shaumik$ git init
Initialized empty Git repository in /Users/shaumik/test/my_git_project/.git/
$ my_git_project shaumik$ ls -al
total 0
drwxr-xr-x 3 shaumik staff 96 Mar 21 23:05 .
drwxr-xr-x 3 shaumik staff 96 Mar 21 23:05 ..
drwxr-xr-x 9 shaumik staff 288 Mar 21 23:05 .git

---

## Slide 19

Create Our First Commit
Now that we’ve initialized Git, let’s add a few files to our repository.
On your computer, navigate to the my_git_project directory and add three text files with the following names: my_file, myfile2 and myfile3.
Place some content in each one, such as a simple sentence.

---

## Slide 20

Create Our First Commit
After adding the files, let’s return to the terminal and run the following command to see how Git reacts: git status
You can see the output below:
$ git status
On branch master
No commits yet
Untracked files:
(use "git add <file>..." to include in what will be committed)
my_file
myfile2
myfile3
nothing added to commit but untracked files present (use "git add" to track)

---

## Slide 21

Create Our First Commit
In a Git repository, any file that’s added is either “tracked” or “untracked”.
A file is said to be tracked when Git monitors the changes being made to that file, whereas the changes to an untracked file are ignored by Git and don’t form a part of any commits.
Checking the status of our repository, we can see that three files are currently marked in red.
They’re also grouped as untracked.
Git doesn’t track all files in a repository.
You can explicitly tell Git which files to track and which to ignore.

---

## Slide 22

Create Our First Commit
In order to track these files, we run the following command:
git add my_file myfile2 myfile3
As an alternative, you can simply run the following:
git add .
The . (period) is an alias for the current directory.
Running git add . tells Git to track the current directory, as well as any files or subdirectories within the current directory.

---

## Slide 23

Create Our First Commit
Now that we’ve set our new files to be tracked by Git, let’s check the status of the repository again:
$ git add my_file myfile2 myfile3
$ git status
On branch master
No commits yet
Changes to be committed:
(use "git rm --cached <file>..." to unstage)
new file: my_file
new file: myfile2
new file: myfile3

---

## Slide 24

Create Our First Commit
We’re now ready to make a commit:
$ git commit -m "First Commit"
[master (root-commit) ed90340] First Commit
3 files changed, 0 insertions(+), 0 deletions(-)
create mode 100644 my_file
create mode 100644 myfile2
create mode 100644 myfile3
The -m option specifies that you’re going to add a message within the command. (The message is the text in quotes after -m: “First Commit”.)
Alternatively, you can just run git commit, and a text editor will open up and ask you to enter a commit message.

---

## Slide 25

Create Our First Commit
Notice the string ed90340 shown in the code above (second line).
It’s the hash of the commit, or its identity.
A hash is a unique, identifying signature for each commit, generated automatically by Git.
If you’re interested in how a commit hash is formed, you may want to check out “The anatomy of a Git commit”.
What’s shown here is a short version of a considerably longer string.

---

## Slide 26

Further Commits with Git
The first commit in a Git repository is a little different from subsequent commits.
In subsequent commits, Git is already tracking the files you’re working on (unless you’re adding new files).
So we’ll need another important command, git diff, which shows you the changes in the tracked files since the last commit.

---

## Slide 27

Further Commits with Git
Let’s make some changes to the files and see how Git reacts.
For demonstration purposes, I’ve added a line to my_file, and some extra words to an existing line in myfile2. Let’s check the status of the repository by running the following command:
$ git status
On branch master
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified: my_file
modified: myfile2

---

## Slide 28

Further Commits with Git
As shown here, Git shows that certain changes have been made to two files.
We can also see exactly what was changed in the files by running the following command:
$ git diff
diff --git a/my_file b/my_file
index e69de29..e32ce9e 100644
--- a/my_file
+++ b/my_file
@@ -0,0 +1 @@
+Sample line
diff --git a/myfile2 b/myfile2
index e69de29..d00491f 100644
--- a/myfile2
+++ b/myfile2
@@ -0,0 +1 @@
-Some more info
+Some more info! Changing this file too.

---

## Slide 29

Further Commits with Git
The diff command shows the changes that have been made to the tracked files in the repository since the last commit.
In the output shown above, lines starting with a + sign (colored green) show what’s been added, and the line starting with a - sign (colored red) shows what’s been removed. (When you edit a line of code, the same thing happens: the old line is shown in red with a - sign, and the new version of the line is shown in green with a +.)

---

## Slide 30

Further Commits with Git
If you want to check the changes in a single file, add the file name after the diff command. For instance:
git diff my_file
After you’ve reviewed the changes you made, you need to “stage” the changes to be committed:
git add my_file myfile2
Alternately, you can add all tracked files like so:
git add –u

---

## Slide 31

Further Commits with Git
You can go one step further and add only parts of the changes to a file to the commit.
This process is a bit complex, though, and we’ll tackle it in Chapter 6, “Correcting Errors While Working with Git”.
Now that you’ve staged the files, they’re ready to be committed:
git commit -m "Made changes to two files"

---

## Slide 32

Why git add Again?
At this point, you may think “Why add tracked files again?” Well, before you commit, Git needs you to specify which files you want to commit.
It may happen that you’ve made changes to two files but only want to commit one of those files.
The process is like sending a package. git add is adding an item to the package. git commit is sealing the package and writing a note on it.
Git push is sending the package to the recipient.

---

## Slide 33

Why git add Again?

---

## Slide 34

Commit History
Now that we have more than one commit, let’s explore a new area of Git—the history of the project.
The simplest way of reviewing the history of a project is by running git log, which shows the commits that we’ve made so far:
$ git log
commit 870e4d76e6dc6539315992f16a20f47a49e2ea79 (HEAD -$ master)
Author: Shaumik Daityari <sdaityari@gmail.com>
Date: Sat Mar 21 23:31:16 2020 +0530
Made changes to two files
commit ed90340105b9511381d76706f8e5d4e7df3f6458
Author: Shaumik Daityari <sdaityari@gmail.com>
Date: Sat Mar 21 23:16:28 2020 +0530
First Commit

---

## Slide 35

Commit History
The history shows the list of commits, each with a unique hash, an author, a timestamp and a commit message.
Previously in this chapter, we encountered a commit hash that was truncated. Although the long, 40-character commit hash uniquely identifies each commit, usually five or six characters are enough to identify them in a repository:
git show ed90340

---

## Slide 36

Commit History
The git show command lists information about a commit.
Let’s see how short we can go until Git fails to identify the hash:
git show ed90340
git show ed9034
git show ed903
git show ed90
git show ed9

---

## Slide 37

Commit History
It’s only once we’re down to the first three characters that Git gives us a fatal error:
ambiguous argument 'ed9': unknown revision or path not in the working tree.
Although it only failed at three characters in our repository with a very short history, it will probably need to be longer in repositories with a considerably longer history.

---

## Slide 38

The .gitignore File
Although I’ve mentioned that Git only tracks files you explicitly ask it to, it could happen that you ask it to track some files by mistake.
You need a way to hide certain files, directories, or file extensions from Git that you know you’ll never want it to track.
This is exactly what a .gitignore file does.
A .gitignore file is added to the root directory of the repository, and it lists files you don’t want Git to track or display as part of git status.
You can add items to the .gitignore file and commit them.

---

## Slide 39

The .gitignore File
Examples of files that you might want to add to .gitignore include compiled files with extensions like .exe and .pyc, local configuration files, macOS .DS_Store files, Thumbs.db on Windows, directories of node modules in Node.js, and build folders of Grunt or gulp.js.
Let’s have a look at what a .gitignore file looks like:
configuration/
some_file.m
*.exe

---

## Slide 40

The .gitignore File
The three lines in this sample file are used to tell Git to ignore a whole repository and its contents (the configuration directory), a single file some_file.m, and all files with a .exe extension.
The code sample below shows the effect of a .gitignore file that tells Git to ignore *.exe files that have already been committed to the repository.
I’ve created a new file called somefile.exe in our project directory, but Git is ignoring it. git status shows that there is nothing to commit:
$ echo "some line" > somefile.exe
$ git status
On branch master
nothing to commit, working tree clean

---

## Slide 41

The .gitignore File
Nowadays, many .gitignore templates are available online, depending on the framework you’re working on, such as Rails.
You may want to browse through this huge collection of .gitignore files on GitHub.
These .gitignore templates serve as handy starting points for new projects.

---

## Slide 42

Remote Repositories
As we’ve seen so far, you can use Git on your local machine to manage versions of your work.
However, because Git is a distributed version control system, many copies of the same repository can exist.
So rather than just keep your repository locally, it’s common to store another copy in a centralized location on a centralized server (or in the cloud).
This also enables you to work in a team, as others can access the repository from the centralized copy.
Any such copy of your repository can be linked to your repository to enable synchronization.
Such an external copy is called a remote.
A remote is simply a copy of your repository.
It can be on a remote server, on a peer’s system, or even on a different location within your local system. Interestingly, if you have access to your coworker’s repository (through SSH for instance), even that can be added as a remote.

---

## Slide 43

Remote Repositories
For demonstration purposes, let’s create such a copy on GitHub.
To set up a remote repository on GitHub, you first need to create an account on GitHub, or log in to GitHub with your credentials if you already have an account.
After login, click on the + arrow on the top right and select New repository to create a new repository in the cloud, shown in the figure below.

---

## Slide 44

Remote Repositories
Choose a name for your repository.
You can also choose whether to display your repository publicly or to keep it private.
Once the repository has been created, we have three options: create a new repository from the command line and push to GitHub; push the code from an existing repository from the command line; or import code from another GitHub repository.
We’ll take the second option here.

---

## Slide 45

Remote Repositories
Returning to your local repository, run the following command to synchronize it with the remote repository:
git remote add origin
https://github.com/sdaityari/my_git_project.git
git push -u origin master
We first add a remote named origin to our repository, which points to the GitHub location.
Next, the push command sends the commits from your local repository to the cloud repository. The -u option links your repository to the remote for future reference.
When you add commits later, Git will show the status of your local copy in relation to this remote repository. master is the name of the branch that we want to synchronize with the origin remote.

---

## Slide 46

What Have You Learned?
In this chapter, we covered the basics of Git:
the various ways to install Git on your system.
the three basic operations of track, stage, and commit.
the Git workflow of initialization, tracking, committing and pushing a repository.
starting a Git project from scratch.
the history of a repository.
the use of .gitignore.
setting up a remote on GitHub and pushing your code to the cloud.

---

# Chapter 3: Branching in Git


## Slide 1

Chapter 3 Branching in Git
Full Stack Web Developer
FWDN 232: Web Developer Tools
Based on slides accompanying the book
Jump Start Git, Second Edition 2020
by Shaumik Daityari

---

## Slide 2

Remember: Git and GitHub
What is the difference between Git and GitHub?
Git is a version control system that lets you manage and keep track of your source code history.
GitHub is a cloud-based hosting service that lets you manage Git repositories

---

## Slide 3

Remember
Git diff: shows the changes between working directory and staging area.
Git  status: shows the overview of the current state of working directories and index.
Git show: displays detailed information about a specific commit, including the commit message and the changes made in that commit..
Staging area: location contains the list of files that will be included in the next commit
Repository: location contains the commit history of a project

---

## Slide 4

Remember: The multiple states of files in a Git repository

---

## Slide 5

Introduction
What if we tried something ambitious and it broke everything that was working earlier?
This problem is solved by the use of branches in Git.

---

## Slide 6

What Are Branches?
Creating a new branch in a project essentially means creating a new copy of that project.
You can experiment with this copy without affecting the original.
So if the experiment fails, you can just abandon it and return to the original—the master branch.
But if the experiment is successful, Git makes it easy to incorporate the experimental elements into the master.
And if, at a later stage, you change your mind, you can easily revert back to the state of the project before this merge.

---

## Slide 7

What Are Branches?
So a branch in Git is an independent path of development.
You can create new commits in a branch while not affecting other branches.
This ease of working with branches is one of the best features of Git. (Although other version control options like CVS had this branching option, the experience of merging branches on CVS was a very tedious one. If you’ve had experience with branches in other version control systems, be assured that working with branches in Git is quite different.)

---

## Slide 8

What Are Branches?
In Git, you find yourself in the master branch by default.
The name “master” doesn’t imply that it’s superior in any way.
It’s just the convention to call it that.
You might argue that, with the ability to go back to any commit, there’s no need for branches.

---

## Slide 9

What Are Branches?
However, imagine a situation where you need to show your work to your superior, while also working on a new, cool feature that’s not a part of your completed work.
As branching is used to separate different ideas, it makes the code in your repository easy to understand.
Further, branching enables you to keep only the important commits in the master branch or the main branch.

---

## Slide 10

What Are Branches?
Branches give you the ability to work on multiple things at the same time, without them interfering with each other.
Let’s say you submit feature 1 for review, but your supervisor needs some time before reviewing it.
Meanwhile, you need to work on feature 2.
In this scenario, branches come into play. If you work on your new idea on a separate branch, you can always switch back to your earlier branch to return the repository to its previous state, which doesn’t contain any code related to your idea.
Further, imagine your team suddenly discovers a bug in your project and you urgently need to fix it.
A new branch would have to be created for this fix and merged with all existing branches once it’s fixed.

---

## Slide 11

What Are Branches?
Let’s now start working with branches in Git.
A branch is a sequence of commits that has name (which is a branch name)
To see the list of branches and the current branch you’re working on, run the following command:
git branch

---

## Slide 12

What Are Branches?
Cloning is the process of creating a local copy of a repository from a different source.
If you’ve cloned your repository or set a remote, you can see the remote branches too. Just postfix -a to the command above:
$ git branch
* master
$ git branch -a
* master
remotes/origin/HEAD -> origin/master
remotes/origin/another_feature
remotes/origin/master
remotes/origin/new_feature
As shown above, the branches that start with “remotes” signify that they’re on a remote.
In our case, we can see the various branches that are present in the origin remote.

---

## Slide 13

Create a Branch
There are various ways of creating a branch in Git.
To create a new branch and stay in your current branch, run the following:
git branch test_branch
Here, test_branch is the name of the created branch.
However, on running git branch, it seems that the active branch is still the master branch.
To change the active branch, we can run the checkout command:
$ git checkout test_branch
$ git branch
git branch
master
* test_branch

---

## Slide 14

Create a Branch
You can also combine the two commands above and thereby create and checkout to a new branch in a single command by postfixing -b to the checkout command:
$ git checkout -b new_test_branch
Switched to a new branch 'new_test_branch'
$ git branch
master
* new_test_branch
test_branch

---

## Slide 15

Create a Branch
The branches we’ve just created are based on the latest commit of the current active branch—which in our case is master.
If you notice an unwanted change or error in the latest commit and would like to explore an earlier version of the repository, you can create a branch from an older commit.

---

## Slide 16

Create a Branch
To create a branch (say old_commit_branch) based on an older commit—such as cafb55d—you can run the following command:

---

## Slide 17

Create a Branch
To create a branch (say test) based on an older commit—such as cf4b234—you can run the following command:
git checkout -b test cf4b234
git checkout -b test

---

## Slide 18

Create a Branch
The --oneline option shows a compact form of the Git history, with one line for each commit.
To rename the current branch to renamed_branch, run the following command:
git branch -m renamed_branch

---

## Slide 19

Delete a Branch
To delete a branch, run the following command:
git branch -D new_test_branch
The -D option used above deletes a branch even if it hasn’t been synchronized with a remote branch.
This means that, if you have commits in your current branch that haven’t been pushed yet, -D will still delete your branch without providing any warning.

---

## Slide 20

Delete a Branch
To ensure you don’t lose data, you can postfix -d as an alternative to -D. -d only deletes a branch if it’s been synchronized with a remote branch.
Since our branches haven’t been synced yet, this is what happens if we postfix -d:
As you can see, Git gives you a warning and aborts the operation, as the data hasn’t been merged with a branch yet.

---

## Slide 21

Branches and HEAD
Now that we’ve had a chance to experiment with the basics of branching, let’s spend a little time discussing how branches work in Git, and also introduce an important concept: HEAD.
As mentioned above, a branch is just a link between different commits, or a pathway through the commits.
The HEAD of a branch points to the latest commit in the branch.
In other words, it refers to the tip of a branch.

---

## Slide 22

Branches and HEAD
A branch is essentially a pointer to a commit, which has a parent commit, a grandparent commit, and so on.
This chain of commits forms the pathway                           I mentioned above.
How, then, do you link a branch and HEAD? Well, HEAD and the tip of the current branch point to the same commit.
The following diagram illustrates this idea.

---

## Slide 23

Branches and HEAD
Add a new commit:

---

## Slide 24

Branches and HEAD
Change branch:

---

## Slide 25

Branches and HEAD
Add another commit:

---

## Slide 26

Branches and HEAD
As shown in previous figures, BRANCH_ONE initially is the active branch and HEAD points to commit C.
Commit A is the base commit and doesn’t have any parent commit, so the commits in BRANCH_ONE in reverse chronological order (which also forms the pathway I’ve talked about) are C → B → A.
The commits in BRANCH_TWO are E → D → B → A.

---

## Slide 27

Branches and HEAD
The HEAD points to the latest commit of the active BRANCH_ONE, which is commit C.
When we add a commit, it’s added to the active branch.
After the commit, BRANCH_ONE points to F, and the branch follows F → C → B → A, whereas BRANCH_TWO remains the same. HEAD now points to commit F.
Similarly, the changes when we add yet another commit are demonstrated in the figure.

---

## Slide 28

Advanced Branching: Merging Branches
As mentioned earlier, one of Git’s biggest advantages is that, compared to Subversion, merging branches is especially easy.
For instance, it’s difficult to store linkages between branches and the master branch (called trunk) in Subversion.
Working on a branch for a long time makes it really difficult to go back and merge with the trunk, as it requires the developer to figure out where to merge.
All of these issues are fixed in Git.
Let’s now look at how branching works in Git.

---

## Slide 29

Advanced Branching: Merging Branches
We’ll create two new branches—new_feature and another_feature—and add a few dummy commits.
Checking the history in each branch shows us that the branch another_feature is ahead by one commit, as shown below:

---

## Slide 30

Advanced Branching: Merging Branches
This situation is illustrated in figure below.
Each circle represents a commit, and the branch name points to its HEAD (the tip of the branch).

---

## Slide 31

Advanced Branching: Merging Branches
To merge new_feature with master, run the following (after first making sure the master branch is active):
git checkout master
git merge new_feature
The result is illustrated in figure below.

---

## Slide 32

Advanced Branching: Merging Branches
To merge another_feature with new_feature, just run the following (making sure that the branch new_feature is active):
git checkout new_feature
git merge another_feature
The result is illustrated in figure below.

---

## Slide 33

Advanced Branching: Merging Branches
This merge happened without any “conflicts”.
The simple reason for that is that no new commits had been added to branch new_feature as compared to the branch another_feature.
Conflicts in Git happen when the same file has been modified in non-common commits in both branches.
Git raises a conflict to make sure you don’t lose any data.

---

## Slide 34

Advanced Branching: Merging Branches
I mentioned earlier that branches can be visualized by just a simple pathway through commits.
When we merge branches and there are no conflicts, such as above, only the branch pathway is changed and the HEAD of the branch is updated.
This is called the fast-forward type of merge.

---

## Slide 35

Advanced Branching: Merging Branches
The alternate way of merging branches is the no-fast forward merge, by post-fixing --no-ff to the merge command.
In this way, a new commit is created on the base branch with the changes from the other branch.
You’re also asked to specify a commit message:
git checkout master
git merge --no-ff new_feature

---

## Slide 36

Advanced Branching: Merging Branches
In the example above, the former (merging new_feature with master) was a fast-forward merge, whereas the latter was a no fast-forward merge with a merge commit.
While the fast-forward style of merges is default, it’s generally a good idea to go for the no-fast-forward method for merges into the master branch.
In the long run, a new commit that identifies a new feature merge might be beneficial, as it logically separates the part of the code that’s responsible for the new feature into a commit.

---

## Slide 37

What is the difference between fast-forward and no-fast-forward merge?
In fast-forward merge, when we merge branches and there are no conflicts, only the branch pathway is changed and the HEAD of the branch is updated.
In no-fast-forward merge a new commit is created on the base branch with the changes from the other branch.

---

## Slide 38

What Have You Learned?
In this chapter, we discussed the following characteristics about branches in Git:
what branches are in Git
how to create new branches from existing branches
the process of merging branches, and how Git’s history is affected

---

# Chapter 5: Git Workflows


## Slide 1

Chapter 5 Git Workflows
Full Stack Web Developer
FWDN 232: Web Developer Tools
Based on slides accompanying the book
Jump Start Git, Second Edition 2020
by Shaumik Daityari

---

## Slide 2

Introduction
So far, we’ve covered the basics of Git and how to use them as part of a team.
But teams differ in the way they utilize Git in their projects.
A Git workflow is a set of guidelines that a team should follow to manage a project.
A workflow generally provides guidelines on the following items:
the architecture of the project.
how contributions are made to the project.
how the work of others is merged into the project.

---

## Slide 3

Introduction
Git’s flexibility allows you to set up diverse guidelines for your project.
This can potentially lead to a large number of workflows.
How do you ensure that team members follow these guidelines?
It may be a good idea to follow a specific, well-defined workflow.

---

## Slide 4

Introduction
Workflows represent broad guidelines for using Git in your project, and that developers often make minor changes to these guidelines for their convenience.
When you’re assessing a workflow, make sure you ask the following questions:
How difficult is it for a new team member to get started?
How much effort goes into reverting the status of the repository after an unwanted change?
Does the workflow scale up well to your team size growth projections?
As each workflow is described, the discussion will be structured around these items.

---

## Slide 5

Git Workflows
The Centralized Workflow
The Feature-branch Workflow
The Gitflow Workflow
The Forking Workflow

---

## Slide 6

The Centralized Workflow

---

## Slide 7

Features
While Git is a distributed version control system, it’s still possible to implement a centralized workflow, inspired by centralized version control systems like Subversion.
A centralized workflow is the simplest of Git workflows, in which just a single branch (typically the master branch) is used for all operations.
It’s called a “centralized” workflow because a single copy of the repository is treated as the main copy, into which every developer syncs their changes.
The centralized workflow is also called the “trunk” workflow, as subversion’s master branch is called trunk.
For this workflow to work seamlessly, you need to give every team member access to your master branch.
The central repository can be on a local server at a location every developer can access, or it can be hosted on a central platform like GitHub or Bitbucket.

---

## Slide 8

New Team Member Orientation
If you’re a new team member, you start by cloning the central repository.
All you need to do is make changes to your master branch and push it to the central repository.
If someone has updated the master since you last updated your local branch, you’re prompted to merge the changes first and then push them.

---

## Slide 9

Pros and Cons
The biggest advantage of this workflow is its simplicity.
The centralized workflow doesn’t use the branching feature of Git.
Beginners often find the branching feature of Git to be the most difficult to understand, so the simplicity of this workflow works best for beginners.
Developers who are familiar with Subversion and new to Git also find this workflow very intuitive.
It’s also ideal for smaller teams that require minimal code review before a merge.
If you’re managing a personal project, the centralized workflow is an intuitive choice as well.

---

## Slide 10

Pros and Cons
On the other hand, the centralized workflow gets tedious with an increase in team size.
Managing changes in code is a challenge if you have multiple people working on the same branch at the same time.
Finally, giving all team members access to the master branch may not be a good idea in a large team.
A single error, if introduced in the codebase, can corrupt the whole repository.
No one can really make changes to the codebase until it’s fixed.
Therefore, a more robust workflow is needed as your team grows in size.

---

## Slide 11

Who Should Use the Centralized Workflow
The simplicity of the centralized workflow makes it perfect for two types of users.
If you’re new to Git and your team is exploring the use of version control in your projects, you should start with the centralized workflow.
Secondly, if you use Git to manage a personal project, the centralized workflow is ideal.
For instance, if you’re a student who manages academic assignments, or an author managing your texts, the centralized workflow fits into your needs perfectly.

---

## Slide 12

The Feature-branch WorkflowFeatures
Because the centralized workflow doesn’t utilize the branching features of Git, the next logical step up from that is to introduce branches for specific changes in your codebase.
This results in what’s known as the “featurebranch” workflow.
The feature-branch workflow follows the concept of feature development in separate branches, without affecting the master branch.
You can either merge or rebase the feature branch into the master, as shown above.

---

## Slide 13

New Team Member Orientation
You must maintain a repository at a central location in the feature-branch workflow, with read access to the master branch to all developers.
A new developer must first clone the master branch and create a new local branch for every feature they start.
While the definition of a feature differs from project to project, it’s a good idea to logically separate each “feature” before starting development on it.
When a feature is ready, a developer should request the core developers to pull changes from this feature branch to the master of the core.
This initiates the code review, which concludes with the merge of the feature into the master.

---

## Slide 14

New Team Member Orientation
The separation of feature development from the codebase allows for a detailed code review process before merging into the main codebase.
This allows the core developers to comment on proposed changes in a review and to request further action before merging them into the main codebase.
Code reviews are interactive and easy if you’re using a cloud-based solution to host your central repository, allowing feature-rich discussions before merging the code into the main repository.

---

## Slide 15

Pros and Cons
Interestingly, a consequence of this workflow is that a developer must never directly commit to the local master branch.
When their feature is accepted into the core repository, they should pull changes from the core master to the local master to keep it up to date.
The departure from the centralized workflow makes it easy for developers to work on multiple features, while keeping the core codebase operational.
At the same time, any critical bug fixes are directly committed to the master branch, and pulled into the feature branches being worked on.

---

## Slide 16

Pros and Cons
As the core developers have a final say before a merge into the main codebase, you can selectively give write access to your master branch, thus making the process secure.
An open-source project must follow at least a feature-branch workflow to ensure code reviews happen before code merges from contributors.
Finally, this workflow gives you more control over your code, and therefore solves the issues of scaling up.

---

## Slide 17

Who Should Use the Feature-branch Workflow
The feature-branch workflow provides a key benefit over centralized workflows: the ability to logically manage multiple changes and multiple contributors.
If you initially followed the centralized workflow because your team was small, you may need to switch to the feature-branch workflow as your team grows.
The target of every team project following the centralized workflow should be to eventually migrate to the feature-branch workflow.

---

## Slide 18

Gitflow Workflow
A successful Git branching model » nvie.com

---

## Slide 19

Features
While the feature-branch workflow works well for any project, adding specific roles for different types of branches can further tighten up your development cycle.
The Gitflow workflow was initially tested and popularized by Vincent Driessen at nvie.com.
The core Git concepts involved in the Gitflow workflow remain the same as the feature-branch workflow.

---

## Slide 20

Features
As mentioned, the Gitflow workflow works as an extension of the feature-branch workflow.
A primary issue with the feature-branch workflow is the loose definition of the term “feature”: it could potentially be interpreted differently depending on the developer, culture, or project.
Further, there was no well-defined provision for other tasks such as regular maintenance and bug fixes.
The Gitflow workflow essentially solves this by defining many types of branches and their functions.

---

## Slide 21

Features
There are two core branches in the Gitflow workflow— the master and develop branches.
The develop branch serves as the latest development version of the software, while the master branch contains only the last stable release.
If you want to work on a new feature, you create a feature branch from the develop branch.
Once you’ve finished working on your feature, you request a merge to the develop branch.
As a developer, you’re essentially never directly involved with the master branch, treating the develop branch as a pseudo master.

---

## Slide 22

Features
In addition to a feature branch, the Gitflow workflow also defines a release branch.
All the planned changes, based on your roadmap for what should feature in the next release cycle, go into the release branch.
A release branch is created from the develop branch.
When all the changes for a release are done, it’s merged with the master with a relevant tag attached to it.
Only the core developers get to work on the release branch by choosing which merges should go into it.

---

## Slide 23

Features
Finally, the next type of branch in the Gitflow workflow is the hotfix branch.
Any critical bug that’s identified needs to be fixed immediately, so a hotfix branch is created from the master branch to solve the bug.
Once it’s solved, the hotfix branch is merged with the master and develop branches to ensure the changes are reflected in both of these.

---

## Slide 24

New Team Member Orientation
Because of the concepts involved, the Gitflow workflow is certainly more complex than the feature-branch workflow.
Even so, getting started is arguably not very difficult.
A developer working on just a single feature only needs to be concerned with the develop branch and a corresponding feature branch.
Once the developer’s role in the project grows, they may be introduced to new tasks and given further responsibilities.

---

## Slide 25

Pros and Cons
The Gitflow workflow shares the same advantages as the feature-branch workflow, with the added clarity of handling various scenarios in the software development cycle.
Even if you’re encouraged to adopt this workflow from the start, you may consider moving to it from the feature-branch workflow once your project has matured a bit.

---

## Slide 26

Who Should Use the Gitflow Workflow
The Gitflow workflow allows a team to manage a number of scenarios effectively.
As the Gitflow workflow is an extension of the feature-branch workflow, the transition is easy to handle.
Imagine that you have a project with a good mix of new and experienced developers.
The end product also has a significant number of users, who may be using multiple versions of it.
Such a project demands the use of the Gitflow workflow to effectively handle any situation that may come up.
Popular open-source projects often use the Gitflow workflow.

---

## Slide 27

Forking Workflow

---

## Slide 28

Features
The forking workflow is an implementation of the feature-branch workflow—in the cloud.
It introduces an extra layer between the central repository of the organization and the local repository of a developer— known as a “fork”.
A fork is a developer’s personal copy of the central repository within the cloud.
When you use a cloud-based Git solution, a developer clones their own fork from the cloud.
Any changes they make on the local repository are pushed to this fork.
To merge the code into the main repository, the developer creates a pull request from the fork to the main repository.
This pull request initiates a code review, which the administrators of the repository assess before merging into the main repository.

---

## Slide 29

Features

---

## Slide 30

New Team Member Orientation
A new member first creates a fork of the main repository on the cloud, and then clones this fork to a local machine.
Changes are made to a new feature branch and pushed to the developer’s fork on the cloud.
Next, the developer creates a pull request from a feature branch of the fork to a corresponding branch in the main repository.
This initiates a review and conversation with the core developers to get the changes merged into the codebase.
The origin remote of the local repository typically points to the fork, and the upstream remote points to the central repository.

---

## Slide 31

Pros and Cons
Code management and review through pull requests is much easier when it’s done on the cloud with the help of the web GUI of cloud hosts.
Multiple developers can also get involved in the review process through a pull request.
At the same time, it may be overwhelming for a new member to work around Git’s features and related cloud concepts towards the beginning of their project tenure.

---

## Slide 32

Who Should Use the Forking Workflow
Anyone using the cloud for their Git repositories should implement the forking workflow!
This workflow serves as an additional layer to any other workflow.
Thus, it allows you to incorporate features of other workflows without any issues.
If your project is open source, you shouldn’t have any issue with hosting the code on the cloud.
However, if you don’t want the code of your project to be publicly available, you can use private repositories on the cloud.

---

## Slide 33

Who Should Use the Forking Workflow
Further, if your code is highly sensitive and you can’t afford to have it on a public cloud, you can try the enterprise solutions of GitHub or Bitbucket, which allow you to host your code on your own servers.

---

## Slide 34

What Have You Learned?
In this chapter, we covered:
what workflows are
the centralized workflow
the feature-branch workflow
the Gitflow workflow
the forking workflow

---

# Chapter 6: Correcting Errors While Working with Git


## Slide 1

Chapter 6 Correcting Errors While Working with Git
Full Stack Web Developer
FWDN 232: Web Developer Tools
Based on slides accompanying the book
Jump Start Git, Second Edition 2020
by Shaumik Daityari

---

## Slide 2

Introduction- Amending Errors in the Git Workflow
Git makes it possible to correct mistakes at each stage of a project—which is yet another reason why it’s so popular with developers.
With Git, it’s fairly easy to undo changes you’ve made. In this lecture, we’ll look at three examples:
Undoing a stage operation;
Undoing a commit, by reverting back to an older commit;
Undoing a push, by rewriting the history of a remote repository.

---

## Slide 3

Git
Life cycle

---

## Slide 4

Git
Stages
Working Directory

---

## Slide 5

Git command cycle

---

## Slide 6

UNDO GIT ADD
The git add command either tells Git to track an untracked file, or to stage the changes in a tracked file for a commit.
If you’ve just asked Git to track a new file that you’ve created but not yet committed—let’s call it mistake_file—you can undo the operation by running the following command:
git rm --cached mistake_file
Here, rm stands for remove (just like the regular terminal command rm).
When we postfix --cached, we ask Git to untrack the file, but let it remain in the file system.

---

## Slide 7

UNDO GIT ADD
You can check the status of the repository to confirm that the file is untracked again:
The command git rm --cached can also be used to remove a file from the repository.
Once a file has been removed, you need to commit the changes for them to take effect.

---

## Slide 8

UNDO GIT ADD
Let’s say you make changes to a tracked file (myfile2), and then run git add to stage it for commit.
Then you realize you made a mistake before committing it. You can run the following command to unstage the changes:

---

## Slide 9

UNDO GIT ADD
This command resets a file to the state where the HEAD, or the last commit, points to.
This is the same as “unstaging” the changes in a file.
Once you’ve unstaged the changes in a file, you can undo the changes you made in the file as well, reverting it back to the state during the last commit.
This is where the following command comes in:
We’ve seen the checkout command used previously during the process of branching.
It’s also used to restore any unstaged changes in a file, as seen above.

---

## Slide 10

UNDO GIT COMMIT
If you’ve already committed your changes and then realize your mistake, there’s a way to undo that too.
Let’s make an unnecessary commit and try to revert back to the original.
Run the following command to see Git do some magic:
The --soft option undoes a commit, but it lets the changes you made in that commit remain staged for you to review.
HEAD~1 means that you want to go back one commit from where your current HEAD points (which is the last commit).

---

## Slide 11

UNDO GIT COMMIT
The second option here is postfixing the --hard option to permanently undo commits.
It’s generally advised that you avoid using the --hard option—unless you’re absolutely sure you want to do away with the commits.
A third option of reset is --mixed, which is also the default option.
In this option, the commit is reverted, and the changes are unstaged.
The process of committing involves three steps: making changes in a file, staging it for a commit, and performing a commit operation.
The --soft option takes us back to just before the commit, when the changes are staged.
The --mixed option takes us back to just before the staging of the files, where the files have just been changed.
The - -hard option takes us to a state even before you changed the files.

---

## Slide 12

UNDO GIT COMMIT
There’s yet another Git command that could help you in case you’ve committed changes by mistake.
This is the revert command.
The reset command changes the history of the project, but revert undoes the changes made by the faulty commit by creating a new commit that reverses the changes.
The following figure shows the difference between revert and reset.

---

## Slide 13

UNDO GIT COMMIT
The following code shows how to go back one commit using revert.
You can also modify the commit message for the commit that reverses the changes of the unwanted commits:

---

## Slide 14

UNDO GIT COMMIT
You can change the commit message of the last commit by running the following command:
The --amend -m option changes the commit message of the last commit. Notice that the hash changes too, effectively rewriting the history.

---

## Slide 15

UNDO GIT PUSH
In case you’ve also pushed your changes to a remote, it’s possible to revert changes in the push too.
The simplest way is to go for a revert and push the new commit that undoes the changes:

---

## Slide 16

UNDO GIT PUSH
However, if you also want the other commit(s) to vanish from the remote repository, you first need to go for a reset command—deleting the unwanted commit—and then push the changes to the remote.
If you perform a normal git push, the push will be rejected, because the origin HEAD is at a more advanced position than your local branch.
Therefore, you need to force the change with a postfix—-f—which forces the push on the remote origin:

---

## Slide 17

Debugging Tools
The scenarios we’ve discussed so far help you to undo changes in Git.
They’ve dealt with mistakes you’ve committed in the near past and want to correct.
Now we’ll look at dealing with bugs introduced by you or others in the past.
This will involve exploring tools in Git that help in the process of debugging.
These tools are required when you’re working on a relatively large codebase with a large number of contributors.

---

## Slide 18

Debugging Tools
You may or may not know the location of the bug.
If you know which file or set of files is the source of the bug, you can debug with git blame.
If you don’t know the source of the bug, you can debug with git bisect.
If you’ve written unit tests, you can also automate the process of debugging.
So let’s explore the different ways of debugging your code in Git.

---

## Slide 19

GIT BLAME
Running the git blame command on a file gives you detailed information about each line in the file.
git blame lists the commits that introduced changes in a file, along with basic information about the commit, like the commit hash, author and date.
git blame is usually used when you know which file is causing a bug.

---

## Slide 20

GIT BLAME
Let’s see how it works:

---

## Slide 21

GIT BLAME
As you can see in the code above, the command git blame displays each line of the file.
These lines are prepended with information in the following order: the hash of the commit that added the line, and the commit author, date, time and time zone.
In this scenario, as you already know where the faulty code is, you can just display the details of the required commit to find out more about the bug that was created.
Let’s assume it was committed f934591c that introduced the bug.

---

## Slide 22

GIT BLAME
You should therefore run the following:

---

## Slide 23

GIT BLAME
The git show commands shows the author of the commit, the date of the commit and the changes that constitutes the commit.
Once you’ve figured out what caused the error, you can go ahead and fix it in your repository and then commit the changes.
Normally, though, you’ll most likely have no idea what caused the bug.
So we need to explore some more debugging tools.

---

## Slide 24

GIT BISECT
There’s probably no better way to search for a bug than with bisect.
Even if you have a thousand commits to check, bisect can help you do it in just a few steps.
Let’s assume you have no idea what’s causing an error.
However, you do know that, at a certain point in time— after a particular commit—the bug wasn’t present in your code.
Git’s bisect helps you quickly traverse between these stages to identify the commit that introduced the bug.
bisect essentially performs a binary search through these commits.

---

## Slide 25

GIT BISECT
To start the process, you select a “good” commit from the history, where you know the bug wasn’t present, and a “bad” commit (which is usually the latest commit).
Git then changes the state of your repository to an intermediate commit and asks you if the bug is present there.
You search for the bug and assign that commit as “good” or “bad”.
This process continues until Git finds the faulty commit.
Since a binary search algorithm is used, the number of steps required is a logarithmic value of the number of commits in between the initial “good” and “bad” commits.

---

## Slide 26

GIT BISECT
An example will help explain how git bisect works.
Let’s create a file in our repository—sum.py—containing a function that adds two numbers in Python.
The contents of the file are as follows:

---

## Slide 27

GIT BISECT
I’ve intentionally added the second block of code to print the response of the function to two dummy values.
We can run the program with the following: python sum.py
After adding a few more commits, let’s change the file sum.py to introduce an error:

---

## Slide 28

GIT BISECT
Running the program now, we can see that the result is not 12, but 7. Let’s now demonstrate the use of git bisect.
To decide the good and bad commits, we need to have a look at the commit history:

---

## Slide 29

GIT BISECT
As is evident from the history, the latest commit 083e7ee (at the top) is “bad”, whereas the commit two positions before we introduced the bug—7d1b1ec—is “good”.
To better identify the bug, I’ve mentioned in the commit message which commit introduced the error.
We must now undertake the following steps to find out the bug:
start the Git bisect wizard
select a good commit
select a bad commit
assign commits as good or bad as the wizard takes you through the commits
end the Git bisect wizard

---

## Slide 30

GIT BISECT
Let’s go ahead and start the Git bisect wizard: git bisect start
This takes Git into a binary search mode.
Next, we need to tell Git the last known commit where the bug was absent, which in our case is 7d1b1ec:
git bisect good 7d1b1ec
Now assign the latest commit as the bad one:

---

## Slide 31

GIT BISECT
To combine the last three commands (start, good, and bad) into one, you may instead start the wizard with the following command:
git bisect start 083e7ee 7d1b1ec
As soon as you assign the good and bad commits, git bisect starts its work and takes the state of your repository to an intermediate commit.
At this point, you’re shown the commit hash and commit message, and you’re asked whether or not the bug is present in that commit.

---

## Slide 32

GIT BISECT
In our situation, we just run the file sum.py to find out if the bug is present.
For the commit b00caea, we see that the output is 12.
So the bug is absent, and we mark it as good:
git bisect good
In the next step, we’re asked whether commit 49a6bec is good.
We check the commit by running sum.py again and assign it as bad:
git bisect bad

---

## Slide 33

GIT BISECT
Once we’re done with this, Git shows us the faulty commit as 5199b4e, which is also evident from the commit message I added when I introduced the error:
Once you’ve found your faulty commit, you can exit the wizard by running the following:
git bisect reset

---

## Slide 34

GIT BISECT
In this case, the use of git bisect was overkill and not necessary (as we knew the source of the bug already).
However, in real life there are often bugs that are difficult to trace back to a file, but the bug is visible only in the way your code functions.
For instance, you have a complex algorithm to find out the popularity of a person in social media and you find out that the results aren’t right.
In such cases, you employ the bisect tool to find out which commit first introduced the error to rectify it.

---

## Slide 35

Automated Bisect With Unit Tests
We’ve just seen how bisect helps you find the commit that introduced a bug.
However, this process is tedious, as you need to check for the bug at every single step of the wizard.
The easiest way to automate the process is to write unit tests.
You can also write custom scripts that test the required functionalities.
In our case, we’ll write a custom file—test_sum.py—that tests the functionality of the function in sum.py.
This file is just for demonstrating the functionality of bisect.

---

## Slide 36

Automated Bisect With Unit Tests

---

## Slide 37

Automated Bisect With Unit Tests
Running the file test_sum.py runs the tests specified in it:
python test_sum.py
Running it on our current code shows errors.
Let’s start the bisect process again:
git bisect start 083e7ee 7d1b1ec
We next inform Git about the command that runs the tests:
git bisect run python test_sum.py

---

## Slide 38

Automated Bisect With Unit Tests
If you have a custom command to run your tests, replace python test_sum.py with your command.
On informing Git about the command that tests our code, the wizard runs it against the remaining commits and figures out which commit introduced the error.
Once the bug has been identified, reset the wizard:
git bisect reset
Once you’ve found out which commit introduced the error, you can look carefully into it to see the faulty code.
Once you identify that, you can fix it and commit it to the repository.

---

## Slide 39

What Have You Learned?
In this chapter, we looked at how Git lets you undo mistakes:
undo git add
undo git commit
undo git push
We’ve also looked at two debugging tools, which help you find bugs in your Git workflow:
blame
bisect

---

# Chapter 7: Unlocking Git's Full Potential


## Slide 1

Chapter 7Unlocking Git’s Full Potential
Full Stack Web Developer
FWDN 232: Web Developer Tools

---

## Slide 2

Advanced Use of log
We saw earlier that you can view the history of your project in Git using the log command.
However, in busy repositories that handle hundreds to thousands of commits each day, a long list of commits isn’t going to be useful unless you know how to navigate through them.
The manual entry for the log command shows the different options that can be postfixed to this command to get a desired output.
We’ll look at a few tweaks to the log command, which could prove useful in such situations.
Since our dummyدمية project doesn’t have a considerable number of commits, we’re going to use the open-source repository of an e-learning management system—ATutor —to explore the different capabilities of the log command.

---

## Slide 3

Short Version
In general, the log command shows a list of commits in the active branch, each with the commit hash, author, date and commit message.
Depending on your screen size and text size of the output, you get around five to ten commit details in a screen.
Each commit occupies يحتل four to five lines on the screen, or even more if the size of the commit message is large:

---

## Slide 4

Short Version
In case you want to have a quick glance at the list of commits, you can format the output to show only the commit hashes and single-line messages, using the --oneline option:
git log --oneline
A single commit is displayed on each line, and thus many more commits fit onto the screen at once:

---

## Slide 5

Branches and History
The log command can also be used to view the workflow and commits in branches other than the current active branch.
If you want to view the commits in all branches, just postfix --all to the command:
git log --all

---

## Slide 6

Branches and History
This doesn’t look very appealing, as you have no idea which commit came from which branch.
You can add the --decorate option to view which branch each commit belongs to. It also shows the remote branches.
Note that I’ve used --oneline to accommodate more commits:

---

## Slide 7

Branches and History
The --graph option shows you the commit history, with a graphical representation interconnecting the links between commits of different branches (if any).
Combining it with --all shows you how the different branches in your repository have progressed:

---

## Slide 8

Branches and History
To understand this concept better, let’s take a look at the output again.
8dd76fc is the first commit of this repository, which appears at the bottom of the output.
As you traverse upwards from the bottom of the figure, notice that commit 49ed357 diverges from the master branch into a new branch, another_feature.
Following the path of another_feature shows us that commit 5ef655a is the last commit in the branch, before it merges back with master at commit cafb55d.

---

## Slide 9

Filter Commits
When you view the history, you’re shown all the commits in the history’s branch.
However, if you wish to view only a few of the latest commits, postfix -n, followed by the number of commits you want to see:
git log -n 2

---

## Slide 10

Filter Commits
Alternatively, you can use the following command as well, which serves as a shortcut for the previous command:

---

## Slide 11

Filter Commits
You can also view the commits in a specified time range.
This can be achieved by postfixing --after and --before to the log command:

---

## Slide 12

Filter Commits
--after and --before can be replaced by --since and --until.
For instance, the following pairs of commands will produce the same results:

---

## Slide 13

Trace Changes in a Single File
If you want to check the commits that resulted in changes in a single file, you can use the --follow option:
Tracing the changes in a file may be useful while debugging, especially if you want to see if anyone has changed a particular file since a certain time.
It also helps you to check if parts of a file were removed in previous commits.

---

## Slide 14

Track Your Peers
The shortlog is a command that shows the authors who’ve contributed to the repository, their commits and commit messages.
You can use this command if you’re interested in knowing the contributions of different developers.

---

## Slide 15

Track Your Peers
The output of this command is sorted by name, and you can postfix -n to sort it by the number of commits:
Notice that there are two different authors with the same name, as the second set of commits was created on GitHub.

---

## Slide 16

Track Your Peers
You can also view the commits by a single author by using the --author option:
git log --author='Shaumik'
You only need to type just enough of the name for Git to identify the author.
If there are two authors matching the string you’ve provided, both their commits will be displayed.
If there are two authors with the same name committing to the same repository, Git differentiates them through other details—such as their email address, or the system the commit was generated from.

---

## Slide 17

Search in Commit Messages
Imagine a situation where you’d like to know when a certain feature was introduced.
Searching for a commit through its commit message would be useful.
Git enables searching in the commit messages by using the --grep option.
For instance, if you want to search for the word “test” in your commit history, you should use the following command:

---

## Slide 18

Search in Commit Messages
In the search term, you can also use regular expressions to search in commit messages.
This would be useful in a situation where, for example, you’d like to search for all commits that refer to a certain feature name.
You can also use regular expressions while using the grep command.

---

## Slide 19

Tagging in Git
You’ve most likely noticed that software updates normally come with a version number.
For instance, as of March 2020, the version number of popular screen recording software ScreenFlow is 9.0.0, which was released in November of 2019.
Git allows you to associate these version numbers with specific milestone commits in your repositories, by attaching labels to these commits.
The labels are called tags. Let’s again visit the ATutor repository to check its use of tags.

---

## Slide 20

Tagging in Git
Tagging can be used to easily find any commit that’s important to a developer.
Tags can also be used to mark a breakthrough after debugging, or a milestone in development.
They can also be used to mark changes being made without creating an extra branch.
Tags provide an easy way to go back in branch history if something didn’t work out right.

---

## Slide 21

Tagging in Git
To list the tags in alphabetical order, run git tag, which results in the following output:

---

## Slide 22

Tagging in Git
There are two types of tags—“lightweight” and “annotated”. Lightweight tags contain only the tag name and point to a commit.
Annotated tags contain the tag name, information about the tagger, and a message associated with the tag.
Annotated tags are generally preferred in organizations because they contain information about the tagger when the tag was created, and why.
Lightweight tags are handy for tagging special commits when you’re working on your personal projects.

---

## Slide 23

Tagging in Git
To view the details of a tag—say Atutor_1.4.1—run the following command:
git show Atutor_1.4.1
You can create a lightweight tag latest_commit, associated with the latest commit, by running the following:
git tag latest_commit

---

## Slide 24

Tagging in Git
To create an annotated tag, you need to postfix -a for annotated and -m for an associated message:

---

## Slide 25

Tagging in Git
You can also checkout to a tag Atutor_1.4.1 by creating a new branch version_1_4_1 (just like you checkout to a commit):
git checkout -b version_1_4_1 Atutor_1.4.1
When you push your code, your tags aren’t pushed to the remote.
If you specifically want to push newly created tags to the remote origin, you can run the following:
git push origin --tags
If you specifically want to push a tag to a remote, run the following:
git push origin Atutor_1.4.1

---

## Slide 26

Refs and reflog
Now that we’ve explored the log command in detail, let’s now have a look at something new: refs.
You already know that a commit is identified by its hash—a long string unique to a commit.
A ref, short for a “reference”, is a way of referencing a commit.
In other words, the hash is a name, whereas a ref is a pointer.
Refs are stored internally in Git, and we won’t go into how Git treats refs.
We will, however, use the reflog command to utilize refs.
We’ve discussed what a HEAD in Git points to.
At this point, it’s important to note that HEAD is also a ref. There are other such special refs like ORIG_HEAD, MERGE_HEAD and FETCH_HEAD.

---

## Slide 27

Refs and reflog
This brings us to the reflog. It’s a “log of refs”.
That is, any change you make in Git is recorded and accessible via the reflog command.
For instance, if you create a commit, checkout to a new branch, merge two branches, pull, push or even make a failed merge, reflog records them all:

---

## Slide 28

Refs and reflog
The reflog command stores the records for each action you perform in your repository.
When you push the changes, this data isn’t synced with the server.
Using the reflog command is necessary if you want to review changes to your local repository.
It could also be used to recover lost commits.

---

## Slide 29

Checking for Lost Commits
We’ve just seen how reflog can help you search for commits that might be lost because of the use of a hard reset.
However, it’s difficult to search specifically for lost commits in a repository with a huge history.
A commit is lost when it’s not a part of any branch.
The log command fails to search and show lost commits.
One way of losing commits from your branch history is to do a hard reset.
However, deleting a branch without merging it with a different one can also lead to commits that are recorded by Git but not present anywhere in any of your branches.

---

## Slide 30

Checking for Lost Commits
You can search for commits that aren’t a part of any branch by using the fsck (file system check) command:
If you want to recover a lost commit—say c9067—from the list to your current branch, you can run the following:
git merge c9067

---

## Slide 31

Rebase
We saw earlier how merge works: it creates loops in the commit history of a project.
These loops don’t really cause any problems for Git, though over time they can make project histories difficult to understand and navigate.
For the central repository of a project, it’s preferable to have a linear history, rather than a bunch of interconnected loops.
In this section, we’ll discuss a merging mechanism— rebase—that avoids loops in the project history.
I mentioned rebase earlier, when I used it with the git pull command.
Quite literally, the process of rebasing is a way of rewriting the history of a branch by moving it to a new “base” commit.

---

## Slide 32

Rebase
If you’re rebasing a master into new feature, the new commits in the master are put before the new commits in new feature that aren’t common to the master.
To do so, run the following command from the new feature branch:
git rebase master
This can also be accomplished by the following:
git merge --rebase master

---

## Slide 33

Rebase

---

## Slide 34

Rebase
One important observation from the diagram is the presence of a linear commit history, which is not present in a merge.
The following figure shows the difference between a merge and a rebase for two branches.

---

## Slide 35

Rebase

---

## Slide 36

Rebase
A rebase operation may lead to conflicts, just like a merge operation.
The process of resolving a conflict is exactly the same as we discussed earlier.
You can use rebase when you’re pulling changes.
It essentially puts the new commits in the master of the remote in your history, and then superimposes your commits on them.
Any conflicts that arise can be fixed easily, because they’ve been raised by your code.
You can rebase with a pull using the following command:
git pull --rebase origin master

---

## Slide 37

Squash Commits Together
When you’re contributing to a codebase by working on a different branch, the code may not be accepted at the first go.
Once changes in your code have been suggested, you create a new commit with the changes.
You may, however, be asked to make more changes and, before you know it, you may have added multiple commits to the pull request.
Since you created the pull request asking for your code to be merged, all of the commits would also get merged.
To "squash" in Git means to combine multiple commits into one. You can do this at any point in time (by using Git's "Interactive Rebase" feature), though it is most often done when merging branches. Please note that there is no such thing as a stand-alone git squash command.

---

## Slide 38

Squash Commits Together
In such a situation, you might have a list of commits, the first of which was an attempt to resolve a bug, whereas the latter were attempts at refactoring the code to follow best coding practices.
The group of commits as a whole signifies a single task that’s been accomplished, and hence, it makes logical sense to package them together as a single commit (rather than merging these multiple commits into the main project history).

---

## Slide 39

https://www.git-tower.com/learn/git/faq/git-squash

---

## Slide 40

Squash Commits Together
This can also be done through the rebase command (essentially rebasing your current branch).
If you want to squash the last two commits, run the following command:
git rebase -i HEAD~2
The HEAD~2 refers to the last two commits in the current branch, and the -i option stands for interactive (which can be replaced by --interactive).
You’re then taken to an interactive screen, where you need to pick the old commit and squash the latest commit.

---

## Slide 41

Squash Commits Together
Git showing a list of commits to squash

---

## Slide 42

Squash Commits Together
You then proceed to provide a commit message:
Git asking for a commit message for the squashed commit

---

## Slide 43

Squash Commits Together
Let’s look at the repository after the squash operation, to make sure the last two commits have been converted into one.
Status of a repository before and after squash

---

## Slide 44

Squash Commits Together
https://www.git-tower.com/learn/git/faq/git-squash

---

## Slide 45

Stash Changes
Imagine a situation where you’re working on a bug or a feature, and many files have been edited since the last commit.
However, you need to switch branches to work on something else, or you need to demonstrate the state of the repository at the last commit to your boss.
You can’t commit your current changes, as they’re not complete yet.
How do you solve this problem?
stash allows you to save the changes you’ve made in your repository and revert back to the state of the last commit.
At a later stage, you can get back your changes if you wish.
To stash uncommitted changes, run the following command: git stash

---

## Slide 46

Stash Changes
You can check the list of stashes in your Git repository by running the following:
In the code above, note the serial numbers associated with each stash, which Git uses to identify it.
The commit hash and message refer to the last commit of the active branch when you stashed the changes.
To apply the changes that were stored in the last stash, you can use the following command:
git stash apply

---

## Slide 47

Stash Changes
To restore an old stash, you need to mention the serial number next to the stash in the list of stashes:
git stash apply stash@{1}
A stash can only be applied if no files have been modified since the last commit.
To apply multiple stashes, you first need to commit the changes from a stash.
Applying a stash may raise a conflict if a file in the stash has since been modified in a commit.

---

## Slide 48

Advanced Use of add
In Chapter 6, “Correcting Errors”, we saw that we can instruct Git to track a new file, or stage changes to a modified tracked file, using the add command.
In this section, we’ll go a step further and see how we can stage only a part of our modifications to the same file.
It’s generally a good idea to associate a commit with a single bug fix or feature, as commits can then be used to separate different logical ideas.
If you’ve solved two bugs by changing parts of the same file and want those changes to appear in different commits, you can do so as follows.

---

## Slide 49

Advanced Use of add
To simplify the process, I’ll add three lines at three different positions in the same file and view the changes that I’ve just added:
git diff

---

## Slide 50

Advanced Use of add
Let’s say I want to add the second line among the three added lines to my commit.
We can start the process with git add.
Note the -p postfix to the add command to initiate this process:

---

## Slide 51

Advanced Use of add
Git has clubbed all the changes together into a “hunk”.
A hunk is a group of changes in a file.
Notice that Git now asks us to enter an option.
These are the options and their uses:
y: stage the hunk
n: don’t stage the hunk
e: edit the hunk
d: exit the process
s: split the hunk

---

## Slide 52

Advanced Use of add
In this case, we want to add only the second line, but because all three lines are a part of the same hunk, we need to split it:

---

## Slide 53

Advanced Use of add
After splitting the larger hunk, we’re provided the first of the three smaller hunks.
We wish to add only the second one.
Therefore, we go to the next one by selecting option n:

---

## Slide 54

Advanced Use of add
Next, we’re asked if we want to stage the second line.
Therefore, we select option y, followed by option n for the third line.
You can run git status to check how the repository looks:

---

## Slide 55

Advanced Use of add
As you can see, the same file shows up in the list of modified files and in files staged for commit.
This means you successfully staged a part of a modified file.
You can proceed to commit your changes now.

---

## Slide 56

Cherry Pick
Let’s say our work is progressing in two branches.
If you want to merge a single commit from one branch into another, merge or rebase won’t suffice.
The cherry-pick command allows you to pick a certain commit from a different branch and merge it into your current branch.
Just like in merging and rebasing, cherry-pick can also result in conflicts, which should be resolved as discussed earlier.

---

## Slide 57

Cherry Pick
The idea of a cherry-pick is illustrated in following figure:

---

## Slide 58

Cherry Pick
To merge a commit 30dc1fa2d from a different branch to your current branch, run the following command:
git cherry-pick 30dc1fa2d

---

## Slide 59

GitHub CLI
While we’ve looked at various advanced Git commands, you may have noticed that you still need to access GitHub’s website to create pull requests or raise issues.
GitHub has an in-built bug tracker where you can create issues.
An issue is a task, enhancement, or a bug in your project.
GitHub has now launched a new CLI tool that allows you to perform GitHub-related operations from the command line.
To use the command-line tool, you need to download and install a GitHub client that enables the use of the gh command.
On Windows, you can download the MSI installer from the releases page.

---

## Slide 60

GitHub CLI
Navigate to a local clone of a GitHub repository, and run a gh command.
The first time you run it, you’re redirected to GitHub on the browser to authenticate the tool:
There are two broad categories of commands that you can run: pull requests (the pr subcommand) and issues (the issue subcommand).
To check the list of pull requests on your browser, run the following command: gh pr list

---

## Slide 61

GitHub CLI
To check the status of pull requests, use the status keyword:

---

## Slide 62

GitHub CLI
To create a new pull request, run the following command:
gh pr create
It creates a pull request from the current active branch to the master branch.
If your local clone is of a fork, the pull request is created on the master branch of the main repository.
After you run the command, you’re asked to enter details of the pull request, like title and body.
You can optionally enter the text of the body in a text editor.

---

## Slide 63

GitHub CLI
Similarly, you can create, list and check the status of issues on a repository using the issue subcommand.
For instance, the following command shows the status of all issues:
gh issue status
While Git in itself is powerful, completing actions on GitHub without leaving the terminal makes the process convenient and more efficient.

---

## Slide 64

What Have You Learned?
In this chapter, we discussed various commands and their uses to make your Git experience easier.
In addition to GitHub CLI, here’s a list of the commands we covered:
log
shortlog
reflog
fsck
rebase
stash
add
cherry-pick
You should try to incorporate these into your daily workflow to gain the most out of them.

---

# Chapter 8: Integrate Git in Your Development Cycle


## Slide 1

Chapter 8Integrate Git in Your Development Cycle
Full Stack Web Developer
FWDN 232: Web Developer Tools

---

## Slide 2

Introduction
In earlier chapters, we looked at various Git concepts, managing a codebase in a team environment, and commonly used Git techniques to make your workflow efficient.
These things help you become better at managing your code with Git, but one thing we haven’t discussed yet is how to integrate Git into your development cycle.
This chapter focuses on using Git to bring efficiency into your entire software development cycle.

---

## Slide 3

Git and DevOps
How did DevOps come into being? Traditionally, there was a clear distinction between teams that were responsible for development, testing, deployment, and maintenance.
While this distribution of functions was based on the skills required, teams realized over the years that inefficiencies were introduced due to the friction between these teams.
This led to the birth of DevOps, a cross between development, operations and QA (quality assurance).
DevOps is a set of guidelines that automates processes in the software development cycle, thus lowering the time to market.
A DevOps engineer oversees the code release cycle and ensures that the process is smooth.

---

## Slide 4

DevOps

---

## Slide 5

Git and DevOps
Though the stages in the DevOps cycle can vary, it generally involves the following seven steps:
Continuous development. This involves planning a roadmap depending on the end user’s requirements and then starting development.
Continuous integration. This involves testing all code on every push, and merging with the main codebase if all tests pass. An additional code-review process may be included.
Continuous testing. This involves testing the application in a live environment to verify the product’s functionality.
Continuous monitoring. In this phase, critical metrics of a product’s output and usage are monitored in order to identify any anomalies.
Continuous feedback. Feedback from earlier stages is used to update the roadmap and proactively include features and bug fixes.
Continuous deployment. This ensures that the availability of the end product isn’t affected by releases.
Continuous operations. The objective of this step is the automation of the release process, which leads to a shorter development cycle.

---

## Slide 6

Git and DevOps
The use of Git is critical in the early stages of the DevOps cycle.
Git ensures proper code management, attribution, and integration with other stages.
Git can trigger a set of processes at the onset of an action, like a code push or a pull request.
Without the use of any version control, it would be difficult to create triggers based on code changes.

---

## Slide 7

Using Git Hooks
While we’ve seen that Git is important to DevOps, this section deals with “Git hooks”, a technique to seamlessly integrate Git with the DevOps cycle.
A Git hook is a custom script that executes when a pre-defined action or event occurs.
Git hooks are scripts that run automatically every time a particular event occurs in a Git repository. They let you customize Git’s internal behavior and trigger customizable actions at key points in the development life cycle.
Git hooks are of two types: client-side and server-side.
A client-side Git hook is reactive to local changes: it happens on actions such as a commit or merge.
A server-side Git hook gets initiated on a network-based action, like a push to a remote.

---

## Slide 8

Using Git Hooks
As Git hooks are executable scripts, there’s no limit to the actions you can perform with them.
The simplest use case of a Git hook is to send an email on every new commit.
You could initiate unit tests to be run on every commit.
You could raise a pull request on every push to a new branch.
Git hooks reside in the .git/hooks directory of your repository.
When you initialize a Git repository, Git populates this directory with sample scripts with the .sample extension.
If you’d like to create a hook, remove the .sample extension from any of them.
Since they’re executed on an action or event, double-check the file permissions to ensure they’re executable.

---

## Slide 9

Using Git Hooks
If you view the contents of any of these files, you’ll notice that they’re Bash scripts with an opening line of #!/bin/sh.
While the sample files are Bash scripts, you can change the first line to change the language of the script.
While local Git hooks generally work around changes (pre-commit, commit-msg, post-commit), server hooks (pre-receive, update, post-update) are mostly centered around updates.

---

## Slide 10

Using Git Hooks
Here’s a list of common hooks and when they’re triggered:
pre-commit: before a commit message is entered
commit-msg: with the commit message (it’s a path to a
temporary file)
post-commit: after a commit process is complete
pre-push: before changes are sent to a remote
post-merge: after a merge is complete
pre-receive: before a push from a client
post-receive: after a push from a client is completed

---

## Slide 11

Using Git Hooks
The most important Git hook is the pre-commit, where you can integrate unit tests:
While using Git hooks provides you with a lot of functionality to integrate with the software development cycle, it may be difficult for the average user to write custom scripts to achieve the objectives.
However, you can utilize continuous integration (CI) tools to achieve this task.

---

## Slide 12

Integrating Travis CI with GitHub
Continuous integration is the second step in the DevOps cycle, and it involves substantial use of Git.
Continuous integration ensures a smooth transition between the code push and beta testing.
It ensures that any new changes to the repository won’t break things.
Travis CI is popular, hosted continuous integration tool for GitHub repositories.
It’s free to use for open-source GitHub projects, with paid plans for commercial projects.
You can only test repositories hosted on GitHub with Travis CI.
However, you can create a workaround by adding submodules to test repositories hosted on other platforms.

---

## Slide 13

Integrating Travis CI with GitHub
Travis CI works like this: on every push to GitHub, the tool essentially clones the repository on a virtual machine on the cloud, installs the requirements on the fly, and runs pre-defined unit tests to determine if the new code breaks the existing functionality of your project.

---

## Slide 14

Getting Started With Travis CI
To integrate Travis CI with your GitHub repository, you need to first create an account on the Travis CI website.
If you log in through your GitHub account, you can skip the additional step of linking GitHub with Travis CI.
After logging in, go to the settings page of your Travis CI account to view the list of public repositories in your connected GitHub account.
Search the repository you’d like to link to Travis CI and select the toggle button next to the repository.

---

## Slide 15

Getting Started With Travis CI

---

## Slide 16

Getting Started With Travis CI
Next, you need to add a configuration file to the root directory of your repository.
Name the configuration file .travis.yml
Here are the minimal settings for your Travis CI configuration file:

---

## Slide 17

Getting Started With Travis CI
First, you instruct Travis CI to test each build on Python and then specify the versions 3.7 and 3,8.
Note that, for each version you specify, a new build will be created and tested, thereby increasing the time to perform the test.
Next, you provide the command to install the dependencies of the repository.
Finally, you provide the command to run the unit tests, against which the push will be evaluated.
After you’ve created the configuration file, push a commit to the repository to trigger a Travis CI build.
Interestingly, without the configuration file in your repository earlier, the commit that introduces this file in the repository would also trigger a build on Travis CI.

---

## Slide 18

Getting Started With Travis CI

---

## Slide 19

Travis CI Build Results
How long Travis CI takes to run tests on a single commit depends on a few factors:
how many versions your build needs to be tested on
how many requirements your repository has
how detailed your unit tests are
Once your tests are complete, you receive an email with the results of the test. You can also view the status of your recent tests on your Travis dashboard.

---

## Slide 20

Travis CI Build Results

---

## Slide 21

Travis CI Build Results
If the tests are still running, Travis CI shows the live information about the test.
You can cancel the build if it’s taking a long time, or even restart a build after it has completed.
You can view the configuration file from within the build page to ensure the tests ran the way you intended them to.

---

## Slide 22

Advanced Configuration Settings
Now that we’ve run a successful test on Travis CI, let’s examine some advanced features of Travis CI and their use cases.
Imagine you intend to run Git-related operations in the build.
If a unit test fails, you’d like to automate the process of git bisect within this build to find out which commit introduced a bug.
To go ahead in this scenario, it isn’t necessary to download the full history of the project.
With the depth option, you can set the number of Git commits to clone through the following setting:
git:
depth: 3

---

## Slide 23

Advanced Configuration Settings
Next, while unit tests test how your code runs, your project may have detailed requirements before installation of the prerequisites.
In such cases, you may feel the need to run custom configuration commands on the server before running your projects’ build.
You can also set a list of commands to run before installing the prerequisites.
You can pass terminal commands as a list to run in this setting.
The echo command in the example below prints a message in your log:

---

## Slide 24

Advanced Configuration Settings
On similar lines, you can set a list of commands to run after the build is complete.
For instance, did the right version of your project execute? Do you want to check if data integrity is maintained on your server?
The following terminal commands are sequentially run after the build is complete:

---

## Slide 25

Advanced Configuration Settings
It’s possible that, during the process of a build, you may only be interested in how the current version of your project runs.
To make the debugging process easier, you may wish to remove Git-related messages from your logs altogether.
To ignore Git-related messages in your log files, you can set the quiet option in git to true:
git:
quiet: true

---

## Slide 26

Advanced Configuration Settings
While multiple developers work on their own features, you probably won’t want to trigger a build every time a developer sends a push.
You can safelist and blocklist branches to trigger builds for, or ignore changes to specific branches:

---

## Slide 27

Advanced Configuration Settings
While safelisting branches makes sense for a smaller team, you may still be dealing with a large number of push operations.
There’s an option to ignore build triggers with every push altogether — by setting up cron jobs on Travis CI to run a set of tasks periodically.
Go to the Cron Jobs section on the settings tab of any repository to set up cron jobs.

---

## Slide 28

Advanced Configuration Settings
Travis can integrate with Docker to create a custom build environment to test your code on.
You need to enable Docker under services and set up custom Docker commands in the before_install section:

---

## Slide 29

What Have You Learned?
In this chapter, we covered the integration of Git with DevOps to enable you to bring more efficiency into your software development cycle.
We first looked at custom scripts that can be used through Git hooks for various events and actions in Git.
We then discussed how to integrate Git with Travis CI to perform the task of continuous integration, one of the critical steps in the DevOps cycle.

---

# Chapter 9: Git GUI Tools


## Slide 1

Chapter 9Git GUI Tools
Full Stack Web Developer
FWDN 232: Web Developer Tools

---

## Slide 2

Introduction
Until now, we’ve performed all our Git-related actions through the terminal, looking in detail at what each command does.
The advantage of terminal commands is that they work across all platforms.
There are various GUI (graphic user interface) tools that can be used instead of the terminal.
Although GUI tools can appear to make life simpler, applications can use differing UIs, terminology, and Git concepts.
GUI tools also lack some of the power and features of the terminal, and terminal commands execute more quickly.

---

## Slide 3

Introduction
In this chapter, we’ll look at the GUI tools that serve as Git clients.
First, we’ll review GitHub Desktop, GitHub’s own GUI tool, and then Atlassian’s Sourcetree.
Both of these applications have macOS and Windows versions, but neither supports Linux.
Other popular GUI clients are Tower (macOS), GitBox (macOS), SmartGit (Windows, macOS, Linux), Fork (Windows, macOS, Linux), and GitKraken (Windows, macOS, Linux).
All of these applications are either free or have free trial versions.

---

## Slide 4

Introduction
You can also use Git’s capabilities through extensions in your text editor.
Atom, a text editor by GitHub, has builtin Git and GitHub functionality.
Sublime Text’s Git Integration package enables the use of many Git-related features from within the confines of the text editor.
Visual Studio’s version control tools enable you to integrate with multiple version control systems to manage repositories hosted in remote locations.

---

## Slide 5

Introduction
GUI tools are an attractive option to many developers, as they provide an easy interface for managing a project with Git.
Though we arguably gain a deeper understanding of Git by learning it through the command line, GUI tools have their place, especially in simple situations.
One issue with using GUI tools is that it’s easy to forget proper Git commands.
This is problematic if you find yourself in an environment without GUI software, or if you need to run emergency commands from the command line—such as working on a remote server.
I suggest using a combination of GUI tools and the command line, utilizing the advantages of each.

---

## Slide 6

GitHub Desktop
Let’s first take a look at the GUI client of GitHub itself. It supports both Windows and macOS.
The Windows and macOS versions of GitHub’s previous clients differed, but in August 2015 GitHub launched GitHub Desktop as a new, unified client for both platforms.
After installation, you should add your GitHub account details.
When you successfully log in to your account, all your repositories are linked to your GUI tool.
You can create a new repository through the New Repository… option from the File menu.
You can also see a list of your repositories under the Clone Repository… option.

---

## Slide 7

GitHub Desktop
Select the repository you want to clone, and click on Clone to clone it.

---

## Slide 8

GitHub Desktop
Alternatively, you can add a local Git repository by choosing the Add Local Repository… option in the File menu.
You’re then asked to select the path to an existing Git repository on your local system.

---

## Slide 9

GitHub Desktop
Once you’ve added your repository, you’ll notice that it’s now listed among the tracked repositories in the repositories list (Current Repository tab, top-left).
If you add a GitHub repository, it will be listed under your username on GitHub, whereas if you add a local repository, it will be listed under Other.

---

## Slide 10

GitHub Desktop
Once a repository is selected, the commits in the current branch are listed. The UI resembles the GitHub website. If any commit is selected, the commit details are shown too. The workflow in the current branch is shown at the top.

---

## Slide 11

GitHub Desktop
On selecting Show History from the View menu, you’re shown the commits in the active branch.
On selecting a specific commit, you’re shown the changes that were made in that commit:

---

## Slide 12

GitHub Desktop
Let’s move on from comparing branches to creating or changing a branch.
To create a branch, click on the Current Branch tab and enter the name of the new branch.
It will be created from the current active branch.

---

## Slide 13

GitHub Desktop
To change your current active branch to a different one, simply select a new branch from the list of branches.
On the top right of the window, there’s the Fetch Origin option, which gets the latest commits from your origin remote.
You can create a pull request from within the GUI client by first comparing two branches and then creating the pull request, just like you do on the GitHub website.

---

## Slide 14

GitHub Desktop
Any changes made to the repository are visible in the Changes tab (top left).
It lists the changes in the files, but note that there’s no mention of the term “staging”.
You simply select the files you want to include in the commit and add a commit message before committing the changes, which makes the process simpler for beginners.

---

## Slide 15

GitHub Desktop
Once you’ve committed the changes, the Fetch Origin button changes to Push Origin, which first fetches commits from the origin and then pushes your new commits.
On pushing to a branch of origin that’s not the master branch, a Create Pull Request button comes up, which redirects you to the appropriate link on the GitHub website.
GitHub Desktop tries to simplify the process of source code management, which is good for a beginner who’s trying to learn Git.
Let’s now explore Sourcetree, which has a wider range of functions.

---

## Slide 16

Sourcetree
Sourcetree is a GUI client developed by Atlassian.
It’s compatible with repositories managed by both Git and Mercurial, another distributed VCS.
Sourcetree can use the version of Git already installed on your local system, or a version that’s bundled with Sourcetree itself.
You can download and install the application from the Sourcetree website.
Sourcetree offers a wider range of features than GitHub’s tool, and gives you more control over your repositories.
Its various options also better match the corresponding terminal commands.
During installation, you’re invited to add details of any accounts you hold at code sharing websites like GitHub and Bitbucket.
If you skip this step, you can add accounts later in the Accounts tab of Preferences.

---

## Slide 17

Sourcetree

---

## Slide 18

Sourcetree
After adding your cloud accounts, you’re shown the list of repositories in your connected accounts.

---

## Slide 19

Sourcetree
The repositories listed here are present only on the cloud, so they need to be cloned before you can start working on them locally.
Click on the Clone link on the right of any repository to clone it.
After confirming the details, the remote repository is cloned to the location you specified in the last step.
Alternatively, you can add a local repository to Sourcetree by clicking on the +New Repository button.
Once you’ve added a repository, a new window opens with the details of the repository.

---

## Slide 20

Sourcetree
As highlighted in the image, the window has three parts: the top menu, the left menu, and the main body.
The top menu contains buttons that perform important actions in Git.
The left menu lists the branches, remotes, stashes and submodules.
The main body contains the list of commits in the active branch and the details of each commit.

---

## Slide 21

Sourcetree
If you look at the top menu, you’ll notice that it contains buttons for performing basic Git actions like commit, pull and push.
There’s also an option to open up a terminal in case you want to run a custom command.

---

## Slide 22

Sourcetree
The Branch button helps you checkout to a new or an existing branch.

---

## Slide 23

Sourcetree
When you make changes to any file, the list of changed files pops up in the space for unstaged files.
You can stage them by clicking the Add button on the top—after which they appear in the staged list. You can also remove staged files using the Remove button at the top.

---

## Slide 24

Sourcetree
Once you’re ready to make a commit, click on the Commit button.
For your first commit, you’re asked to nominate a name and email address to be associated with your commits.
This is similar to setting the global configuration settings through the terminal.
From now on, your email address and name will be associated with this commit, as well as any future commits.

---

## Slide 25

Sourcetree
After adding your name and email, you’re asked to add a message describing your commit.

---

## Slide 26

Sourcetree
After a successful commit, notice the state of the repository and the change in the branch workflows: the blue color shows the current commit—which hasn’t been merged with origin/master, denoted by yellow.

---

## Slide 27

Sourcetree
You can add or remove branches by clicking the Branch button in the top menu.
You can force delete a branch even if it hasn’t been merged yet. (This is analogous to the -D option in the terminal.)
You can merge branches through the Merge button in the top menu. If you want to merge branch_A into branch_B, make sure branch_B is active when you perform the merge operation.

---

## Slide 28

Sourcetree
Let’s now have a look at the left menu.
It shows a list of branches, tags, remotes, stashes and submodules.

---

## Slide 29

Sourcetree
In this case, master and gh-pages are the two branches, and origin is the only remote.
We also have one stash created on the master branch, which is shown in the screenshot above.
Sourcetree’s stash option is a powerful, easy-to-use feature.
You can apply any stash to your HEAD, with the option of keeping or removing the stash.
Submodules are Git repositories within a parent repository.
This repository uses a google_app submodule.

---

## Slide 30

Sourcetree
In addition, commit-based actions like checking out to the commit, cherry-picking or creating a patch can be performed by right-clicking on a commit, as shown below.

---

## Slide 31

Sourcetree versus GitHub Desktop
Both Sourcetree and GitHub Desktop are free to use.
Sourcetree has a lot of features, with an information-rich display that directly relates to Git’s terminal commands.
Desktop, on the other hand, focuses more on bridging the gap between a local GitHub repository and the GitHub website, often substituting standard Git terms and processes with easier terms for beginners.
It eases the process of hosting your repositories on GitHub, but makes it difficult—though not impossible—to host your repository elsewhere.

---

## Slide 32

Sourcetree versus GitHub Desktop
Finally, Desktop simplifies the whole process by cutting down on certain features, whereas Sourcetree offers a full-featured dashboard that might be overwhelming for beginners.
I encourage you to try both GUI tools, perhaps along with a few more listed at the beginning of this chapter, to work out which best suits your needs.

---

## Slide 33

What Have You Learned?
In this chapter, I reviewed two GUI tools for Git— Sourcetree and GitHub Desktop.
When using them, the history of a project, with respect to the different branches, is easily visualized.
Even when you’re working on a project, it’s useful to graphically analyze the changes you’ve made before committing them into the project history.
Even when you’re reviewing the work of others, it’s a good idea to use a GUI tool to quickly review the changes.
GUI tools aren’t cross platform, whereas terminal commands are.
There’s no single tool that works the same in Windows, macOS and Linux.
Also, if you’re working on a remote server (which is often a virtual machine), only command-line tools can help you work with Git.
And knowing terminal commands will help you understand how these GUI tools work.

---