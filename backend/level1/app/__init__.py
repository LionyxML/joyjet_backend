from flask import Flask, jsonify, request


# App setup
app = Flask(__name__)


# App routes
@app.route("/", methods=["POST"])
def procces_post():
    msg = request.json
    return jsonify(msg),200


# App init
if __name__ == "__main__":
    app.run()
