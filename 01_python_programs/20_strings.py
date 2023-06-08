a = "Hello";
print(a, type(a), "\n");

b = str("Hi");
print(b, type(b), "\n");

# multiline strings
a = """Hi,
how are you?,
where
are you 
from?"""
print(a, "\n");

b = '''Hi,
how are you?,
where
are you 
from?''';
print(b, "\n");

# check size of string
a = "Hello, World!";
print("Size = ", len(a), "\n");

# slicing
print(a[1]);
print(a[-1]);
print(a[2 :]);
print(a[: 5]);
print(a[0 : 3]);
print(a[-5 : -2]);
print(a[0 : 10 : 2]);
print();

# Looping Through a String
for x in "banana":
  print(x);

print();

# check string
txt = "The best things in life are free!";
print("free" in txt);
print("free" not in txt);

if "free" in txt:
  print("Yes, 'free' is present.");
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.\n");

# String Concatenation
a = "Hello";
b = "World";
c = a + " " + b;
print(c, "\n");

# Modify Strings
a = " Hello, World! "
print(a.upper());
print(a.lower());
print(a.strip());   # remove white spaces
print(a.replace("H", "J"));
print(a.split(","));
print();


s = "Bharat";
print(s * 3);
print(s.find("a"));
print();

x = 'a';
print(ord(x));
print(chr(97));
print(type(chr(97)));