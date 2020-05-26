import urllib.request
from bs4 import BeautifulSoup

url = 'http://lol.inven.co.kr/dataninfo/champion/'
req = urllib.request.Request(url)
res = urllib.request.urlopen(url).read()

soup = BeautifulSoup(res, 'html.parser')
images = soup.find_all("div", {"class":"champImage"})
names = soup.find_all("div", {"class":"champName"})

image_url = []
image_name = []

for single_image in images :
    image_url.append(single_image.find("img")['src'])


for single_champ in names :
    image_name.append(single_champ.text)

for i in range(len(image_name)) :
    urllib.request.urlretrieve(image_url[i], 'champ images/'+image_name[i]+".jpg")



