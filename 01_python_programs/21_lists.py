# list creation
l1 = [1, 2, 3];    
print(l1, type(l1));

l2 = list([4, 5, 6]);
print(l2, type(l2));
print();

l = [];     # Empty List
# insert element
l.append(11);
l.append("Raj");
l.append(True);

print(l);
l.insert(1, 1001);
print(l);

# print size
print(len(l));
print();

# delete element
l = [1, 2, 3, 4, 5, 6, 7, 8];
print(l);

l.pop();
l.pop();
print(l);

# delete specific index element
l.pop(4);
print(l);

# # delete specific element
l.remove(2);
print(l);

# delete all element
l.clear();
print(l);
print();

# access list element
li = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"];
print(li[2:5]);
print(li[:4]);
print(li[-4:-1]);
print();

# Check if Item Exists
li = ["apple", "banana", "cherry"];
if "apple" in li:
  print("Yes, 'apple' is in the fruits list");


# Change Item Value
li = ["apple", "banana", "cherry"];
li[1] = "blackcurrant";
print(li);

# Change a Range of Item Values
li = ["apple", "banana", "cherry", "orange", "kiwi", "mango"];
li[1:3] = ["blackcurrant", "watermelon"];
print(li);
print();

# loops on lists
li = ["apple", "banana", "cherry"];
for x in li:
  print(x);
print();

# Loop Through the Index Numbers
for i in range(len(li)):
  print(li[i]);
print();

# Looping Using List Comprehension
li = ["apple", "banana", "cherry"]
[print(x) for x in li]
print();


# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x);
print(newlist);
print();


fruits = ["apple", "banana", "cherry", "kiwi", "mango"];
newlist = [x for x in fruits if "a" in x];
print(newlist);
print();



l1 = [1, 2, 3];
l2 = [4, 5];
l1.extend(l2);
print(l1, "\n");


print(list(range(10)));
print(list(range(1, 10)));
print(list(range(1, 20, 2)));


