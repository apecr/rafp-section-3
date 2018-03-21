from flask import Flask

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
    pass


@app.route('/store/<string:name>', methods=['GET'])
def get_store(store_name):
    pass


@app.route('/store', methods=['GET'])
def get_stores():
    pass


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(store_name):
    pass


@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_in_store(store_name):
    pass


app.run(port=5000)
