from flask import Flask, request
from flask_restful import Resource, Api

flask2 = Flask(__name__)
api = Api(flask2)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return{'item':None}, 404

    def post(self, name):
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}  

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
#api.add_resource(Rooturl, '/', '/check')


if __name__ == "__main__":
    flask2.run(debug= True)
    
