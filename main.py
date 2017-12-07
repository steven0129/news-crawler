from io import BytesIO
from PIL import Image
from selenium import webdriver
from pyvirtualdisplay import Display


def listArticle(driver, page):
    result = []
    driver.get('http://news.ltn.com.tw/list/breakingnews/all/' + str(page))
    for elem in driver.find_elements_by_class_name('tit'):
        result.append(elem.get_attribute('href'))

    return result


display = Display(visible=0, size=(1024, 768))
display.start()

driver = webdriver.Firefox()
driver.maximize_window()
print(listArticle(driver, 2))

driver.quit()
