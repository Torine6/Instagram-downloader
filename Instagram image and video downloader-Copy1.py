#!/usr/bin/env python
# coding: utf-8

# In[36]:


get_ipython().system('pip install selenium')


# In[117]:


import os
import sys
os.path.dirname(sys.executable)


# In[118]:


path = r'C:\\Users\\VICTORINE\\anaconda3'


# In[119]:


from selenium import webdriver
browser = webdriver.Chrome('C:/Users/VICTORINE/Desktop/NEWFolder/chromedriver.exe')
browser.set_page_load_timeout(30)
browser.get('https://www.instagram.com/')


# In[120]:


browser.implicitly_wait(60)


# In[121]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# In[122]:


import urllib.request
url = 'https://www.instagram.com'
file_name = 'myfile.txt'
urllib.request.urlretrieve(url, file_name)


# In[65]:


pip install wget


# In[123]:


import wget


# In[124]:


# logging in to your account
user_name = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name ='username']")))
password = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name = 'password']")))

user_name.clear()
password.clear()
user_name.send_keys('vickiemj6')
password.send_keys('0740960629Vi')


# In[125]:


log_in = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


# In[126]:


not_now = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not now')]"))).click()


# In[127]:


not_now2 = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()


# In[128]:


# getting a hashtag
search_box = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
search_box.clear()
keyword = input('Enter hashtag: ')
search_box.send_keys(keyword)


# In[129]:


search_box.send_keys(Keys.ENTER)


# In[130]:


browser.execute_script("window.scrollTo(0, 5000);")

images = browser.find_elements(by=By.TAG_NAME, value='img')
images = [image.get_attribute('src') for image in images]


# In[131]:


# saving the images to your desktop
path = os.getcwd()
path = os.path.join(path, keyword[1:] + 's')

os.mkdir(path)
path


# In[132]:


counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1


# In[96]:


# the images have been downloaded successfully in your desktop

