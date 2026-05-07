# The item's discount and stock status have been defined
discounted = False
lowStock = True
#Define a boolean variable movingProduct that is True if the item is either discounted or low in stock, using logical operators.
movingProduct = discounted or lowStock
#Create a boolean variable promotion that is True if the item is not discounted and sufficiently stocked (meaning the item is not low in stock).
promotion = not movingProduct
#Print the message: Is the item eligible for promotion? <promotion>.
print("Is the item eligible for promotion?" , promotion)