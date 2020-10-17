from flask import Flask, render_template
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import *

app = Flask(__name__)

# Funcion que encripta con los parametros ingresados
def proceso_encriptar(llave, texto):
    cipher = AES.new(llave, AES.MODE_ECB)
    return cipher.encrypt(pad(texto, AES.block_size))

# Aqui modificar los datos
llave = b'LlaveDeLargo16__'
texto_plano = b'Este es un mensaje que sera encriptado'

# Encriptamos con los datos ingresados anteriormente
texto_encriptado = proceso_encriptar(llave, texto_plano)

# Cambiamos la base del texto encriptado
msj_b64 = b64encode(texto_encriptado).decode()

@app.route('/')
def home():
    try:
        return f"""<p>Este sitio contiene un mensaje oculto</p> <div class="AES-ECB" id={msj_b64}></div>"""
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)