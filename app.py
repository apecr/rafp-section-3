from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/')
def home():
    return "Hello, world!"


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store), 201


@app.route('/store/<string:store_name>', methods=['GET'])
def get_store(store_name):
    store = [store for store in stores if store['name'] == store_name]
    if store:
        return jsonify(store)
    return jsonify({}), 404


@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:store_name>/item', methods=['POST'])
def create_item(store_name):
    request_data = request.get_json()
    store = [store for store in stores if store['name'] == store_name]
    if store:
        store[0]['items'].append(request_data)
        return jsonify(request_data), 201
    return jsonify({}), 404


@app.route('/store/<string:store_name>/item/<string:item_name>', methods=['GET'])
def get_item_in_store(store_name, item_name):
    store = [store for store in stores if store['name'] == store_name]
    if store:
        store = store[0]
        item = [item for item in store['items'] if item['name'] == item_name]
        if item:
            return jsonify(item)
    return jsonify({}), 404


app.run(port=5000, debug=True)
