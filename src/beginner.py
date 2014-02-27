import sys
sys.path.insert(0,"../..")
# Utilities  

tokens = ('COMMAND','ARGS','PARAM','PIPE','COLON','LREDIRECT','RREDIRECT')

FLAG=False

#Tokens



def t_PIPE(t):
    r'\|'
    global FLAG
    FLAG=False
    return t

def t_COLON(t):
    r';'
    global FLAG
    FLAG=False
    return t

t_ARGS=r'(-[a-zA-Z]+)'    

#t_PIPE=r'\|'
#t_COLON=r';'
#----------------------------------------------------------------------
def t_RREDIRECT(t):
    r'>'
    global FLAG
    FLAG=True
    return t
    
t_LREDIRECT=r'<'
#t_RREDIRECT=r'>'


t_ignore=" \t"

def t_newline(t):
    r'\n+'
    global FLAG
    FLAG=False
    t.lexer.lineno+=t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_COMMAND(t):
    r'"?[^|<>;\t ]+"?'
    global FLAG
    if FLAG:
        t.type='PARAM'
    else:
        FLAG=True
    return t



import ply.lex as lex
lexer=lex.lex()

'''
data=raw_input("input any commands:")
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok
'''


# Utilities
import os
import utilities
cmds=dir(utilities)



# Classes for commands
class expr:
    inPipe=False
    def __init__(self,cmd,params):
        self.cmd=cmd
        self.params=params

    def __str__(self):
        return self.cmd+" " +str(self.params)
    
        
    def execute(self):
        print "Execute command:"+self.cmd+" with params:"+str(self.params)
        if self.cmd in cmds:
            try:
                #print(self.params[0:])
                result=getattr(utilities,self.cmd)(*self.params[0:])
                #print result
                return result
            except Exception,e:
                print e
        else:
                print "No such command:"+self.cmd


'''      
class params:
    def __init__(self):
       self.params=[]
       
    def add(self,param):
        self.params.append(param)

    def __str__(self):
        s=""
        for element in self.params:
            s+=element+" "
        return s
'''



# Parser

precedence=(
    ('left','PIPE','COLON'),
    ('left','LREDIRECT','RREDIRECT')
    )

def p_statement(p):
    'statement : expression'
    global FLAG
    FLAG=False
    result =p[1].execute()
    if result:
        print result
    
def p_expression_pipe(p):
    'expression : expression PIPE expression'
    params=[]
    params.extend(p[3].params)
    params.append(p[1].execute())
    p[0]=expr(p[3].cmd,params)


    
def p_expression_colon(p):
    'expression : expression COLON expression'
    result=p[1].execute()
    if result:
        print result
    p[0]=p[3]

def p_expression_lredirect(p):
    'expression : expression LREDIRECT PARAM'
    raise Exception("< not supported yet!")

def p_expression_rredirect(p):    
    'expression : expression RREDIRECT PARAM'
    global FLAG
    FLAG=False
    result=p[1].execute()
    redirect(result,p[3])
    p[0]=p[1]
    p[0].execute=None
    
def p_expression(p):
    'expression : COMMAND PARAMS'
    global FLAG
    FLAG=False
    p[0]=expr(p[1],p[2])


def p_params(p):
    '''PARAMS : ARGUMENT
    | PARAMS PARAM'''
    if len(p)==2:
            p[0]=[]
            p[0].append(p[1])
    elif len(p)>2:
            p[1].append(p[2])
            p[0]=p[1]
    

def p_arg(p):
    '''ARGUMENT : ARGS
    |'''
    if len(p)>1:
        p[0]=p[1]
    else:
        p[0]=""


import ply.yacc as yacc
yacc.yacc()

import getpass
user=getpass.getuser()

import socket
computer_name=socket.gethostname()

print '''
#-------------------------------------------------------------------------------
#
# Shell4Win
#
# This is an open source shell interpreter
# it is made for system administrators who are used to shell syntax and
# need to deal with Windows from now and then. it enables you to use shell
# commands and scripts under Windows environment.
# 
# author:log4leo  https://github.com/log4leo/Shell4Win
# license: BSD
#
#-------------------------------------------------------------------------------
'''
print "[Current directory]"+os.getcwd()
while 1:
    try:  
        s=raw_input('['+user + '@' + computer_name +']#')
    except EOFError:
        break
    if not s:continue
    yacc.parse(s)
    lexer.input(s)
    while True:
        tok=lexer.token()
        if not tok:break
        print tok
    
    


