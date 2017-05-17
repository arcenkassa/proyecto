import boto.ses
conn = boto.ses.connect_to_region(
        'us-west-2',
        aws_access_key_id='AKIAIVUS2LY3A5X6IOUQ',
        aws_secret_access_key='py0R+BZMHCWdJWE+zUtTU67Gs0kRBOytUiwCeHrZ')

response = conn.send_email(
                        'arcenkassa2@gmail.com',
                        'Your subject',
                        'Body here',
                        ['arcenkassa@gmail.com'])

print (response)


