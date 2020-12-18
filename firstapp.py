from flask import Flask, jsonify, request, render_template

flask1 = Flask(__name__)

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

@flask1.route('/')

def home():
    return render_template('index.html')

# POST ~ used to recieve data
# GET ~ used to send back the data

# POST / store data: {name: }
@flask1.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'item': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string: none>
@flask1.route('/store/<string:name>')  #
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not  found'})        
         

# GET /store
@flask1.route('/store')  
def get_stores():
    return jsonify({'stores': stores})

# POST / store/<string:name>/item   {name: , price:}
@flask1.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})        

# GET /store/<string:name>/Item
@flask1.route('/store/<string:name>/item')  #
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['item']})
    return jsonify({'message': 'store not found.'})        

flask1.run(port=5000)    

