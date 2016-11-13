class Recipe(object):
    def __init__(self,meal,category,title): #initial
        self.meal = meal
        self.category = category
        self.title = title

    def __str__(self): #string method
        return self.title
