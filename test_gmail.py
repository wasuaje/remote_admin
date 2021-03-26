from gmaillib import *

c = GmailClient()
c.login('wasuaje@gmail.com', 'www4214')
c.get_inbox_conversations()
