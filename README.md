Shell4Win
=========

Shell4Win is a <b>shell interpreter</b> accepting UNIX/Linux style shell commands and shell scripts,it enables you to use shell on windows platform. it realised many important features of shell,including pipes,colon seperating commands in one line and redirection <br/ >
As a former UNIX administrator, batch is a little too messy for me and I have wasted too much time on its strange syntaxes and arguments.
If you happen to be familiar with shell and have to deal with Windows from now and then,There is a great chance you will like Shell4Win
<br/ >

How to get 
=========

Download zip files and all executables can be found in the bin directory.


How to use
=========

Shell4Win.exe in the bin directory is our main program,double click and you can get an interactive window where you can type in any <a href="#available-commands">available commands</a>. <br />
Shell4Win is also capable of explaining shell scripts by typing in <a href="#examples">sh example.sh</a>

Available Commands
=========

Shell4Win realised many commands in common use and the list of available commands keeps growing.
[echo,cd,ls,cat,rm,grep,wc,mkdir,touch,cp,mv...]

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

Dependecies
=========

Shell4Win uses following third party tools:
* [ply](http://www.dabeaz.com/ply/):generate lexical analyzer and syntax analyzer
* [py2exe](http://www.py2exe.org/):generate executable exe files on Windows


License
=========
[BSD]()
