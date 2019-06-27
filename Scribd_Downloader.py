import bs4 as bs
from selenium import webdriver
from urllib import request
import os
import re
import img2pdf

browser = webdriver.Chrome()
url = https://es.scribd.com/document/358853751/3ro-BGU-Emprendimiento-y-Gestin-Texto-Del-Estudiante-12062017-B
browser.get(url)
source = browser.page_source

soup = bs.BeautifulSoup(source,"lxml")
images =[]

for element in soup.find_all('div', attrs={'class':"ie_fix"}):
    try:
     images.append(element.find('img').get('src'))
    except:
        pass


downloader = request.URLopener()
path = 'C:/Users/Vishal/Desktop/PYTHON BEST/'
name = url.split('/')[5][0:-23]

newpath = path+name


if not os.path.exists(newpath):
    os.mkdir(name)

for image in images:
    image_name = image.split('/')[-1]
    pattern = r"(([0-9]+))"
    match = re.search(pattern, image_name)
    try:
     global page
     page = match.group()


    except:
        pass

    downloader.retrieve(image,newpath+'/'+page+'.jpg')

with open('output.pdf',"wb") as f:
    f.write(img2pdf.convert([newpath+'/'+image for image in os.listdir(newpath) if image.endswith('.jpg')]))
