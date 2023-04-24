from flask import Flask, request, jsonify, make_response, Response
from flask_cors import CORS, cross_origin
from convert_image import b64_to_array
import matplotlib.pyplot as plt
import time
import random
import os


app = Flask(__name__)
CORS(app)


@app.route('/api/user/pattern', methods=['PUT'])
def hello_world():
    response = request.get_json()
    print(time.time())

    time.sleep(3.0)
    try:
        plt.imsave("images/frame_{}.jpg".format(len(os.listdir("images"))), b64_to_array(response['images'][0]))
    except:
        pass
    return make_response(jsonify({
        "zcfg_requester_comboname": "test",
        "zcfg_requester_phone_number": random.randint(0, 1000),
        "zcfg_requester_address_email": "test@example.com",
        "zcfg_requester_id_passport": random.randint(0, 1000)
    }), 200)


if __name__ == '__main__':
    app.run(
        host='192.168.0.2', port=5000,
        debug=True, ssl_context=('certs/kotora.crt', 'certs/kotora.key')
    )
