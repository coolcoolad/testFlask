# -*- coding: utf-8 -*-

import os, sys
sys.path.insert(0, os.path.abspath('../flaskPackages/'))
from flask import Flask, request

app = Flask(__name__)

@app.route('/hello/', methods='POST')
def hello():
    print request.data
    print request.args
    jsonMap = {
        "@": "mst.bot.response",
        "result": {
            "@": "mst.map",
            "pic": {
                "@": "[INSERT YOUR NAMESPACE HERE].astro_picture",
                "highres_url": "http://apod.nasa.gov/apod/image/1612/RBA_DS_SeagullToSirius_2048.jpg",
                "meta": {
                    "@": "msp.meta",
                    "url": "http://apod.nasa.gov/apod/image/1612/RBA_DS_SeagullToSirius_1364.jpg",
                    "label": "Seagull to Sirius"
                }
            }
        }
    }
    return 'hello ok'

if __name__ == '__main__':
    app.run(host='10.172.211.107',port=7070)
