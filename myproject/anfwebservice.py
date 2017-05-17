import requests
import base64, os
from SOAPpy import *


WSDLFILE = 'https://level.anf.es/FirmaArchivos/Firma?wsdl'
url = 'https://level.anf.es/FirmaArchivos/Firma?wsdl'


def cifrar1 ():
    archivo_cifrado=base64.b64encode(open("/home/arcen/test.pdf").read())
    #archivo_cifrado=base64.b64encode(bytes(open("/home/arcen/test.pdf").read(), 'utf-8'))
    print archivo_cifrado
    # headers = {'content-type': 'application/soap+xml'}
    headers = {'content-type': 'text/xml'}
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://servicio.anf.es/">
   <soapenv:Header/>
   <soapenv:Body>
      <ser:SignedPDF>
         <!--Optional:-->
         <usuario>{}</usuario>
         <!--Optional:-->
         <password>{}</password>
         <!--Optional:-->
         <archivo>{}</archivo>
         <!--Optional:-->
         <nombre>{}</nombre>
         <!--Optional:-->
         <tipoFirma>1</tipoFirma>
         <!--Optional:-->
         <mensaje>pruebarcen</mensaje>
         <!--Optional:-->
         <location>pruebarcen</location>
         <!--Optional:-->
         <reason>pruebarcen</reason>
         <!--Optional:-->
         <hashType>SHA1</hashType>
         <!--Optional:-->
         <posicion>1</posicion>
         <!--Optional:-->
         <pagina>1</pagina>
         <!--Optional:-->
         <px>380</px>
         <!--Optional:-->
         <py>700</py>
         <!--Optional:-->
         <height>20</height>
         <!--Optional:-->
         <width>20</width>
         <!--Optional:-->
         <conexion>0</conexion>
      </ser:SignedPDF>
   </soapenv:Body>
</soapenv:Envelope>""".format("ANFAC","WlTAqL7F",archivo_cifrado,"test.pdf")

    response = requests.post(url, data=body, headers=headers)

    archivo =response.content.split("<archivos>")[1]
    archivo = archivo.split("</archivos>")[0]
    with open(os.path.expanduser('/home/arcen/firmado.pdf'), 'wb') as fout:
        fout.write(base64.decodestring(archivo))
    print archivo


cifrar1()
