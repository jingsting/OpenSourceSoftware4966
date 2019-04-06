from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
import datetime
client = MongoClient('mongodb://localhost:27017/')


def random_word_requester(col):
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    record = col.aggregate([{ '$sample': { 'size': 1 } }])
    word = [one for one in record][0]['word']
    return word


if __name__ == '__main__':
    db = client['mongo_db_lab']
    col = db['definitions']
    
    while True:
        word = random_word_requester(col)
        print(word)
        col.update_one({'word':word}, {'$push':{'dates': datetime.datetime.utcnow()}})
        newword = col.find_one({'word':word})
        print(newword)
        if len(newword['dates']) > 1:
            print('found duplicate')
            break