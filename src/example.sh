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
ls test
echo "cp can copy files:"
cp 2 4
ls test
echo "rm can remove directory or files,and grep can be used with pipes:"
rm 4
ls test
echo "touch can create empty files:"
touch 5
ls test
echo "wc can measure file lines:"
wc 2
