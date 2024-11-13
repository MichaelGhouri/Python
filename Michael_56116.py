
# coding: utf-8

# In[1]:


import numpy as np

student_names = input("Enter student names separated by commas: ").split(',')
grades_input = input("Enter corresponding grades separated by commas: ").split(',')

# Convert grades to a NumPy array of integers
grades = np.array(grades_input, dtype=int)

#Ascending Order Sorting
grades_sort_asc = np.argsort(grades)
ascending_students = np.array(student_names)[grades_sort_asc]
ascending_grades = grades[grades_sort_asc]

print("\nSorted grades in ascending order:")
for i in range(len(ascending_students)):
    print(f"{ascending_students[i]}: {ascending_grades[i]}")

#Descending Order Sorting
grades_sort_desc = np.argsort(grades)[::-1]
descending_students = np.array(student_names)[grades_sort_desc]
descending_grades = grades[grades_sort_desc]

print("\nSorted grades in descending order:")
for i in range(len(descending_students)):
    print(f"{descending_students[i]}: {descending_grades[i]}")


# In[3]:


# Base Class: Product
class Product:
    def __init__(self, name, price, manufacturer):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
    
    def display_details(self):
        return f"Name: {self.name}, Price: ${self.price}, Manufacturer: {self.manufacturer}"

# Derived Class: ElectronicProduct
class ElectronicProduct(Product):
    def __init__(self, name, price, manufacturer, brand, model):
        super().__init__(name, price, manufacturer)
        self.brand = brand
        self.model = model
    
    def display_details(self):
        base_details = super().display_details()
        return f"{base_details}, Brand: {self.brand}, Model: {self.model}"

# Derived Class: ClothingProduct
class ClothingProduct(Product):
    def __init__(self, name, price, manufacturer, size, material):
        super().__init__(name, price, manufacturer)
        self.size = size
        self.material = material
    
    def display_details(self):
        base_details = super().display_details()
        return f"{base_details}, Size: {self.size}, Material: {self.material}"

# Derived Class: GroceryProduct
class GroceryProduct(Product):
    def __init__(self, name, price, manufacturer, expiry_date, quantity):
        super().__init__(name, price, manufacturer)
        self.expiry_date = expiry_date
        self.quantity = quantity
    
    def display_details(self):
        base_details = super().display_details()
        return f"{base_details}, Expiry Date: {self.expiry_date}, Quantity: {self.quantity}"

# Creating instances of each product type
electronic_product = ElectronicProduct(name="Laptop", price=1200, manufacturer="ABC Electronics", brand="TechBrand", model="X123")
clothing_product = ClothingProduct(name="T-Shirt", price=25, manufacturer="FashionCo", size="L", material="Cotton")
grocery_product = GroceryProduct(name="Milk", price=3, manufacturer="DairyFarm", expiry_date="2024-07-10", quantity="1L")

# Displaying the details of each product
print("Electronic Product Details:")
print(electronic_product.display_details())

print("\nClothing Product Details:")
print(clothing_product.display_details())

print("\nGrocery Product Details:")
print(grocery_product.display_details())

