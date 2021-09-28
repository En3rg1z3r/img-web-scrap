from posix import sched_param
from selenium import webdriver
import os 
import urllib
import urllib.request
import time

driverPath = r"/home/dedsec/img-web-scrap/chromedriver" #insert your chromedriver path here 

linkPrefix = "https://www.google.com/search?q="
linkSuffix = "&sxsrf=AOaemvJltkJx9YryOUmZYZwu6cdhVjOFQw:1631437222344&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjSmfGgifnyAhXBzKQKHYigArgQ_AUoAXoECAEQAw&biw=952&bih=968" #can be changed

saveFolder = "Raw_Data/"


def main() : 
    if not os.path.exists(saveFolder):
        os.mkdir(saveFolder)
    downloadImages(saveFolder)

def downloadImages(saveFolder):
    searchTerm = input("search for : ")
    saveFolder += searchTerm +"/" 
    if not os.path.exists(saveFolder):
        os.mkdir(saveFolder)
    #searchTerm += " food" for more accurate result , add custom keywords 
    n_images = int(input("how many images do you want : "))
    url = linkPrefix+searchTerm+linkSuffix
    driver = webdriver.Chrome(driverPath)
    driver.get(url)

    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        try:
            driver.find_element_by_xpath(
            """//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input""").click() #auto click on "load more" 
        except:
            pass
        if lastCount==lenOfPage:
            match=True

    
        
    
    elm1 = driver.find_element_by_id('islmp')
    sub = elm1.find_elements_by_tag_name('img')
    j = 0
    for i in sub: 
        if j< n_images:
            src= i.get_attribute('src')
            try:
                if src != None :
                    src =  str(src)
                    print(src)
                    urllib.request.urlretrieve(src, os.path.join(saveFolder, searchTerm+str(j)+'.jpg'))
                    j+=1
                else: 
                    #raise TypeError
                    pass
            except Exception as e:
                print("failed" + e)
    
    driver.close()


if __name__ == '__main__':
    print("welcome")
    main()

