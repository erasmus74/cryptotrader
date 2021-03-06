import sys,os,json
from flask import Flask,render_template,request,jsonify

sys.path.append("..")
curdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curdir + "/..")

import cryptolib
from tcpsock import TcpSock

app = Flask (__name__)


@app.route("/mybot", methods = ['GET'])
def mybot():
    return render_template("newdark.html")


@app.route("/_botdata")
def botdata():
    port = int(request.args["bot"])
    sock = TcpSock("127.0.0.1", port )

    info = json.loads(sock.get("info"))
    charts = json.loads(sock.get("amcharts"))
    trades = json.loads(sock.get("trades"))

    return jsonify({
        "info": info,
        "charts": charts,
        "trades": trades
        })



@app.route("/_botinfo")
def botinfo():
    port = int(request.args["bot"])
    sock = TcpSock("127.0.0.1", port )
    response = json.loads(sock.get("info"))
    return jsonify(response)

@app.route("/_botchart")
def botchart():
    port = int(request.args["bot"])
    sock = TcpSock("127.0.0.1", port )
    response = json.loads(sock.get("chart"))
    return jsonify(response)

@app.route("/_tacharts")
def tacharts():
    port = int(request.args["bot"])
    sock = TcpSock("127.0.0.1", port )
    response = json.loads(sock.get("tacharts"))
    return jsonify(response)

@app.route("/_amcharts")
def amcharts():
    port = int(request.args["bot"])
    sock = TcpSock("127.0.0.1", port )
    response = json.loads(sock.get("amcharts"))
    return jsonify(response)


@app.route("/_bottrades")
def bottrades():
    port = int(request.args["bot"])
    sock = TcpSock("127.0.0.1", port )
    response = json.loads(sock.get("trades"))
    return jsonify(response)

