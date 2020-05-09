from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
name="hozier"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name('q').send_keys(name+"wikipedia")
driver.find_element_by_name('q').send_keys(Keys.ENTER)
#driver.find_element_by_css_selector("LC20lb DKV0Md").click()
#driver.find_element_by_id('viewport').click()
#try:
#    driver.find_element_by_css_selector("LC20lb DKV0Md").click()
#except NoSuchElementException:
#    print("hard luck!")
results = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
results[0].click()
url=driver.current_url
driver.close()

import matplotlib.pyplot as plt
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
temp=soup.find(class_="infobox")
links = soup.find_all(class_="image")
imgs=[i.find('img')['src'] for i in links]
desc=[i.find('img')['alt'] for i in links]
img=wget.download("https:"+imgs[1])

cnt=0
for my_table in temp:
    cnt += 1
    print ('=============== TABLE {} ==============='.format(cnt))
    rows = my_table.find_all('tr', recursive=False)
    
    k=0                  # <-- HERE
    for row in rows:
        cells = row.find_all(['th', 'td'], recursive=True)          # <-- HERE
        for cell in cells:
            print (cell.get_text())
        if k==0:
            new=plt.imread(img)
            plt.imshow(new) 
        if k%2==0:
            print('---')
        k+=1
