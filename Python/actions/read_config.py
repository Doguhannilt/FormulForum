import os, json


def MainConfig(config_path):
    # Dosyanın varlığını kontrol etme
    if not os.path.exists(config_path):
        # Boş bir yapı ile config dosyası oluşturma
        default_config = {
            "email": "",
            "password": "",
            "mongo_connect_url": "",
            "table1": "",
            "table2": ""
        }
        
        #Config dosyası yok ise oluşturup, içerisine default değerleri atıyoruz
        with open(config_path, 'w') as config_file:
            json.dump(default_config, config_file, indent=4)

    #dosyanın var olduğu durumda içerisindeki değerleri okuyoruz
    result = ReadConfig(config_path)

    is_null = False
    #Bu değerlerin doluluğunu kontrol ediyoruz
    for value in result:
        if len(value) <= 0:
            is_null = True
    
    return [is_null, result]

def ReadConfig(config_path):
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)

        email = config.get("email")
        password = config.get("password")
        mongo_connect_url = config.get("mongo_connect_url")
        table1 = config.get("table1")
        table2 = config.get("table2")

        return [email, password, mongo_connect_url, table1, table2]
    except Exception as err:
        print(err)
        return ["", "", "", "", ""]
    
def SaveSettings(config_path, email, password, mongo_connect_url, table1, table2):
    try:
        if not os.path.exists(config_path):
            default_config = {
                "email": "",
                "password": "",
                "mongo_connect_url": "",
                "table1": "",
                "table2": ""
            }
            
            with open(config_path, 'w') as config_file:
                json.dump(default_config, config_file, indent=4)

        new_config = {
            "email": email,
            "password": password,
            "mongo_connect_url": mongo_connect_url,
            "table1": table1,
            "table2": table2
        }

        with open(config_path, 'w') as config_file:
            json.dump(new_config, config_file, indent=4)

        return [True]
    except Exception as err:
        return [False, err]