# Import required libraries
import random
import pandas as pd
import os
from datetime import datetime, timedelta
import altair as alt

# Add color and size attributes to randomize for "Keyboard" object
colors = ["red", "yellow", "blue", "orange", "green", "purple", "white", "black", "grey"]
sizes = ["Full", "10KL", "60%"]

# Create Keyboard class with color and size parameters
class Keyboard:

    def __init__(self, color, size):

        self.color = random.choice(colors)
        self.size = random.choice(sizes)

        self.price = round(random.uniform(39.99, 109.99), 2)

# Create a string that returns color and size of keyboard object
    def __str__(self):
        return f'Color: {self.color}, Size: {self.size}'
        
# Create Inventory class to contain keyboards
class Inventory:

    def __init__(self):
        self.keyboards = []

        num_keyboards = random.randint(10, 20) # Generate a random number of keyboards between 10 and 20
        
# Creates a list of keyboards with randomly assigned color and size parameters
        for i in range(num_keyboards):
            color = random.choice(colors) # random color
            size = random.choice(sizes) # random size
            keyboard = Keyboard(color, size) # make a keyboard with random values
            self.keyboards.append(keyboard)

    def add_keyboard(self, keyboard): # Define logic to a Keyboard to the order
        self.keyboards.append(keyboard)

    def display_cart(self): # Display all keyboards in the order
        for keyboard in self.keyboards:
            print(keyboard)
            
# Create store class that references the Inventory class and contains a customer parameter
class Store:

    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.customers = []

        self.purchase = Purchase()

    def add_customer(self, customer):
        self.customers.append(customer)

    def getCustomers(self):
        for customer in self.customers:
         print("customer " + customer.getName() + " is currently shopping")

    # Print output stating the store name and customers
    def run(self):
        print("Welcome to " + self.name + "!!!")

        print("We have " + str(len(self.customers)) + " customers currently shopping.")

        for customer in self.customers:
            print("Customer " + customer.name + " is shopping.")
            
# Add a keyboard with random attributes to the cart object
            item = random.choice(self.inventory.keyboards)
            customer.add_to_cart(item)
            print("Customer " + customer.name + " added " + str(item) + " to their cart")

            self.purchase.increment(item.price)
            print("Customer " + customer.name + " cashed out and paid $" + str(item.price) + ".")
        print("The total sales for " + self.name + " today is $" + str(self.purchase.total) + ".")

# Create Customer class that references cart object
class Customer:

  def __init__(self, name):
      self.name = name
      self.cart = Cart()

  def getName(self):
        return self.name

  def add_to_cart(self, product):
      self.cart.add(product)

  def __str__(self):
        return self.name + " (" + str(self.order) + ")"
      
# Create Cart class that contains customer's products
class Cart:

  def __init__(self):
    self.products = []

  def add(self, product):
    self.products.append(product)

  def __str__(self):
    result = "Cart:\n"
    for product in self.products:
        result += str(product) + "\n"
    return result
      
# Create Purchase class that adds total purchase price
class Purchase:

  def __init__(self):
      self.total = 0

  def increment(self, price):
      self.total += price

  def __str__(self):
      return "Sale: $" + str(self.total)
      
# Create Corporation class that contains a store parameter
class Corporation:

  def __init__(self, name):
    self.name = name
    self.stores = []

    self.analytics = []

  def add_store(self, store):
    self.stores.append(store)
      
# Print stores in corporation
  def simulate(self):
    print("Welcome to " + self.name + "!")
    print("We have " + str(len(self.stores)) + " stores in our corporation.")

    for store in self.stores:
        
# Simulate the stores
        store.run()

    total_sales = 0
    for store in self.stores:
            total_sales += store.purchase.total # Adds the total sales from all stores

            dict_A = {"name":store.name, "total_sales":store.purchase.total}
            self.analytics.append(dict_A)
    print("The total sales for " + self.name + " today is $" + str(total_sales) + ".")

#Define variables for the analytics class

  def get_analytics(self):
        return self.analytics


  def display_analytics(self):
        for i in self.analytics:
            print(i)

  def __str__(self):
      result = self.name + "\n"
      for store in self.stores:
          result += str(store) + "\n"
      return result
# Create class analytics to produce csv files containing corporation data
class Analytics:

    def __init__(self):
        self.store_analytics = []

    def add_analytics(self, analytics):  #send collected store results
        self.store_analytics = analytics

    def make_csv(self):
        df = pd.DataFrame(self.store_analytics)
        print(df)
        entitle = "latest-store.csv"  # file title
        df.to_csv(entitle)


# List of stores
cities = ['Irvine', 'Tampa', 'Hamburg']
# Initialize an empty list to store dictionaries
weekly_totals_per_store = []

# Create dictionaries for each city
for city in cities:
    store_name = city
    weekly_sales_total = random.randint(99999, 1000000)
    store_dict = {'store_name': store_name, 'weekly_sales_total': weekly_sales_total}
    weekly_totals_per_store.append(store_dict)

# Create a Pandas DataFrame
df = pd.DataFrame(weekly_totals_per_store)

# Write the DataFrame to a CSV file
df.to_csv('weekly_sales.csv', index=False)

# Generate weekly sales data for each week in 2024
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
current_date = start_date

while current_date <= end_date:
    week_name = current_date.strftime('%B-%d-%Y')
    current_date += timedelta(days=7)  # Move to the next week

    print(current_date) #this should be the name of your csv

 # Write the DataFrame to a CSV file
    save_as = week_name.replace(' ', '-').lower() + '.csv'
    df.to_csv(save_as, index=False)

# Get the current directory
current_directory = os.getcwd()

# List all files in the current directory
all_files = os.listdir(current_directory)

# Filter only the CSV files
csv_files = [file for file in all_files if file.endswith('.csv')]

# Print the filenames
for filename in csv_files:
 print(filename)

# Initialize the master list
all_stores_all_weekly_sales = []  #global dataframe

# Read each CSV file, extract rows, and append to the master list
for filename in csv_files:
    df = pd.read_csv(filename)
    week_name = filename.replace('.csv', '')  # Extract week name from filename
    for _, row in df.iterrows():
        row_dict = row.to_dict()
        row_dict['week'] = week_name
        all_stores_all_weekly_sales.append(row_dict)

# Print the first few rows from the master list
print(all_stores_all_weekly_sales)

# Create a DataFrame from the list
df = pd.DataFrame(all_stores_all_weekly_sales)

# Print the DataFrame
print(df)


# Name the stores and corporation
store = Store("Worst Buy")
corp = Corporation("Worst Buy Co Inc.")

store1 = Store("Worst Buy, Irvine")
store2 = Store("Worst Buy, Tampa")
store3 = Store("Worst Buy, Hamburg")
corp.add_store(store1)
corp.add_store(store2)
corp.add_store(store3)

# Name the customers
customer1 = Customer("Mark")
customer2 = Customer("Ted")
customer3 = Customer("Daniel")
customer4 = Customer("David")
customer5 = Customer("Eve")
customer6 = Customer("Adam")
customer7 = Customer("Fred")
customer8 = Customer("Gary")
customer9 = Customer("Mary")
customer10 = Customer("Katie")

# Add the customers to stores
store1.add_customer(customer1)
store1.add_customer(customer2)
store2.add_customer(customer3)
store2.add_customer(customer4)
store2.add_customer(customer5)
store3.add_customer(customer6)
store3.add_customer(customer7)
store3.add_customer(customer8)
store3.add_customer(customer9)
store3.add_customer(customer10)

# Run the corporation simulation
corp.simulate()

corp.display_analytics()

# Create a csv file containing data from the corporation sales
analytic = Analytics()
analytic.add_analytics(corp.get_analytics())
analytic.make_csv()


names = ["Mark","Ted","Daniel","David","Eve","Adam","Fred","Gary","Mary","Katie"]
for i in range(len(names)):
    store.add_customer(Customer(names[i]))

store.getCustomers()

store.run()

# Define the width and height
width = 800  # Set the width 
height = 300  # Set the height

# Create a base line chart with specified width and height
base = alt.Chart(df, width=width, height=height).mark_line().encode(
    x='week:T',
    y='weekly_sales_total:Q',
    color='store_name:N',
    tooltip=['store_name:N', 'weekly_sales_total:Q', 'week:T']
).interactive() # Adds ability to zoom and interact with the chart

# Display the chart
base
