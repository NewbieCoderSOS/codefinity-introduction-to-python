# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")



#Calculate the revenue for each product by multiplying the price by the quantity sold, and store all results in a new list called revenue
revenue = prices[i] * quantities_sold[i] for


#Use the zip() function to combine the products and revenue lists into a list of tuples named revenue_per_product, where each tuple contains a product name and its corresponding revenue

#Sort the revenue_per_product list alphabetically by product name

#Print each product and its revenue using this format: <product_name> has total revenue of $<revenue>