from bicycles import *

# Wheels
bouncy = Wheel(10, 18, "bouncy")
flat = Wheel(10, 1, "flat")
fat = Wheel(12, 25, "fat")

# Frames
modern = Frame("steel", 21, 100, "modern")
classic = Frame("aluminum", 8, 80, "classic")
professional = Frame("carbon", 5, 350, "professional")

# Manufacturers (need to add models)
schwinn = Manufacturer("Schwinn", .15, [])
acme = Manufacturer("Acme", .10, [])

# Models.  Note: need to associate manufacturers with models!!!
bruiser = Model(flat, modern, "Bruiser", schwinn)
speedy = Model(bouncy, classic, "Speedy", schwinn)
fatty = Model(fat, modern, "Fatty", acme)
turbo = Model(bouncy, professional, "Turbo", acme)

# Shops
cool_shop = Shop("Cool Shop", .20)
cool_shop.buy_bikes(bruiser, speedy, fatty, turbo)

# Customers
Moe = Customer("Moe", 1000)
Curly = Customer("Curly", 500)
Larry = Customer("Larry", 150)
customers = [Moe, Curly, Larry]

# Print shop inventory:
cool_shop.display_inventory()

# Print customer options:
for customer in customers:
	customer.display_affordable_bikes(cool_shop)

cool_shop.sell_bike(bruiser, Moe)
cool_shop.sell_bike(fatty, Curly)
cool_shop.sell_bike(turbo, Larry)
cool_shop.sell_bike(speedy, Larry)

cool_shop.display_inventory()
print "{}'s profit is ${}".format(cool_shop.name, cool_shop.profit)
        
    
    
   
    
