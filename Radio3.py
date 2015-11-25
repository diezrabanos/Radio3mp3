import urllib2
from bs4 import BeautifulSoup
import time

#1 obtengo el listado de archivos
url=="http://www.rtve.es/alacarta/audios/turbo-3/"

resp = urllib2.urlopen(url2)
soup = BeautifulSoup(resp.read())
lista=[]
for link in soup.find_all('a'):
    if "http://mvod.lvlt.rtve.es/" in link['href']:
        lista.append(link['href'])

# 2 descargo el archivo
lista2=lista[:1]
for elemento in lista2:
    archivoDescargar = elemento
    archivoGuardar = "Turbo3"+str(elemento[-7:])
    now = time.time()
    descarga = urllib2.urlopen(archivoDescargar)
    ficheroGuardar=file(archivoGuardar,"wb")
    ficheroGuardar.write(descarga.read())
    ficheroGuardar.close()
    elapsed = time.time() - now
    print "Descargado el archivo: %s en %0.3fs" % (archivoDescargar,elapsed)
    
print "Hecho"
