class Recipe(object):
	def __init__(self, Meal, Category, Text, Date, Location):
		self.Meal = Meal
		self.Category = Category
		self.Text = Text
		self.Date = Date
		self.Location = Location
		
	def __str__(self):
		return self.Text
		
	def as_dict(self):
		return {
			'meal': self.Meal,
			'category' : self.Category,
			'text' : self.Text,
			'date' : self.Date,
			'location' : self.Location
		}

