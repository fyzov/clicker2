from flask import jsonify


def success_response(data=None, message=None):
    return jsonify({"status": "success", "data": data, "message": message}), 200


def error_response(message, code=400):
    return jsonify({"status": "error", "message": message}), code
