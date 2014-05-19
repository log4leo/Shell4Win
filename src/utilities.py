import os
import sys
import shutil
import tools
import subprocess
import helpers
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
    
def ls(*d):
    if(len(d)==0):
        cur=os.getcwd()
        ret=os.listdir(cur)
    else:
        ret=os.listdir(d[0])
    return list_to_str(ret)

def cat(param):
    if not os.path.exists(param):
        raise Exception("No such file exists!")
    f=open(param)
    lines=f.readlines()
    ans=""
    if len(lines)==0:
        return ans
    for i in range(0,len(lines)-1):
        if len(lines[i])>2 and lines[i].rfind('\n')==len(lines[i])-1:
            ans+=lines[i]
    ans+=lines[len(lines)-1]
    return ans

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
        shutil.rmtree(path)
    else:
        os.remove(path)

def grep(match,source):
    ans=[]
    for s in source.split('\n'):
        if match in s:
            ans.append(s)
    return list_to_str(ans)
    
def redirect(source,destination):
    #if os.path.isfile(destination):
        f=open(destination,"w")
        f.write(source)
    #else:
     #   f=open(destination,'w')
        
    #    raise Exception("No such file "+destination)
    
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
    if os.path.isfile(source):
        shutil.copy(source,destination)
    else:
        if(os.path.exists(destination) and os.path.isfile(destination)):
            raise Exception("File "+destination+" exists, please specify another directory name for dir copy!")
        if(not os.path.exists(destination)):
            mkdir(destination)
        for f in os.listdir(source):
            abf=source+'\\'+f
            if os.path.isdir(abf):
                cp(abf,destination+'\\'+f)
            else:
                shutil.copy(abf,destination)    
        
        
def mv(source,destination):
    shutil.move(source,destination)
    
def sh(fn):
    f=open(fn,"r")
    for l in f:
        tools.parse(l.strip())
        
def echo(*ss):
    ans=""
    for s in ss:
        ans+=s.replace('"','')+" "
    return ans
    
def diff(fn1,fn2):
    ans=[]
    f1=open(fn1,"r")
    f2=open(fn2,"r")
    list1=f1.readlines()
    list2=f2.readlines()
    max_len=max([len(list1),len(list2)])
    min_len=min([len(list1),len(list2)])
    for i in range(0,min_len):
        s1=list1[i]
        s2=list2[i]
        if s1!=s2:
            ans.append("line "+str(i+1)+":   "+s1 +"\t"+s2)
    for i in range(min_len,max_len):
        s=list1[i]
        if s:
            ans.append("line "+str(i+1)+":   "+s+"\t")
        else:
            ans.append("line "+str(i+1)+":   "+"\t"+s)
    return list_to_str(ans)


def read(*ss):
    ans=""
    for s in ss:
        ans+=s.replace('"','')+" "    
    raw_input(ans)
    
    
def call(*p):
    ans=""
    for cmd in p:
        ans+=cmd+" "
    os.system(ans)
    
def findinfile(p,d=os.getcwd()):
    ans=""
    for f in os.listdir(d):
        absf=d+"\\"+f
        if os.path.isdir(absf):
            ans=ans+findinfile(p,absf)
        else:
            if helpers.istext(absf):
                content=open(absf,'r').readlines()
                #print "search in file "+(d+f)
                #contains=False
                for s in content:
                    if p in s:
                        ans+=absf+"\n"
                        break
    return ans

            