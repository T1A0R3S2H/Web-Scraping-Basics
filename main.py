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
