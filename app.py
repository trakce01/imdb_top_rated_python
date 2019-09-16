from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

web_browser = webdriver.Chrome(executable_path='WEBDRIVER_LOCATION')
web_browser.get('https://www.imdb.com/chart/top?ref_=nv_mv_250')
timeout=20
try:
    WebDriverWait(web_browser, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, 'lister-list')))
    movie_titles_element=web_browser.find_elements_by_class_name('titleColumn')
    movie_title = [title.text for title in movie_titles_element]
    for t in movie_title:
        print(t)

except TimeoutException:
    print('Timeout')
    web_browser.quit()