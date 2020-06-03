from bs4 import BeautifulSoup
import requests

# Creating a header that looks like a browser to spoof site
headers = requests.utils.default_headers()
# headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

# CA police salary page from 2019
url = "https://transparentcalifornia.com/salaries/search/?q=Police&a=&y=2019"
req = requests.get(url, headers);
soup = BeautifulSoup(req.content, 'html.parser');
# print(soup.prettify());

# Find all the rows of the table
table = soup.find_all("tr");
print(table);