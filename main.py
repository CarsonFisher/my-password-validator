import flask


# TODO: change this to your academic email
AUTHOR = "carsonf@sas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    if not pw:
        return flask.jsonify({"valid": False, "reason": "Password is required"}), 400

    if not any(c.isupper() for c in pw):
        return flask.jsonify({"valid": False, "reason": "Password must include at least one uppercase letter"}), 400

    if not any(c.isdigit() for c in pw):
        return flask.jsonify({"valid": False, "reason": "Password must include at least one digit"}), 400

    if not any(c in string.punctuation for c in pw):
        return flask.jsonify({"valid": False, "reason": "Password must include at least one special character"}), 400

    return flask.jsonify({"valid": True}), 200

    # FIXME: to be implemented
    return flask.jsonify({"valid": False, "reason": "Not implemented"}), 501
