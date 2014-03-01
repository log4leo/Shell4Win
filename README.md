Shell4Win
=========

Shell4Win is a <b>shell interpreter</b> accepting UNIX/Linux style shell commands and shell scripts,it enables you to use shell on windows platform. it realised many important features of shell,including pipes,colon seperating commands in one line and redirection <br/ >
As a former UNIX administrator, batch is a little too messy for me and I have wasted too much time on its strange syntaxes and arguments.
If you happen to be familiar with shell and have to deal with Windows from now and then,There is a great chance you will like Shell4Win
<br/ >

How to get 
=========

<a href="https://github.com/log4leo/Shell4Win/archive/master.zip">Download</a> zip files and all executables can be found in the bin directory.


How to use
=========

Shell4Win.exe in the bin directory is our main program,double click and you can get an interactive window where you can type in any <a href="#available-commands">available commands</a>. <br />
Shell4Win is also capable of explaining shell scripts by typing in <a href="#examples">sh example.sh</a>

Available Commands
=========

Shell4Win realised many commands in common use and the list of available commands keeps growing.
[echo,cd,ls,cat,rm,grep,wc,mkdir,touch,cp,mv...]

Dependecies
=========

Shell4Win uses following third party tools:
* [ply](http://www.dabeaz.com/ply/):generate lexical analyzer and syntax analyzer
* [py2exe](http://www.py2exe.org/):generate executable exe files on Windows


License
=========
[BSD]()


Examples
=========

```shell
[Administrator@PC-20121113XYVZ]#ls
parser.out
parsetab.py
parsetab.pyc
ply
Shell4Win.py
tools.py
tools.pyc
utilities.py
utilities.pyc
```

```shell
[Administrator@PC-20121113XYVZ]#ls|grep Shell
Shell4Win.py
```

```shell
[Administrator@PC-20121113XYVZ]#pwd
C:\Users\Administrator\Documents\GitHub\Shell4Win\src
```

```shell
[Administrator@PC-20121113XYVZ]#cat example.sh
echo "#This is a example shell script written to demostrate a shell interpreter named Shell4Win#"

echo "Let's start with some simple commands"

echo "ls can show files under current directory:"

ls

read "Press Enter key to continue"

echo "pwd can show you current directory:"

pwd

read "Press Enter key to continue"

echo "mkdir can make a directory,and grep can be used with pipes:"

mkdir test

ls|grep test

echo "cd can change current directory:"

cd test

echo "redirection can create files:"

echo "test content1">1

echo "test content2">2

cat 1

cat 2

echo "diff can be used to compare two text files:"

diff 1 2

echo "mv can move files or change file name:"

mv 1 3

ls

echo "cp can copy files:"

cp 2 4

ls

echo "rm can remove directory or files,and grep can be used with pipes:"

rm 4

ls

echo "touch can create empty files:"

touch 5

ls

echo "wc can measure file lines:"

wc 2

[Administrator@PC-20121113XYVZ]#sh example.sh
#This is a example shell script written to demostrate a shell interpreter named Shell4Win# 
Let's start with some simple commands 
ls can show files under current directory: 
example.sh
parser.out
parsetab.py
parsetab.pyc
ply
Shell4Win.py
test
tools.py
tools.pyc
utilities.py
utilities.pyc
Press Enter key to continue 
pwd can show you current directory: 
C:\Users\Administrator\Documents\GitHub\Shell4Win\src
Press Enter key to continue 
mkdir can make a directory,and grep can be used with pipes: 
Directory already existed!
test
cd can change current directory: 
change current directory to test
redirection can create files: 
test content1 
test content2 
diff can be used to compare two text files: 
line 1:   test content1 	test content2 
mv can move files or change file name: 
[Error 183] 
example.sh
parser.out
parsetab.py
parsetab.pyc
ply
Shell4Win.py
test
tools.py
tools.pyc
utilities.py
utilities.pyc
cp can copy files: 
example.sh
parser.out
parsetab.py
parsetab.pyc
ply
Shell4Win.py
test
tools.py
tools.pyc
utilities.py
utilities.pyc
rm can remove directory or files,and grep can be used with pipes: 
example.sh
parser.out
parsetab.py
parsetab.pyc
ply
Shell4Win.py
test
tools.py
tools.pyc
utilities.py
utilities.pyc
touch can create empty files: 
file 5 already exist!
example.sh
parser.out
parsetab.py
parsetab.pyc
ply
Shell4Win.py
test
tools.py
tools.pyc
utilities.py
utilities.pyc
wc can measure file lines: 
1
```
