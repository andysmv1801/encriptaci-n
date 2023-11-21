
def encriptar_imagen(ruta_imagen, ruta_imagen_encriptada):
    with open(ruta_imagen, 'rb') as archivo:
        imagen_bytes = bytearray(archivo.read())

        clave = 42

        imagen_encriptada = bytes([byte ^ clave for byte in imagen_bytes])

        with open(ruta_imagen_encriptada, 'wb') as archivo_encriptado:
            archivo_encriptado.write(imagen_encriptada)

def desencriptar_imagen(ruta_imagen_encriptada, ruta_imagen_desencriptada):
    with open(ruta_imagen_encriptada, 'rb') as archivo:
        imagen_encriptada_bytes = bytearray(archivo.read())

        clave = 42

        imagen_desencriptada = bytes([byte ^ clave for byte in imagen_encriptada_bytes])

        with open(ruta_imagen_desencriptada, 'wb') as archivo_desencriptado:
            archivo_desencriptado.write(imagen_desencriptada)

ruta_imagen_original = 'chihuahua.jpg'
ruta_imagen_encriptada = 'chihuahua1.jpg'
ruta_imagen_desencriptada = 'chihuahua2.jpg'

encriptar_imagen(ruta_imagen_original, ruta_imagen_encriptada)

desencriptar_imagen(ruta_imagen_encriptada, ruta_imagen_desencriptada)

