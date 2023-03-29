# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
CORS(app)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/api/user/pattern', methods=['POST'])
def hello_world():
    response = request.get_json()
    print(response)
    return jsonify(
        message='Success'
    )

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True, ssl_context=('certs/cert.pem', 'certs/key.pem'))
