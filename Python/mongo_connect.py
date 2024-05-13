from pymongo import MongoClient

mongo_connect_url = CONNECTION


def monngoDBConnection(connection):
    try:
        client = MongoClient(connection)    
        db = client['test']
        post_table = db['posts']
        documents = post_table.find() 
    # 'posts' tablosunun içeriğini yazdırıyoruz
        for document in documents:
            print(document)
    except Exception as err:
        print(err)
    

    
   
