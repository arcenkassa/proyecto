from mongoengine import *
import json
import os
import time


class Emailjobs(Document): #(arcen)
    extra = {
        'collection': 'emailjobs'
    }
    content_source = ListField(required=False)
    creation_date = DateTimeField(required=False, null=False)
    procesando = BooleanField(default=False)
    finalizado = BooleanField(default=False)


def main ():
    count = 0
    while (count < 1):
        lista=Emailjobs.objects.filter()
        run=end=0
        os.system('clear')
        for i in lista:
            if i.procesando == True:
                run= run + 1
            if i.finalizado == True:
                end=end + 1

        print "*****Emailsend*******"
        print "procesos corriendo: " + str(run)
        print "procesos finalizados: " + str(end)
        print "*********************"

        time.sleep(1)




if __name__ == "__main__":
    connect('kulteo_aedashomes')
    main()

