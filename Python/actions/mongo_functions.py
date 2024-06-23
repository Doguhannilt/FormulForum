from pymongo import MongoClient



def get_collection_names(mongo_url):
    try:
        # MongoDB'ye bağlan
        client = MongoClient(mongo_url)
        db = client.get_database()
        
        # Tablo isimlerini al
        collection_names = db.list_collection_names()
        
        # Başarılı ise [True, tablo isimleri] döndür
        return [True, collection_names]
    except Exception as e:
        # Hata durumunda [False] döndür
        return [False]



def read_table_data(mongo_url, table_name):
    try:
        # MongoDB'ye bağlan
        client = MongoClient(mongo_url)
        db = client.get_database()
        
        # Belirtilen tabloyu (koleksiyonu) seç
        collection = db[table_name]
        
        # Tabloyu (koleksiyonu) oku
        documents = list(collection.find())
        
        # Başarılı ise [True, tablo verileri] döndür
        return [True, documents]
    except Exception as e:
        # Hata durumunda [False] döndür
        return [False]