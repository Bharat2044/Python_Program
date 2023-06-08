s = {"apple", "banana", "cherry"}
print(s, type(s));
print();

s = {"apple", "banana", "cherry", "apple"};
print(s);

s = {"apple", "banana", "cherry", True, 1, 2};
print(s);
print("Size = ", len(s), "\n");

# set() Constructor
s = set(("apple", "banana", "cherry")) # note the double round-brackets
print(s)


# access set item
s = {"apple", "banana", "cherry"};
for x in s:
  print(x);
print("banana" in s);
print();

# add items
s.add("orange");
print(s);

# remove items
s.remove("banana");
print(s);

print();

# loops on sets
for x in s:
  print(x);