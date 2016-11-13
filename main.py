import json
from TigerMealAPI import getRecipesFromURL

recipes = []
recipes.extend( getRecipesFromURL('Rockefeller & Mathey Colleges', 'https://campusdining.princeton.edu/dining/_Foodpro/menuSamp.asp?locationNum=01&locationName=Rockefeller+%26+Mathey+Colleges&sName=Princeton+University+Campus+Dining&naFlag=1') )
recipes.extend( getRecipesFromURL('Butler & Wilson Colleges', 'https://campusdining.princeton.edu/dining/_Foodpro/menuSamp.asp?locationNum=02&amp;locationName=Butler+%26+Wilson+Colleges&amp;sName=Princeton+University+Campus+Dining&amp;naFlag=1') )
recipes.extend( getRecipesFromURL('Forbes College', 'https://campusdining.princeton.edu/dining/_Foodpro/menuSamp.asp?locationNum=03&amp;locationName=Forbes+College&amp;sName=Princeton+University+Campus+Dining&amp;naFlag=1') )
recipes.extend( getRecipesFromURL('Whitman College', 'https://campusdining.princeton.edu/dining/_Foodpro/menuSamp.asp?locationNum=08&amp;locationName=Whitman+College&amp;sName=Princeton+University+Campus+Dining&amp;naFlag=1') )
recipes.extend( getRecipesFromURL('Center for Jewish Life', 'https://campusdining.princeton.edu/dining/_Foodpro/menuSamp.asp?locationNum=05&amp;locationName=Center+for+Jewish+Life&amp;sName=Princeton+University+Campus+Dining&amp;naFlag=1') )

dictionaries = []
    
for d in recipes:
	dictionaries.append(d.as_dict())
	
with open('dictionaries.json', 'w') as f:
	f.write(json.dumps(dictionaries))

print json.dumps(dictionaries, indent=2, sort_keys=True)


