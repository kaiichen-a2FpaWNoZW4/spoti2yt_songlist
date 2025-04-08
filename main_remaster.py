from os import system

from spoti_to_yt import *

print("1:get from spotify link(dynamic)")
print("2:get from spotify link(old ver)")
print("3:load from songlist.txt")
method=int(input())
songtitles=[]

if method==1 or method==2:
    url=input("input spotify songlist :)")
    mxlen=int(input("maxlen:(最大199!)"))
    if method==1: songtitles = getspotify_dynamic(url,mxlen)
    else: songtitles = getspotify(url)
    print("done1")
    f=open("songlist.txt","w",encoding='utf-8')
    for i in songtitles:
        f.write(i)
        f.write("\n")
    f.close()
    print("done2")

elif method==3:
    f=open("songlist.txt","r",encoding='utf-8')
    for i in f:
        songtitles.append(i)
    f.close()
    print("done")

print("歌曲名稱->youtube連結...")
yturl = title_to_yturl(songtitles,"lyrics")
print("done")

print("連接youtube api...")
system("pause")
youtube=connect()
print("done")

print("1:create new youtube playlist")
print("2:add to existed playlist")
method=int(input())
if(method==1): 
    title = input("input songlist name :)")
    print("創建合集...")
    listId=create_yt_playlist(youtube,title)
    print("done")

else: 
    listId=input("input playlist lintId")

st=int(input("start from which song:"))
print("加入歌曲...")
for i in range(st,len(yturl)):
    addsong(youtube,listId,yturl[i])

print("go ckeck ur youtube!!")
print("https://youtube.com/playlist?list="+listId)
system("pause")


