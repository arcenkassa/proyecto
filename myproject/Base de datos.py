from mongoengine import *
from datetime import *
from calendar import *
from bson import json_util
import json

class Empresa5 (Document):
    title = StringField(max_length=200, required=True)
    email = StringField(max_length=255, required=True)
    login = StringField(max_length=255, required=True)
    #date_modified = DateTimeField(default=datetime.now)

class Empresa2(Document):
    first_name = StringField(max_length=255)
    last_name = StringField(max_length=255)
    email = StringField(max_length=255, unique=True)
    login = StringField(max_length=255, unique=True)
    user_folder = ReferenceField('Folder', required=False)
    system_user = BooleanField(required=False, default=False)
   # confirmed = DateTimeField(default=datetime.datetime.now)
    time_offset = IntField(default=0)

    creation_date = DateTimeField(required=False, null=False)
    creation_user = ReferenceField('User')

    last_modification_date = DateTimeField(required=False, null=False)
    last_modification_user = ReferenceField('User')

    deleted = BooleanField(required=False, default=False)
    deletion_date = DateTimeField(required=False, null=False)
    deletion_user = ReferenceField('User', required=False)

    last_login = DateTimeField(null=True)
    last_login_ip = StringField(max_length=39)
    last_login_retries = IntField(default=0)
    image = StringField(max_length=512, default='')
    expiration = DateTimeField(null=True)
    password = StringField(max_length=255, required=True)
    active = BooleanField(default=True)



def main ():
    connect('')
    empresa=Empresa5()
    empresa.title="papyrum"
    empresa.email ="papyrum"
    empresa.login ="papyrum"
    empresa.save()
    empresa=Empresa5.objects.filter()
    lst=json.loads(empresa.to_json())
    print lst

if __name__ == "__main__":
    main()


