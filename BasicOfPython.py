import random

x, y, z = "Mango", "Oranges", "Grapes"
print(x)
print(y)
print(z)

fruits = {"Hello1", "Hello2", "Hello3"}
x, y, z = fruits
print(x)
print(y)
print(z)
x = "Hello 4"
y = "Hello 5"
z = "Hello 6"
print(x, y, z)

x = "Hello Ohm , It is Global Variable"


def myfunc():
    global x

    x = "Hello Ohmjee"


print("Global Variable is set as : " + x)

myfunc()

print("Global Variable is set as : " + x)

x = 20
print(type(x))

x = int(20)
print(type(x))

x = 2
y = 3e5
z = 4j

print(x)
print(type(y))
print(type(z))

x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
d = complex(x)
print(a)
print(b)
print(d)

print((type(d)))

#Random Number Generation Examples
x = random.randrange(1, 11)
print(x)

x = 21
y = 21

a = str(x)
b = float(y)
print(a)
print(b)

#MultiLine String example
x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(x)

y = 'Hello Ohm , Welcome to Python World'
print(y)
print(y[0])

for x in "banana":
    print(x)
z = "HelloOhm"
print(len(z))

#Check the string
v = "Hello Ohm , Welcome to New Delhi and Python World !"
print("World" in v)

print("Patna" not in v)

#Slicing String
x = "Hello World! "
print(x[2:5])
#Slice from the start
print(x[2:])
#Slice from the end
print(x[:5])

#Negative Indexing
print(x[-5:-2])

#UpperCase,lowerCase & Remove Whitespaces
print(x.lower())
print(x.upper())
print(x.strip())
