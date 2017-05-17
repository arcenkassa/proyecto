# -*- coding: utf-8 -*-
import boto3

##############################################################
def emailconfig():
    region = 'us-west-2'
    user = 'AKIAIVUS2LY3A5X6IOUQ'  # insert your access key to use when creating the client
    pw = 'py0R+BZMHCWdJWE+zUtTU67Gs0kRBOytUiwCeHrZ'  # insert the secret key to use when creating the client
    client = boto3.client(service_name='ses',
                          region_name=region,
                          aws_access_key_id=user,
                          aws_secret_access_key=pw)
    return client
##############################################################

def emailsend (emaildata):
    client = emailconfig()
    for elemento in emaildata:
        if isinstance(elemento, list):
            emaildestino = elemento[0]
            asunto = elemento[1]
            archivo = elemento[2]
            response = client.send_email(
                Source='arcenkassa@gmail.com',
                Destination={
                    'ToAddresses': [
                        emaildestino,
                    ]
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': 'UTF-8',
                            'Data': archivo + 'This message body contains HTML formatting. It can, for example, contain links like this one: <a class="ulink" href="http://docs.aws.amazon.com/ses/latest/DeveloperGuide" target="_blank">Amazon SES Developer Guide</a>.',
                        },
                    },
                    'Subject': {
                        'Charset': 'UTF-8',
                        'Data': asunto,
                    },
                    }
                )

    return response
##############################################################

Correos=[["arcenkassa2@gmail.com","asunto1","archivo"],
        ["arcenkassa2@gmail.com","asunto2","archivo"],
        ["arcenkassa2@gmail.com","asunto3","archivo"],
        ["arcenkassa2@gmail.com","asunto4","archivo"],
        ["arcenkassa2@gmail.com","asunto5","archivo"]]







emailsend(Correos)









#emailsend(Correos)






