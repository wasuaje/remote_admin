import pexpect,getpass
cmd = "ssh wasuaje@10.3.1.41"
child = pexpect.spawn(cmd,[],1)

# expect mysql to prompt for a db password
a=child.expect(['password:',pexpect.EOF,pexpect.TIMEOUT],1)
print a
# send the password
child.sendline('www4214')
child.sendline('echo prueba12 > /home/wasuaje/prueba.debug')
child.expect(pexpect.TIMEOUT)
