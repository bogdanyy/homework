from threading import Thread
import requests
from datetime import datetime


def executor(url,index):
  print("start",index)
  result=requests.get(url)
  print("finish",index)


if __name__ == "__main__":
    urls =[
        "https://dictionary.yandex.net",
        "https://dictionary.yandex.net",
        "https://dictionary.yandex.net",
        "https://dictionary.yandex.net",
        "https://dictionary.yandex.net"
    ]
    start = datetime.now()
    workers = [Thread (target=executor, args=(urls[index],index)) for index in range(len(urls))]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    finish = datetime.now()
    print(finish-start)
