import smtplib
import time
import imaplib
import email

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "aviveershetty" + ORG_EMAIL
FROM_PWD = "saralaveer"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL, FROM_PWD)
mail.select('inbox')

type, data = mail.search(None, 'ALL')
mail_ids = data[0]

id_list = mail_ids.split()
first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])

for i in range(latest_email_id, first_email_id, -1):
    typ, data = mail.fetch(str(i), '(RFC822)')

    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(str(response_part))
            email_subject = msg['subject']
            email_from = msg['from']
            message = []
            for j in range(10):
                message[j] = msg

print(message)
