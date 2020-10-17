import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)
@app.route('/')
def primos():
    c = 1
    p = 1
    numero = 3
    primos = '2,'

    while p < 100:
        eprimo = 1
        for i in range(2, numero):
            if numero % i == 0:
                eprimo = 0
                break
        if (eprimo):
            primos = primos + str(numero) + ','
            p += 1
        numero += 1
    return primos
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
