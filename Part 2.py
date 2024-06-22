from browsermobproxy import Server
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import csv
import json

# Read URLs from CSV (assuming URLs are in the second column)
urls = []
with open('top-1m.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        urls.append(row[1].strip())

# create a browsermob server instance
server = Server('browsermob-proxy\\bin\\browsermob-proxy')
server.start()
proxy = server.create_proxy(params=dict(trustAllServers=True))

# create a new chromedriver instance
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server={}".format(proxy.proxy))
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chrome_options)

maxCrawl = 1000
crawled = 0
skipped_error = 0
skipped_time = 0

folder_name = "Project 2\har"

# do crawling for each URL in the CSV
for url in urls:
    if crawled >= maxCrawl:
        break
    
    try:
        proxy.new_har("myhar", options={'captureCookies': True})
        driver.set_page_load_timeout(45)
        driver.get("http://"+url)
        
        file_path = f'{folder_name}{url.replace("://", "_").replace("/", "_")}.har'

        # write har file for each URL
        with open(file_path, 'w') as f:
            f.write(json.dumps(proxy.har))
        
        crawled += 1
    
    except TimeoutException as e:
        skipped_time += 1
        continue
    
    except Exception as e:
        skipped_error += 1
        continue

# stop server and exit
print(skipped_time)
print(skipped_error)
server.stop()
driver.quit()