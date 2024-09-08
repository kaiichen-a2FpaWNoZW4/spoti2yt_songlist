from os import system

from spoti_to_yt import *

#https://open.spotify.com/playlist/6onh6mpYQ9GSrfPtmeXZXV
url = input("input spotify songlist :)")
title = input("input songlist name :)")
method = input("超過30首?(Y/n)")

if method=='Y':
    maxlen=int(input("maxlen:(最大199!)"))

print("spotify歌單->歌曲名稱...")
if method=='Y':
    songtitles = getspotify_dynamic(url,maxlen)
else:
    songtitles = getspotify(url)
print("done")

print("歌曲名稱->youtube連結...")
yturl = title_to_yturl(songtitles,"lyrics")
print("done")

print("連接youtube api...")
system("pause")
youtube=connect()
print("done")

print("創建合集...")
listId=create_yt_playlist(youtube,title)
print("done")

system("pause")

print("加入歌曲...")
for i in yturl:
    addsong(youtube,listId,i)
print("go ckeck ur youtube!!")
print("https://youtube.com/playlist?list="+listId)