import requests
from recipe import Recipe

r = requests.get('https://campusdining.princeton.edu/dining/_Foodpro/menuSamp.asp?locationNum=02&amp;locationName=Butler+%26+Wilson+Colleges&amp;sName=Princeton+University+Campus+Dining&amp;naFlag=1')
r.text

with open("page.html","w") as f:
    f.write(r.text)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser") #creating a file with the html of the webpage
#print soup

soup.find_all('table') #search by tag

soup.select("#menusampprices") #ids are unique
soup.select(".menusampprices") #search by CSS selector (class name to identify what data represents) #id 	Selects the element with id="firstname"

#tr = row, td = cell, iterate over all of them, for each of them print out the .get text

rows = soup.select("tr div")
cols = soup.select("td")

last_meal = ""
last_category = ""
recipes = []

for x in rows:
    shortline = x.get_text().replace("\n","").strip() #.strip() gets rid of leading and trailing  space, .strip("") would get rid of quotation marks
    #if shortline.replace("\n","") != '':
        #print shortline

    if "class" in x.attrs: #checking if the tag has a class
        class_string = ".".join(x['class']) #joins every element in the class array together

        if 'cats' in class_string: #if meals is in the class name
            last_category = shortline
            #print "#%s" %(shortline) #print a hash before the string

        if 'recipes' in class_string:
            recipes.append(Recipe(last_meal,last_category,shortline)) #create an array of the recipe names
            #print "##%s" %(shortline)

    if "id" in x.attrs:
        #print "this has an id"
        #print x.get_text()
        id_string = x['id']

        if'meals' in id_string:
            last_meal = shortline
            #print "%s" %(shortline)

for x in recipes:
    print x
