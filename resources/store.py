from flask_restful import Resource 
from models.store import StoreModel

class Store(Resource):
    def get(self , name):
        store = StoreModel.get_by_name(name)
        if store:
            return store.json()
        return {'message' : 'store not found'} , 404

    def post(self , name):
        if StoreModel.get_by_name(name):
            return {'message' : 'store whith this name {} is already exist'.format(name)} , 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message' : 'an error occurred!'}  , 500 
        return store.json(), 201 

    def delete(self , name):
        store = StoreModel.get_by_name(name)
        if store:
            store.delete_from_db()
        
        return {'message' : 'store has been deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores' : [x.json() for x in StoreModel.query.all()]}