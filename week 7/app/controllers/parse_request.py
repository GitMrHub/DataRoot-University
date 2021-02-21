from flask import request

def get_request_data():
    """
    Get keys & values from request (Note that this method should parse requests with content type "application/x-www-form-urlencoded")
    """
    res = {}
    data = request.form
    for key in data:
        res[key] = data[key]
    return res