import poplib,string,StringIO,email,pyssh

def connect_mailserver():
    theurl = 'http://mail.google.com/gmail/feed/atom'
    username = 'wasuaje'
    password = 'www4214'

    mail = poplib.POP3_SSL("pop.gmail.com",995)

    mail.user(username)
    mail.pass_(password)

    emails= mail.list()
    #mail.retr
    message_count = len(emails)

    #print mail.stat()
    mess=mail.retr(mail.stat()[0]-1)# ultimo mensaje agregar -1 para ir restando mensaje 257

    resp, text, octets = mess
    text = string.join(text, "\n")
    #file = StringIO.StringIO.(text)

    q = email.Parser.HeaderParser()
    p = q.parsestr(text)
    
    tipo = p.get_content_type()

    if ("text/plain" == tipo):
        # Si es texto plano, se escribe en pantalla
        a = p.get_payload(decode=True)
        a = a.split('\n')
        print a
        for k, v in p.items():
            if k=='Subject' and 'Host' in v:
                print k,'=',v
            #proces_main(message)
  

def proces_main(message):
        
        print message.fp.read()     #texo del mensage
        commands=message.fp.read().split('\n')
        run_cmds(commands)

def connect(hosts):
    pass
    
def run_cmds(commands):
    for cmd in commands:
        print cmd
        
        
connect_mailserver()    

#This is a multi-part message in MIME format        interceptar para evitar mensaje html buscar en ciclo for,
# es decir no tomar en cuenta si viene en mime
#salvar el nuumero del ultimo email en archivo plano, si la siguiente vez que corre el total de
# de emails es mayoo recorrer en ciclo desde el valor del archivo hasta el nuevo valor leyendo
# los subjects que nos interesa puede ser execute command
# de eontrarlo buscar los
# separa los comandos por \n para tener uno por lineas y poder mandar varios