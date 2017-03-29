import json
from pprint import pprint
from tkinter import filedialog
from os.path import basename

filename = filedialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file

filename = basename(filename)
with open(filename) as data_file:
	data = json.load(data_file)

def get_data(data):
	data_new =list(data.values())[0]
	properties = []
	locations = []
	addresses = []
	shop_names = []
	countries = []
	try:
		for d in data_new:
			properties.append(d['properties'])

		for p in properties:
			locations.append(p['Location'])

		location = locations[1:]
		for l in locations:
			items = list(l.items())
			for i in items:
				if(i[0]=='Address'):
					addresses.append(i[1])
				elif(i[0]=='Business Name'):
					shop_names.append(i[1])
				elif(i[0]=='Country Code'):
					countries.append(i[1])
		return ((properties, locations, addresses, shop_names, countries))
	except TypeError:
		data_new = list(data.values())[1]
		properties = []
		locations = []
		addresses = []
		shop_names = []
		countries = []
		for d in data_new:
			properties.append(d['properties'])

		for p in properties:
			locations.append(p['Location'])

		location = locations[1:]
		for l in locations:
			items = list(l.items())
			for i in items:
				if(i[0]=='Address'):
					addresses.append(i[1])
				elif(i[0]=='Business Name'):
					shop_names.append(i[1])
				elif(i[0]=='Country Code'):
					countries.append(i[1])
		return ((properties, locations, addresses, shop_names, countries))

(properties, locations, addresses, shop_names, countries) = get_data(data)

starred_places = list(zip(shop_names, addresses, countries))
starred_places = starred_places[:]
# print(starred_places)

print("These are the possible country codes:")
print(set(countries))
country = input("What country would you like to search? ")

country_recommendations = []
for s in starred_places:
	if(s[2] == country):
		country_recommendations.append(s)

print("These are your starred locations in %s" % country)
print(country_recommendations)
city = input("What city would you like to search? ")

city_recommendations = []
for c in country_recommendations:
	if(city in c[1]):
		city_recommendations.append(c)
	else:
		print("City not found")

print(city_recommendations)

# location = properties['Location']
# address = location['Address']
# name = location['Business Name']

# pprint(data_new)