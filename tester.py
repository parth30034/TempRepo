#This snippet automates the login process to Facebook
# For more details refer https://sites.google.com/a/chromium.org/chromedriver/getting-started
from selenium import webdriver #selenium is used to automate web browser tasks

username='userkid@fairytale.com'    #enter your email id
password='noobmaster69'             #enter password

url='https://www.facebook.com/'     #Enter the url to the website , in this case facebook

driver=webdriver.Chrome(r"Path to the executable chromedriver_File") #copy the path of executable chromedriver file

driver.get(url)   #directs the chrome browser to the "url"
driver.find_element_by_id('email').send_keys(username)   #finds element by id with name 'email' and feeds 'username' using sendkeys function
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()      #clicks the elemnt loginbutton
