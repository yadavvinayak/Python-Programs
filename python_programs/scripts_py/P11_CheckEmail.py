

import email, getpass, imaplib, os
detach_dir = '.'                                                                        
                                            
pwd = getpass.getpass("Enter your Gmail Password: ")

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login('vinayak.comp@mmcoe.edu.in', pwd)
mail.list()
mail.select('INBOX')                                           

response, ids = mail.search(None, '(ALL)')                            
ids = ids[0].split()
ids = ids[::-1]                                          

i = 0
for emailid in ids:
    i += 1
    response, data = mail.fetch(emailid, "(RFC822)")                    
    email_body = data[0][1]                                                    
    mailFetch = email.message_from_bytes(email_body)                                                

    if mailFetch.get_content_maintype() != 'multipart':
        continue

    mailFetch['Subject'] = mailFetch['Subject'].replace(r'=?utf-8?q?', '')
    mailFetch['Subject'] = mailFetch['Subject'].replace('_', ' ')
                                       
    print ("["+mailFetch["From"]+"]:" + mailFetch['Subject'].replace('=?utf-8?q?', '').replace('_', ' ').replace('=3F?=', '?').replace('?=',''))

    for part in mailFetch.walk():
                                                        
        if part.get_content_maintype() == 'multipart':
            continue

        if part.get('Content-Disposition') is None:
            continue

        filename = mailFetch["From"] + "_hw1answer"

        att_path = os.path.join(detach_dir, filename)

        if not os.path.isfile(att_path) :
                                     
            fp = open(att_path, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()

    if (i == 10):                                   
        break
