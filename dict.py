import requests
import json

API_KEY = "dict.1.1.20190803T170849Z.905cafe7990c2ee7.5e7643c5ec1bc2bbe01243c01fa0d46200f96bd8"
URL = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup"
ui="ru"

class Word():
    pass

    def __init__(self, *args, **kwargs):
        if kwargs.get("lang") and kwargs.get("text"):
            self.url="{0}?{1}&ui={2}&key={3}".format(URL,f"lang={kwargs['lang']}&text={kwargs['text']}", ui,API_KEY)
        else:
            print("Unknown text")

    def get_data(self):
        response=requests.get(self.url)
        if response.status_code == 200:
            self.result = response.json()
        else:
            self.result={}

    def create_response(self):
        dictionary=f"""Введенное слово - {self.result["def"][0]["text"]},
        часть речи - {self.result["def"][0]["pos"]}, род -
        {self.result["def"][0]["gen"]}, о/н - {self.result["def"][0]["anm"]}.
        \n Результат: перевод - {self.result["def"][0]["tr"][0]["text"]}, часть речи -
        {self.result["def"][0]["tr"][0]["pos"]}. \n Синонимы:
        {self.result["def"][0]["tr"][0]["syn"][0]["text"]}, часть речи -
        {self.result["def"][0]["tr"][0]["syn"][0]["pos"]}
        {self.result["def"][0]["tr"][0]["syn"][1]["text"]}, часть речи -
        {self.result["def"][0]["tr"][0]["syn"][1]["pos"]}
        \nЗначение:1 - {self.result["def"][0]["tr"][0]["mean"][0]["text"]}, 2 -
        {self.result["def"][0]["tr"][0]["mean"][1]["text"]}"""
        print(dictionary)

if __name__ == "__main__":
    obj=Word(lang="ru-en", text="вечер")
    #print(obj.url)
    obj.get_data()
    #print(obj.result)
    obj.create_response()





 #https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=API-ключ&lang=en-ru&text=time

        #"https://translate.yandex.net//api/v1.5/tr.json/translate"
        #obj.get_data()
        #print(obj.result)
