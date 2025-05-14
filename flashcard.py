from flask import Flask, render_template, jsonify, request, abort
from model import db

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template(
        "welcome.html"
    )

@app.route("/nginx")
def nginx():
    return jsonify({
        "remote_addr": request.remote_addr,
        "x_real_ip": request.headers.get("X-Real-IP"),
        "x_forwarded_for": request.headers.get("X-Forwarded-For"),
    })

@app.route("/api/card/")
def api_card_list():
    return jsonify(db)

@app.route("/api/card/<int:index>/")
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)

if __name__ == '__main__':
    app.run()