#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

r = requests.get('https://vokasi.uns.ac.id/')

print(r)
print(r.text)


# In[14]:


import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.bukalapak.com/')

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.title)

print(soup.title.name)

print(soup.title.parent.name)


# In[2]:


import requests
from bs4 import BeautifulSoup

r = requests.get('https://proxyway.com/news')

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_= 'entry-content')
content = s.find_all('img')

print(content)


# In[20]:


import requests
from bs4 import BeautifulSoup
import csv

url = 'https://proxyway.com/news'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

images_list = []

images = soup.select('img')

for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})

for image in images_list:
    print(image)
    
with open('data gambar.csv' , 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    
    writer.writerow(images_list)


# In[11]:


import requests
from bs4 import BeautifulSoup
import csv

url = 'https://proxyway.com/news'
r = requests.get(url)

if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    paragraphs = soup.find_all('h2')
    
    with open('subjudul.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        
        for paragraph in paragraphs:
            writer.writerow([paragraph.text])
            print(paragraph.text)

else:
    print('Gagal mengambil halaman:', r.status_code)


# In[1]:


import requests
from bs4 import BeautifulSoup
import csv

url = 'https://proxyway.com/news'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    div_elements = soup.find_all('div', attrs={'data-widget_type': 'theme-post-excerpt.default'})

    if div_elements:
        
        with open('keterangan.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)

            for div_element in div_elements:
                inner_div = div_element.find('div', class_='elementor-widget-container')
                if inner_div:
                    text_content = inner_div.get_text(strip=True)
                    csvwriter.writerow([text_content])
                    print(text_content)
else:
    print(f'Gagal mengambil halaman. Status code: {response.status_code}')


# In[ ]:




