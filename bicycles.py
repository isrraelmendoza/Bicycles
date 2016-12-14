class Wheel(object):
	def __init__(self, weight, cost, name):
		self.weight = weight
		self.cost = cost
		self.model_name = name

class Frame(object):
	def __init__(self, material, weight, cost, name):
		self.material = material 
		self.weight = weight
		self.cost = cost
		self.name = name

class Model(object):
	def __init__(self, wheel, frame, name, manufacturer):
		self.wheel = wheel
		self.frame = frame
		self.name = name
		self.manufacturer = manufacturer
		self.weight = self.frame.weight + (self.wheel.weight * 2)
		self.production_cost = self.frame.cost + (self.wheel.cost * 2)

class Manufacturer(object):
	def __init__(self, name, markup, models):
		self.name = name
		self.markup = markup
		self.models = models

class Shop(object):
	def __init__(self, name, markup):
		self.name = name
		self.markup = markup
		self.inventory = []
		self.profit = 0

	def display_inventory(self):
		print "{}'s inventory is:".format(self.name)
		for model in self.inventory:
			print model.name + " for sale!"
			print " -Price: {}".format(model.retail_cost)
			print " -Weight: {} pounds".format(model.weight)
		print "\n"

	def buy_bikes(self, *models):
		for model in models:
			self.inventory.append(model)
			model.wholesale_cost = model.production_cost * ( 1 + model.manufacturer.markup)
			model.retail_cost = model.wholesale_cost * (1 + self.markup)
			self.profit -= model.wholesale_cost

	def sell_bike(self, model, customer):
		self.inventory.remove(model)
		customer.owned_bikes.append(model)
		customer.fund -= model.retail_cost
		self.profit += model.retail_cost
		print "{} just bought a {} for ${} dollars.".format(customer.name, model.name, model.retail_cost)
		print "{} has ${} left.\n".format(customer.name, customer.fund)

class Customer(object):
	def __init__(self, name, fund):
		self.name = name
		self.fund = fund
		self.owned_bikes = []

	def display_affordable_bikes(self, shop):
		print "Showing models {} can afford".format(self.name)
		for model in shop.inventory:
			if model.retail_cost < self.fund:
				print " -" + model.name
		print "\n"