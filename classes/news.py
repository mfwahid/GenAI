import json
import requests
import datetime

class News:
    def __init__(self,apikey,country,category):
        self.apikey = apikey
        self.country = country
        self.category = category


    def get_topnewsbycountrycategory(objnews):
        url = ('https://newsapi.org/v2/top-headlines?'
            'country='+objnews.country+'&'+'category='+objnews.category+'&'
            'apiKey='+objnews.apikey)

        #print("url:" + url)
        response = requests.get(url)
        content = response.content
        output = json.loads(content)
        #print(output)
        return output['articles']
    
    def getcontentJSON(objnews,content,type):
        data ={
            "category":objnews.category,
            "country":objnews.country,
            "newstype":type,
            "date": datetime.datetime.now().isoformat(),
            "content":content
        }
        #json_data = json.dumps(data)
        return data
