from flask import Flask, render_template, jsonify, request

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

if __name__ == '__main__':
    app.run()