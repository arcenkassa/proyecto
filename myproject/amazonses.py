import smtplib

def send():
    fromaddr = 'arcenkassa2@gmail.com'
    toaddrs = 'arcenkassa2@gmail.com'
    msg = """From: arcenkassa2@gmail.com

    Hello, this is doge.
    """

    print "Message length is " + repr(len(msg))

    # Change according to your settings
    smtp_server = 'email-smtp.us-west-2.amazonaws.com'
    smtp_username = 'AKIAI6IWUWQI5KZR7TIQ'
    smtp_password = 'AkwQer76Gbyboq5MPfuUwIWfJ9eOWZs1rquUZeDXPepe'
    smtp_port = '587'
    smtp_do_tls = True

    server = smtplib.SMTP(
        host=smtp_server,
        port=smtp_port,
        timeout=10
    )
    server.set_debuglevel(10)
    server.starttls()
    server.ehlo()
    server.login(smtp_username, smtp_password)
    server.sendmail(fromaddr, toaddrs, msg)
    print server.quit()

send()



