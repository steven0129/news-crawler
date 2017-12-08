import random
import time
import csv
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

for page in range(1, 39):
    print('------------------Page' + str(page) + '-------------------')
    try:
        for index, article in enumerate(listArticle(driver, page)):
            try:
                time.sleep(random.uniform(0, 10))
                article['content'] = articleContent(driver, article['url'])

                with open('news.csv', 'a') as f:
                    fCSV = csv.writer(f)
                    temp = [article['title'], article['url'],article['content'].replace('\n', '<parp>')]
                    fCSV.writerow(temp)

                print('article index ' + str(index) + ' finish')   
            except:
                print('error at index ' + str(index))
    except:
        print('listArticle() error!')

driver.quit()
