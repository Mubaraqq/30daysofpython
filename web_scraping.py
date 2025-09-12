    # web scraping - process of extracting and collecting data from website and stroring in a local machine or database
# we need requests and beautifulsoup4 packages and a website
# we target content from a website using html tags, classes or ids
import requests
from bs4 import BeautifulSoup

# declare url variable for the website we are going to scrape
url = 'https://www.worldometers.info/world-population/population-by-country//'

# use the requests get method to fetch the data from url
response = requests.get(url)
status = response.status_code
#print(status)

# using beautifulsoup to parse content from the page
# we get all the content from the website
content = response.content

# converts the HTML of the webpage into a BeautifulSoup object, making it easier to search for elements using tags/classes/ids
soup = BeautifulSoup(content, 'html.parser')
#print(soup.title)
#print(soup.title.get_text())
#print(soup.body) # gives whole page

# targeting the table with cellpadding atttribute with the vlaue of 3
table = soup.find('table', {'class': 'datatable'})
#print(table)

# finds all the tr elements inside the table
rows = table.find_all('tr')

# finds all the th element inside the table
th = table.find_all('th')

print(th)
for row in rows[:6]:
    print(row.get_text())
