import sys
#sys.path.insert(0,"./ply")
# Utilities  

tokens = ('COMMAND','PIPE','COLON','LREDIRECT','RREDIRECT')

#Tokens



def t_PIPE(t):
    r'\|'
    return t

def t_COLON(t):
    r';'
    return t 

def t_RREDIRECT(t):
    r'>'
    return t
    
t_LREDIRECT=r'<'
t_ignore=" \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno+=t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_COMMAND(t):
    r'"?[^|<>;\t ]+"?|".*"'
    return t



import ply.lex as lex
lexer=lex.lex()



# Utilities
import os
import utilities
cmds=dir(utilities)


def placeholder():
    'Just a pass'
    pass

# Classes for commands
class expr:
    def __init__(self,cmd,params):
        self.cmd=cmd
        self.params=params

    def __str__(self):
        return self.cmd+" " +str(self.params)
    
        
    def execute(self):
        #print "Execute command:"+self.cmd+" with params:"+str(self.params)
        if self.cmd in cmds:
            try:
                result=getattr(utilities,self.cmd)(*self.params[0:])
                return result
            except Exception,e:
                print e
        else:
                print "No such command:"+self.cmd



# Parser

precedence=(
    ('left','PIPE','COLON'),
    ('left','LREDIRECT','RREDIRECT')
    )

def p_error(p):
    print p

def p_statement(p):
    '''statement : expression
    | term'''
    result =p[1].execute()
    if result:
        print result


def p_expression_pipe(p):
    'expression : term PIPE term'
    params=[]
    params.extend(p[3].params)
    params.append(p[1].execute())
    p[0]=expr(p[3].cmd,params)


    
def p_expression_colon(p):
    'expression : term COLON term'
    result=p[1].execute()
    if result:
        print result
    p[0]=p[3]


def p_expression_lredirect(p):
    'term : term LREDIRECT COMMAND'
    raise Exception("< not supported yet!")

def p_expression_rredirect(p):    
    'term : term RREDIRECT COMMAND'
    result=p[1].execute()
    utilities.redirect(result,p[3])
    p[0]=p[1]
    p[0].execute=placeholder
    
def p_expression(p):
    '''term : COMMAND
    | term COMMAND'''
    if len(p)==2:
        p[0]=expr(p[1],[])
    else:
        p[1].params.append(p[2])
        p[0]=p[1]



    




import ply.yacc as yacc
yacc.yacc()

def parse(s):
    yacc.parse(s)

    


