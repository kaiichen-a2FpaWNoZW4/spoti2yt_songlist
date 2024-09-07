import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

def getspotify_dynamic(url,maxlen):
    driver = webdriver.Chrome('./chromedriver')    # 指向 chromedriver 的位置
    driver.get(url)           # 打開瀏覽器，開啟網頁
    time.sleep(2)
    ele=[]
    cnt=0
    while 1:    #Big Loop
        flg=0
        a=driver.find_elements(By.CLASS_NAME,"j2s64Lz8y6VzBLB_V9Gm")
        #播放 ... 的button 的 class 

        for song in a:
            # print(song.get_attribute('aria-label'))
            ret=song.get_attribute('aria-label').replace(' 的 ',' ')[3:]
            if (ret not in ele) and ret != '':
                flg=1
                cnt+=1
                ele.append(ret)
                print(ret)
                if maxlen<=cnt:
                    break

        if maxlen<=cnt or flg==0:
            break

        a[-1].send_keys(Keys.PAGE_DOWN)
        a[-1].send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        # print(*ele,sep='\n')
        print("scroll:)",cnt)
        # driver.execute_script("window.scrollBy(0, 3000)",a[0]) not working

    # print(*ele,sep='\n')
    # os.system("pause")
    print(f"find {len(ele)} songs")
    return ele

if __name__=='__main__':
    a=getspotify_dynamic('https://open.spotify.com/playlist/0CaEAMM4yAWiAYNU2roSGj',100)