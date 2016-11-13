import requests
from bs4 import BeautifulSoup
from Recipe import Recipe

def getRecipesFromURL(location, URL):
	r = requests.get(URL)
	r.text
	last_meal = ""
	last_category = ""
	recipes = []
	
	soup = BeautifulSoup(r.text, 'html.parser')
	rows = soup.select('tr div')
	date = soup.select('h2')[0].get_text().replace('Menus for ','')

	for x in rows:
		shortline = x.get_text().replace("\n","").strip()
		#if shortline.replace("\n","") != '':
			#print shortline

		if "class" in x.attrs:
			class_string = ".".join(x['class'])

			if 'cats' in class_string:
				last_category = shortline
				#print "#%s" %(shortline)

			if 'recipes' in class_string:
				recipes.append(Recipe(last_meal,last_category, shortline, date, location))
				#print "##%s" %(shortline)

		if "id" in x.attrs:
			#print "this has an id"
			#print x.get_text()
			id_string = x['id']

			if'meals' in id_string:
				last_meal = shortline
				#print "%s" %(shortline)
				
	return recipes
