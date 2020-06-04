from bs4 import BeautifulSoup
import requests
import pandas as pd
# Creating a header that looks like a browser to spoof site
headers = requests.utils.default_headers()
# headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

# Create dataframe for police info
column_names = ["Name", "Title", "City"]
police_df = pd.DataFrame(columns=column_names);

for pageNum in range(1,139) :
	# CA police salary page from 2019
	if(pageNum == 1) :
		url = "https://transparentcalifornia.com/salaries/search/?q=Police&a=&y=2019"
	else : 
		url = "https://transparentcalifornia.com/salaries/search/?q=Police&a=&y=2019&page=" + str(pageNum)
	req = requests.get(url, headers);
	soup = BeautifulSoup(req.content, 'html.parser');
	# print(soup.prettify());

	# Find all the rows of the table
	table = soup.find_all("tr");

	# Iterate through the tables and add the 
	items = 0

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

		# Formatting the data for the dataframe
		row = {"Name": [name], "Title:": [title], "City": [city]};
		data = pd.DataFrame(data=row);
		police_df = police_df.append(data, ignore_index=True);
		items += 1;



	print("Page " + str(pageNum) + " done! " + str(items) + " rows");

police_df.to_csv("../data/police_data.csv");
print(len(police_df.index));
		