import os
import sys
import shutil
sys.path.insert(0,"../..")


def list_to_str(l):
    ans=""
    if len(l)==0:
        return ans
    for i in range(0,len(l)-1):
        ans+=l[i]+"\n"
    ans+=l[len(l)-1]
    return ans    
    
def test():
    print "test"

def pwd():
    return os.getcwd()

def cd(param):
    #print "arg:"+arg
    #print "param:"+param
    #print(d[0])
    #print len(d)
    print "change current directory to "+param
    os.chdir(param)
    
def ls(param=os.getcwd()):
    ret=os.listdir(param)
    return list_to_str(ret)

def cat(param):
    if not os.path.exists(param):
        raise Exception("No such file exists!")
    f=open(param)
    lines=f.readlines()
    return list_to_str(lines)

def rm(path):
    if '*' in path:
        import re
        path_dir=os.path.dirname(path) or '.'
        file_name=os.path.basename(path)
        p=re.compile(file_name,re.IGNORECASE)
        fns=os.listdir(path_dir)
        for fn in fns:
            if p.match(fn):
                os.remove(fn)
        return               
    if os.path.isdir(path):
        os.rmdir(path)
    else:
        os.remove(path)

def grep(match,source):
    ans=[]
    for s in source.split('\n'):
        if match in s:
            ans.append(s)
    return list_to_str(ans)
    
def redirect(source,destination):
    if os.path.isfile(destination):
        f=open(destination,"w")
        f.write(source)
    else:
        raise Exception("No such file "+destination)
    
def wc(s):
    return len(s.split('\n'))
        
def mkdir(path):
    if os.path.exists(path):
        raise Exception("Directory already existed!")
    else:
        os.mkdir(path)
        return "Directory "+path+" created!"
    
def touch(fn):
    if os.path.exists(fn):
        raise Exception("file "+fn+" already exist!")
    else:
        f=open(fn,"w")
        f.close
        return "File created: "+fn
    
def cp(source,destination):
    if not os.path.exists(source):
        raise Exception("No such file exists!")
    shutil.copyfile(source,destination)
    
def mv(*p):
    if len(p)==2:
        os.rename(p[0], p[1])
    elif len(p)==1:
        shutil.move(p[0])
    else:
        raise Exception("Illegal Argument number: mv accept 1 or 2 arguments")
    
