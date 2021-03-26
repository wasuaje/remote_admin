

import pexpect
import sys
import re
import os


PROMPT = "\$|\%|\>"


class SSH:
    def __init__(self, user, password, host):
        self.child = pexpect.spawn("ssh %s@%s"%(user, host))
        i = self.child.expect(['assword:', r"yes/no"], timeout=120)
        if i==0:
            self.child.sendline(password)
        elif i==1:
            self.child.sendline("yes")
            self.child.expect("assword:", timeout=120)
            self.child.sendline(password)
            self.child.expect(PROMPT)


def command(self, command):
    """send a command and return the response"""
    self.child.sendline(command)
    self.child.expect(PROMPT)
    response = self.child.before
    return response

def close(self):
    """close the connection"""
    self.child.close()


if __name__=="__main__":
    import getpass
    password = getpass.getpass("Password: ")
    ssh = SSH("RemoteUsername", password, "RemoteHost")
    print ssh.command("pwd")
    ssh.close()


