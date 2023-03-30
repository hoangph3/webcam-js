from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from convert_image import b64_to_array
import matplotlib.pyplot as plt
import os


app = Flask(__name__)
CORS(app)

@app.route('/api/user/pattern', methods=['POST'])
def hello_world():
    response = request.get_json()
    # print(response)
    plt.imsave("images/frame_{}.jpg".format(len(os.listdir("images"))), b64_to_array(response['image']))
    return jsonify(
        message='Success'
    )


if __name__ == '__main__':
    app.run(debug=True, ssl_context=('certs/cert.pem', 'certs/key.pem'))
