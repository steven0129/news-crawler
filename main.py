import random
import time
from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()
driver = webdriver.Firefox()


def listArticle(driver, page):
    result = []
    driver.get('http://news.ltn.com.tw/list/breakingnews/all/' + str(page))
    for elem in driver.find_elements_by_class_name('tit'):
        result.append({'title': elem.find_element_by_tag_name(
            'p').text, 'url': elem.get_attribute('href')})

    return result


def articleContent(driver, url):
    driver.get(url)
    elem = driver.find_element_by_css_selector('[itemprop="articleBody"]')
    return elem.text


driver.maximize_window()

temp = []
for index, article in enumerate(listArticle(driver, 1)):
    time.sleep(random.uniform(0, 2))
    article['id'] = index
    article['content'] = articleContent(driver, article['url'])
    temp.append(article)
    print(temp)

driver.quit()
