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

# Iterate through the tables and add the 
for row in table : 
	# Grab name
	name = row.contents[1].a.string; 

	# Grab title and city
	raw = row.contents[3].find_all('a');
	
	# Skip the header of the table
	if(len(raw) != 2) :
		continue;

	# Grab police title
	title = raw[0].string

	# Grab just the city
	cityRaw = raw[1].string.split(',');
	city = cityRaw[0] # Just the city not the year

	print("Name: " + name + ", Title: " + title, ", City: " + city);
	