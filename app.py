from flask import Flask, render_template, request, jsonify
from ctf_starter_pack import brute_force, decoder, hash_cracker, flag_finder, xss_payload, zip_flag

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/bruteforce", methods=["POST"])
def api_bruteforce():
    data = request.json
    result = brute_force.web_run(data)
    return jsonify(result)

@app.route("/api/decode", methods=["POST"])
def api_decode():
    data = request.json
    result = decoder.web_run(data)
    return jsonify(result)

@app.route("/api/flagfinder", methods=["POST"])
def api_flagfinder():
    data = request.json
    result = flag_finder.web_run(data)
    return jsonify(result)

@app.route("/api/xss", methods=["POST"])
def api_xss():
    data = request.json
    result = xss_payload.web_run(data)
    return jsonify(result)

@app.route("/api/hashcracker", methods=["POST"])
def api_hashcracker():
    data = request.json
    result = hash_cracker.web_run(data)
    return jsonify(result)

@app.route("/api/zipflag", methods=["POST"])
def api_zipflag():
    data = request.json
    result = zip_flag.web_run(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

