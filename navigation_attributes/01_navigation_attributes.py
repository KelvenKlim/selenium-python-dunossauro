'''
    @copyright  (c) 2023 - Kelven Prasad. ALL RIGHTS RESERVED
    
    @brief      Selenium with Python - Eduardo Mendes, YouTube course

    @details    Learning Selenium with Python, how to get and navigate in attributes DOM using selenium
                Revising and improving my knowledge in Selenium with Python.

    @autor      Kelven Klim Barroso Prasad <kelven.jk14@gmail.com>

    @sice       Jul 20, 2023 
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

def find_by_text(browser, tag, text):
    """Find the element with the text `text`.

    Args:
        browser : Instance of browser [chrome, ...]
        text : Content thet must be in the tag
        tag : TAG where the text will be searched

    """
    elementos = browser.find_elements(By.TAG_NAME, tag )  # lista
    
    for elemento in elementos:
        if elemento.text == text:
            return elemento
    
 
def find_element_by_href(browser, link):
    """ Find the element `a` with the `link`

    Args:
        browser : Instance of browser [chrome, ...]
        link : link that will be looked for in all `a`
     """
    elementos = browser.find_elements(By.TAG_NAME, 'a')
     
    for elemento in elementos:
        href = elemento.get_attribute('href')
        if link in href:
            return elemento
 
    
browser = webdriver.Chrome()

url = "https://curso-python-selenium.netlify.app/aula_04_a.html"

browser.get(url)

# elemento_ddg = find_by_text(browser, 'a', 'DuckDuckGo')

elemento_ddg = find_element_by_href(browser, 'ddg')
