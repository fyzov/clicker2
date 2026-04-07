from functools import lru_cache

from flask import jsonify

from source.main import base_cost, multiplier


@lru_cache(maxsize=None)
def get_upgrade_cost(level):
    if level <= 1:
        return 0

    cost = base_cost * (multiplier ** (level - 2))
    return round(cost)


def success_response(data=None, message="none"):
    return jsonify({"status": "success", "data": data, "message": message}), 200


def error_response(message, code=400):
    return jsonify({"status": "error", "message": message}), code
