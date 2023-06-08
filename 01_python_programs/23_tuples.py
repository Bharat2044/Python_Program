t = ("apple", "banana", "cherry");
print(t);
print(type(t));

print("Size = ", len(t));
print();

t = tuple(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")) # note the double round-brackets
print(t);
print(t[1]);
print(t[-1]);
print(t[2:5]);
print();


# loops on tuple
t = ("apple", "banana", "cherry");
for x in t:
  print(x);