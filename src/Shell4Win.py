import tools    
import getpass
import os

user=getpass.getuser()

import socket
computer_name=socket.gethostname()

print '''
#-----------------------------------------------------------------------------#
# Shell4Win                                                                   #
#                                                                             #
# This is an open source shell interpreter                                    #
# it is made for system administrators who are used to shell syntax and       #
# need to deal with Windows from now and then. it enables you to use shell    #
# commands and scripts under Windows environment.                             #
#                                                                             #
# author:log4leo  https://github.com/log4leo/Shell4Win                        #
# license: BSD                                                                #
#                                                                             #
#-----------------------------------------------------------------------------#
'''
print "[Current directory]"+os.getcwd()
while 1:
    try:  
        s=raw_input('['+user + '@' + computer_name +']#')
    except EOFError:
        break
    if s.startswith('#'):continue
    if not s:continue
    tools.parse(s)