__author__ = 'ryanstuntz'

import requests

# r = requests.get("http://www.azlyrics.com/d/drake.html")
# print r

from selenium import webdriver
link = "http://www.azlyrics.com/lyrics/asaprocky/1train.html"
driver = webdriver.Chrome()
# driver.get("http://www.azlyrics.com/d/drake.html")
# listAlbum = driver.find_element_by_id("listAlbum")
# links = listAlbum.find_elements_by_css_selector("a")
# lyric_links = []
# for link in links:
#     lyric = link.get_attribute("href")
#     if lyric and lyric[:19] == "http://www.azlyrics":
#         lyric_links.append(lyric)
# for link in lyric_links:
driver.get(link)
div = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[6]")
print div.text

driver.close()
