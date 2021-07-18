try:
    from googlesearch import search
    from selenium import webdriver
except ImportError:
   print("No module named 'google' found!!!\n")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# to search
query = "دانلود vikings"

for sites in search(query, tld="co.in", num=1, stop=1, pause=2):
    print(sites)
    driver.get(sites)

driver.close()
#close chrome
#driver.quit()