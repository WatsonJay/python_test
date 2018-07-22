import pymongo
client = pymongo.MongoClient('106.14.220.77',27017)
mydb = client['mydb']
test = mydb['test']
test.insert_one({'name':'Jan','sex':'男','grande':89})