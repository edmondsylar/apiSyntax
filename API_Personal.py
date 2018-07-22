from flask import Flask, request, Response, jsonify, make_response

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST', 'DELETE', 'PUT'])
def my_api():
    if request.method == 'GET':
        return make_response(jsonify({"Result": "Your Fetch Worked"}))

    elif request.method == 'POST':
        return make_response(jsonify({"Result": "You Are Attempting to Make a POST request"}))

    elif request.method == 'PUT':
        return make_response(jsonify({"Reasult": "This is an attempt to Make a PUT request"}))

    elif request.method == 'DELETE':
        return make_response(jsonify({"Reasult": "This is an attempt to make a DELETE request"}))

if __name__ == '__main__':
    app.run(debug=True)