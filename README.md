**Web Scraping Methods**
==========================

### Method 1: Using requests, and BeautifulSoup
```python
import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = "https://www.example.com"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the specific data you want to scrape
title = soup.find('title').text
print(title)

# Find all links on the page
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
```

### Method 2: Using Scrapy
```python
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = [
        'https://www.example.com',
    ]

    def parse(self, response):
        title = response.css('title::text').get()
        yield {
            'title': title,
        }
```


### Method 3: Using Selenium
```python
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")

# Find the specific data you want to scrape
title = driver.find_element_by_tag_name('title').text
print(title)

# Close the browser
driver.quit()
```


**Real Life Example (Scraping reviews from IMDB website)**
==========================
```python
# Install the required packages
!pip install selenium
!apt-get update
!apt-get install -y chromium-chromedriver

# Import the required libraries
from selenium import webdriver
from bs4 import BeautifulSoup

# Create a new instance of the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options) # Use options argument instead of chrome_options

# Navigate to the webpage
driver.get("https://www.imdb.com/title/tt0111161/reviews")

# Get the page source
page_source = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Extract the reviews texts by iterating through all review divs
reviews = soup.find_all('div', {'class': 'review-container'})
for review in reviews:
    print(review.text)

# Close the browser
driver.quit()
```

