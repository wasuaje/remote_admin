import poplib,string,email,pexpect,os
from ssh_controller import *

USER='wasuaje'
PASSWORD='www4214'

def connect_mailserver():
    username = 'wasuaje'
    password = 'www4214'

    mail = poplib.POP3_SSL("pop.gmail.com",995)

    mail.user(username)
    mail.pass_(password)

    #emails= mail.list()
    
    #message_count = len(emails)

    #print mail.stat()
    mess_id= mail.stat()[0]
    
    return (mail,mess_id)

def get_email(messid,mail):
    mess=mail.retr(messid)# ultimo mensaje agregar -1 para ir restando mensaje 257
    resp, text, octets = mess
    text = string.join(text, "\n")
    
    q = email.Parser.HeaderParser()
    p = q.parsestr(text)
    
    tipo = p.get_content_type()
    
    if ("text/plain" == tipo):
        # Si es texto plano, se escribe en pantalla        
        a = p.get_payload(decode=True)
        commands = a.split('\n')        
        for k, v in p.items():            
            if k=='Subject' and 'Host' in v:
                print k,'=',v
                host = v.replace('Host ','')            
                run_cmds(host,commands)
                
    
def run_cmds(host,commands):    
    cmd = "ssh wasuaje@"+host
    child = pexpect.spawn(cmd,[],3)     #es necesario minimo este tiempo sino sale antes

    # expect mysql to prompt for a db password
    child.expect(['password:',pexpect.EOF,pexpect.TIMEOUT,pexpect.EOF],1)
    #print a
    # send the password
    #child.sendline('Am3r1c4*/')
    child.sendline('www4214')
    
    for cmd in commands:
        print cmd
        cmd=cmd.replace('\r','')            
        if 'BlackBerry' not in cmd :
            print cmd
            #response = pyssh.run_command(cmd)
            child.sendline(cmd)   
    child.expect(pexpect.TIMEOUT)
    
def write_to_file(newemailid):
    file = open("last_email_id.txt", "w")
    file.write(str(newemailid))
    file.close()

def read_file():
    mid=connect_mailserver()   
    if os.path.exists("last_email_id.txt"):
        file = open("last_email_id.txt", "r")
        data = file.read()
        file.close()    
        if len(data)==0 or data=='':
            write_to_file(mid[1])
    else:
       write_to_file(mid[1])
       data=mid
    return data

def main():
    lastemail=read_file()
    lastid=connect_mailserver()
    #print lastemail,lastid[1]
    if lastemail < lastid[1]:
        for i in range(int(lastemail),lastid[1]+1):        
            get_email(i,lastid[0])        
            write_to_file(str(i))
            print i    
    
main()

#This is a multi-part message in MIME format        interceptar para evitar mensaje html buscar en ciclo for,
# es decir no tomar en cuenta si viene en mime
#salvar el nuumero del ultimo email en archivo plano, si la siguiente vez que corre el total de
# de emails es mayoo recorrer en ciclo desde el valor del archivo hasta el nuevo valor leyendo
# los subjects que nos interesa puede ser execute command
# de eontrarlo buscar los
# separa los comandos por \n para tener uno por lineas y poder mandar varios