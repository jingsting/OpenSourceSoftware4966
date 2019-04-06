from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
client = MongoClient('mongodb://localhost:27017/')

if __name__ == '__main__':
    db = client['mongo_db_lab']
    col = db['definitions']
    for one in col.find():
        print(one)
    [print('.\n') for i in range(5)]
    pprint.pprint(col.find_one())
    pprint.pprint(col.find_one({'word': 'B.S.'}))
    pprint.pprint(col.find_one({'_id': ObjectId('56fe9e22bad6b23cde07b8b8')}))
    post = {'definition': ' n. a single distinct meaningful element of speech or writing, used with others (or sometimes alone) to form a sentence and typically shown with a space on either side when written or printed.',
            'word': 'Word'}
    col.insert_one(post)
    pprint.pprint(col.find_one({'word': 'Word'}))