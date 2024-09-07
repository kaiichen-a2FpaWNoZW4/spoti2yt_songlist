import requests 
import re
from tqdm import tqdm
import threading

# url encode!!!
import urllib.parse

ret=[]
lock=threading.Lock()

def req(url):
    global ret
    response=requests.get(url)

    # {"url":"/watch?v=10DHUqSVu6I\u0026pp=ygUkVkggKFZhc3QgJiBIYXp5KSD...
    res=re.search(r"watch\?v=(.+?)\\",response.text)
    a=res.group(1)
    if len(a)==11:
        lock.acquire()
        ret.append(a)
        print(a)
        lock.release()
    else:
        print("something went wrong...")
        # with open("output.html","w") as f:
        #     f.write(response.text)

    return

def title_to_yturl(query: list,addition: str):
    threads=[]
    addition=urllib.parse.quote(addition)
    for q in tqdm(query):
        if q=='': continue
        q=urllib.parse.quote(q)
        if addition!='': q=q+'+'+addition
        url="https://www.youtube.com/results?search_query="+q
        threads.append(threading.Thread(target=req , args=(url,)))

        # print(url)
        # 獲取原始碼
    
    cnt=0
    while cnt<len(threads):
        for i in range(cnt,min(cnt+50,len(threads))):
            threads[i].start()
        for i in range(cnt,min(cnt+50,len(threads))):
            threads[i].join()
        cnt+=50

    return ret

if __name__=='__main__':
    # print(title_to_yturl(['VH (Vast & Hazy) 與浪之間'],"lyrics"))
    print(urllib.parse.quote('VH (Vast & Hazy) 與浪之間'))