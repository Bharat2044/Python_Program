d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
};
print(d);
print(type(d));

# length
print(len(d));

# Dictionary Items
print(d["brand"])

print();

# dict() Constructor
d = dict(name = "John", age = 36, country = "Norway")
print(d);

# print keys
print(d.keys());

# print values
print(d.values());

# print key-value
print(d.items());


print();

# print keys
for key in d.keys():
    print(key);
print();

# print values
for val in d.values():
    print(val);
print();

# print keys
for key, val in d.items():
    print(key, val);
print();


# add items
d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
};
d["color"] = "red";
print(d);

# update
d.update({"color": "red"});
print(d);

# remove items
d.pop("model");
print(d);

print();

# loop on Dictionary
for x in d:
  print(x);

print();

for x in d:
  print(d[x]);