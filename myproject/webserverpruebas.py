import requests

from SOAPpy import *


WSDLFILE = 'http://level.anf.es:8087/FirmaArchivos/Firma?wsdl'
url = 'http://level.anf.es:8087/FirmaArchivos/Firma?wsdl'


def cifrar1 ():
    archivo_cifrado=base64.b64decode(open("archivocifrar.pdf").read())
    print archivo_cifrado
    # headers = {'content-type': 'application/soap+xml'}
    headers = {'content-type': 'text/xml'}
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://servicio.anf.es/">
   <soapenv:Header/>
   <soapenv:Body>
      <ser:SignedPDF>
         <!--Optional:-->
         <usuario>ANFAC</usuario>
         <!--Optional:-->
         <password>WlTAqL7F</password>
         <!--Optional:-->
         <archivo>cid:608855629024</archivo>
         <!--Optional:-->
         <nombre>FirmaPrueba.pdf</nombre>
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
         <posicion>0</posicion>
         <!--Optional:-->
         <pagina>1</pagina>
         <!--Optional:-->
         <px>?</px>
         <!--Optional:-->
         <py>?</py>
         <!--Optional:-->
         <height>?</height>
         <!--Optional:-->
         <width>?</width>
         <!--Optional:-->
         <conexion>0</conexion>
      </ser:SignedPDF>
   </soapenv:Body>
</soapenv:Envelope>"""

    response = requests.post(url, data=body, headers=headers)
    print response.content



def cifrar2 ():
    service_url = 'http://level.anf.es:8087/FirmaArchivos/Firma'
    namespace = 'http://servicio.anf.es/'
    client = SOAPProxy(service_url, namespace)
    print client.namespace

def cifrar3 ():
    server = WSDL.Proxy("http://level.anf.es:8087/FirmaArchivos/Firma?wsdl")


cifrar1()
