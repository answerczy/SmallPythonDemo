# coding = utf-8

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
print (driver.title ) # 把页面title 打印出来
driver.quit()