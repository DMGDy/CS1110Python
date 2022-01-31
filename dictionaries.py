#declaring dictionar
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)


#dictionaries in key:value pairs, can index with keyname
print(thisdict["brand"])

#dictionaries are not changable/mutable or duplicatable
#dictionaries can not have multiple keys of the same name
#dictionary length, each element is 1
print(len(thisdict))

#dictionary can contain multiple data types (lists, int, boolean)

thisdict ={
    "brand":"Ford",
    "electric": False,
    "year": 1964,
    "colors":['red', 'white','blue']
}
print(thisdict)

#dictionaries have type 'dict'
print(type(thisdict))


##dictionary methods

#clear() removes all elements from the dictionary

print(thisdict.clear())

thisdict ={
    "brand":"Ford",
    "electric": False,
    "year": 1964,
    "colors":['red', 'white','blue']
}


#copy() allows to assign dictionary to another variable

x = thisdict.copy()
print(x)


#fromkeys() returns dictionary with the specified keys and specified value
#dict.fromkeys(keys, value)
x = ('key1','key2','key3')
y = 0

exdict = dict.fromkeys(x, y)
print(exdict)

#from keys without specifying value, returns None instead of 0
thisdict = dict.fromkeys(x)
print(thisdict)


#get() method returns value of the key given in argument, does not return keyname
#dictname.get(keyname, value) value is an optional argument
thisdict ={
    "brand":"Ford",
    "model": "Mustang",
    "year": 1964,
    "colors":['red', 'white','blue']
}
x = thisdict.get("model")
print(x)
x = thisdict.get("year", 1964)
print(x)


#items() method returns key-pair values
#no arguments
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
#if value changes, variable acts as pointer to dictionary
car["year"] = 2018
print(x)


#keys() returns keys of the dictionary in a list
x = car.keys()
print(x)
#similar to items, also will be updated to change

#pop() method will delete specified value given a key
#pop(keyname, defaultvalue) where default value is returned if the given key does not exist
x = car.pop("model")
#if printed, will return deleted value but not key
print(x)
print(car)

#popitem() will delete the item atop the stack of the dictionary
#no arguments given
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.popitem()
print(car)
x = car.popitem()
#if assigned to variable and deleted, will return the dictionary
print(x)


#setdefault() method returns the value with the specified key
#if the key does not exist insert the key with the specified value
#dictname.setdefault(keyname,)
car = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
}
x = car.setdefault("model","Bronco")
print(x)



