from flask import Flask, jsonify, request


# App setup
app = Flask(__name__)


# Utilitary functions
def carts_totalize(msg):
    """ Given the API expected json msg input and the expected resp(onse),
        calculates all carts totals
    """

    resp = {"carts": []}

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


def carts_apply_delivery(carts_totalized, fees):
    """ Given totalized cart values, calculates delivery fees and adds to
        the total price
    """

    resp = {"carts": []}

    for cart in carts_totalized["carts"]:
        for fee in fees:
            lower_value = fee["eligible_transaction_volume"]["min_price"]

            if fee["eligible_transaction_volume"]["max_price"] != None:
                higher_value = fee["eligible_transaction_volume"]["max_price"]
            else:
                higher_value = cart["total"] + 1

            if cart["total"] >= lower_value and cart["total"] < higher_value:
                delivery_fee = fee["price"]

        resp["carts"].append({"id": cart["id"], "total": cart["total"] + delivery_fee})

    return resp


# App routes & main functionality
@app.route("/", methods=["POST"])
def proccess_post():
    """ Receives the requested input and passes to the utilitary carts_total
        function.
    """
    msg = request.json
    carts_total = carts_totalize(msg)
    carts_total_plus_delivery = carts_apply_delivery(carts_total, msg["delivery_fees"])

    return jsonify(carts_total_plus_delivery), 200


@app.errorhandler(Exception)
def exception_handler(e):
    """ Raise API Errors. """
    msg = {"error": "Internal Server Error " + str(e)}
    try:
        code_error = e.code
        msg["error"] = str(e)
    except:
        code_error = 500

    return jsonify(msg), code_error


# App init
if __name__ == "__main__":
    app.run()
