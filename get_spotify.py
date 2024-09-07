import requests
from bs4 import BeautifulSoup

def getspotify(url):
    url=url.split("?")[0]
    # url="https://open.spotify.com/playlist/6onh6mpYQ9GSrfPtmeXZXV"
    response=requests.get(url)

    # with open('output.html','w',encoding='utf8') as f:
    #     f.write(response.text)

    soup=BeautifulSoup(response.text,"html.parser")
    tracks=soup.find_all("meta",{"name":"music:song"})
    ret=[]
    for i in tracks:
        # print(i['content'])
        track_url=i['content']
        # second time crawing
        trackres=requests.get(track_url)
        # print(trackres.status_code)
        stew=BeautifulSoup(trackres.text,"html.parser")
        song=stew.title.get_text()
        ret.append(song.replace(" - song and lyrics by "," ").replace(" | Spotify",""))
        # \r 把鼠標移至最前，\033[k = esc + [ + k 清除鼠標後的東西
        print("\r\033[K"+song.replace(" - song and lyrics by "," ").replace(" | Spotify",""),end='')
    return ret