"""
Dictionary is one of collection data types.
It stores multiple values in Key-Value pairs

create dictionary using syntax : {key:value, key:value, key:value}

"""
###############################################################################################

car = {"Brand": 'Honda',
       "Model": 'Amaze',
       "Price": 900000,
       "Mileage": 14.5}

print(car)
# o/p : {'Brand': 'Honda', 'Model': 'Amaze', 'Price': 900000, 'Mileage': 14.5}

print(type(car))
# o/p : <class 'dict'>

###############################################################################################
# Get/retrieve the values with help of keys
# there are two ways for same purpose

print(car.get("Brand"))
print(car["Model"])

"""
o/p:
Honda
Amaze
"""
###############################################################################################
# print all keys of dictionary

car = {"Brand": 'Honda',
       "Model": 'Amaze',
       "Price": 900000,
       "Mileage": 14.5}
print(car.keys())

# o/p: dict_keys(['Brand', 'Model', 'Price', 'Mileage'])

###############################################################################################
# print all values of dictionary

car = {"Brand": 'Honda',
       "Model": 'Amaze',
       "Price": 900000,
       "Mileage": 14.5}
print(car.values())

# o/p: dict_values(['Honda', 'Amaze', 900000, 14.5])

###############################################################################################
# Update values of dictionary

car = {"Brand": 'Honda', "Model": 'Amaze', "Price": 15000000, "Mileage": 14.5}

print(car)

# o/p: {'Brand': 'Honda', 'Model': 'Amaze', 'Price': 15000000, 'Mileage': 14.5}

###############################################################################################
# Adding the new key
car = {"Brand": 'Honda', "Model": 'Amaze', "Price": 15000000, "Mileage": 14.5}

car["Colour"] = "Grey"

print(car)

# o/p: {'Brand': 'Honda', 'Model': 'Amaze', 'Price': 15000000, 'Mileage': 14.5, 'Colour': 'Grey'}

###############################################################################################
# Use of for loop in dictionary
car = {"Brand": 'Honda', "Model": 'Amaze', "Price": 15000000, "Mileage": 14.5}

# we can call keys using two ways

for k in car:                   # here always key is called
    print(k)

    # OR

for k in car.keys():
    print(k)

"""
o/p:
Brand
Model
Price
Mileage
"""

# for values

for v in car.values():
    print(v)
    
"""
o/p: 
Honda
Amaze
15000000
14.5
"""
###############################################################################################
# print key and values with help of retrieved keys

car = {"Brand": 'Honda', "Model": 'Amaze', "Price": 15000000, "Mileage": 14.5}

for k in car.keys():
    print("key is {} and value is {}".format(k, car.get(k)))

"""
o/p:
key is Brand and value is Honda
key is Model and value is Amaze
key is Price and value is 15000000
key is Mileage and value is 14.5
"""
###############################################################################################
# for printing items (key and value)

car = {"Brand": 'Honda', "Model": 'Amaze', "Price": 15000000, "Mileage": 14.5}

for k,v in car.items():
    print(k,v)

"""
o/p : 
Brand Honda
Model Amaze
Price 15000000
Mileage 14.5
"""
###############################################################################################
# Remove functions we can use with dictionary
car = {"Brand": 'Honda', "Model": 'Amaze', "Price": 15000000, "Mileage": 14.5}

# Two ways for Removing an item using the specific key from dictionary and returns the value of the removed key
# 1
car.pop("Model")
print(car)
# o/p: {'Brand': 'Honda', 'Price': 15000000, 'Mileage': 14.5}

# 2
del car["Price"]
print(car)
# o/p: {'Brand': 'Honda', 'Mileage': 14.5}

# To remove last key value pair
car.popitem()
print(car)
# o/p: {'Brand': 'Honda'}

# Remove all key value pair at a Go
car.clear()
print(car)
# o/p: {}

# Delete entire dictionary
del car
print(car)
# o/p: name 'car' is not defined

###############################################################################################
# Other functions in dictionary

car = {"Brand": 'Honda', "Model": 'Amaze', "Price": 15000000, "Mileage": 14.5}
print(len(car))

# o/p: 4

###############################################################################################
# Compare one dict with another dict

car1 = {"Brand": 'Honda', "Model": 'Amaze', "Price": 15000000, "Mileage": 14.5}
car2 = {"Brand": 'Tata', "Model": 'Nexon', "Price": 2000000, "Mileage": 20.5}

print(car1 == car2)
print(car1 != car2)

"""
o/p:
False
True
"""
###############################################################################################










