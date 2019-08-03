import requests
import json

API_KEY = "trnsl.1.1.20190728T123649Z.b04c710df2b36c83.0f6fdaabe95efa825e2a8d91d18d7a5e5b39da5a"
URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"

class Word():
    pass

    def __init__(self, *args, **kwargs):
        if kwargs.get("lang") and kwargs.get("text"):
            self.url="{0}?{1}&key={2}".format(URL,f"lang={kwargs['lang']}&text={kwargs['text']}",API_KEY)
        else:
            print("Unknown text")


    def  get_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.result = response.json()
        else:
            self.result = {}

    def create_response(self):
        translate=f"Перевод заданного слова с {self.result['lang']} - {self.result['text']}"
        print(translate)

if __name__ == "__main__":
    obj=Word(lang="ru-ur", text="я пойду в кино сегодня вечером")
     #print(obj.url)
    obj.get_data()
    #print(obj.result)
    obj.create_response()







        #"https://translate.yandex.net//api/v1.5/tr.json/translate"
        #obj.get_data()
        #print(obj.result)
