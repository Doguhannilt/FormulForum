from bs4 import BeautifulSoup
import requests 
import json
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)

url = "UNIVERSITY_DATABASE_URL"

try:
    httpRequest = requests.get(url=url,verify=False)   
except Exception as e:
    print(f"ERROR: {e}") 

def getUniversities():
    html = httpRequest.text
    parsedHtml = BeautifulSoup(html,"html.parser")

    all_unilist=parsedHtml.find_all("div",{"class":"row uniListItem"})

    universities = []

    for uni in all_unilist:
        if uni.find("span",{"class":"sehir"}).text == "İstanbul":
            
            uni_data = {}
            uni_data['isim'] = uni.find("h3").text

            logos = uni.find_all("img",{"col-md-2 logo"})
            hrefs = uni.find_all("a")
    
            header = 'URL_HEADER'
            uni_data['logo'] = [header + i['src'] for i in logos]
            uni_data['link'] = [i['href'] for i in hrefs if i['href'] != "#universiteModal"]

            universities.append(uni_data)
            

    for uni in universities:
        print(f"name: {uni['isim']}")
        for logo in uni['logo']:
            print(f"Logo: {logo}")
        for link in uni['link']:
            print(f"Link: {link}")
        print("-" * 30)              
            
                    
    with open('universities.json','w', encoding='utf-8') as f:
        json.dump(universities, f ,ensure_ascii=False,indent=4)

    
            
getUniversities()
         
         
   
     









