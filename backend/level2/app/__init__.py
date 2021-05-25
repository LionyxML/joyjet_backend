from flask import Flask, jsonify, request


# App setup
app = Flask(__name__)


# Utilitary functions
def carts_total(msg, resp):
    """ Given the API expected json msg input and the expected resp(onse),
        calculates all carts totals
    """
    for cart in msg["carts"]:
        cart_value = 0

        for item in cart["items"]:
            cart_value += (
                item["quantity"]
                * next(
                    (sub for sub in msg["articles"] if sub["id"] == item["article_id"]),
                    None,
                )["price"]
            )

        resp["carts"].append({"id": cart["id"], "total": cart_value})

    return resp


# App routes & main functionality
@app.route("/", methods=["POST"])
def proccess_post():
    """ Receives the requested input and passes to the utilitary carts_total
        function.
    """
    msg = request.json
    resp = {"carts": []}
    return jsonify(carts_total(msg, resp)), 200


@app.errorhandler(Exception)
def exception_handler(e):
    """ Raise API Errors. """
    msg = { "error": "Internal Server Error"}
    try:
        code_error = e.code
        msg["error"] = str(e)
    except:
        code_error = 500

    return jsonify(msg), code_error

# App init
if __name__ == "__main__":
    app.run()
