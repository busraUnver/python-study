name = "busu"

#prints busubusu
print(name * 2)

#this isn't dynamic, if you later change the name and print greeting it'll still print busu
#to make it dynamic just do print(f"hello, {name}") so it'll calculate every time
greeting = f"hello, {name}"

print("-----------------------")

#prints hello, busu
print(greeting)

greeting2 = "hello, {}"
withName = greeting2.format(name)
print(withName)

longerPhrase = "hello, {}, today is {}"
print(longerPhrase.format("selim", "monday"))

#getting input
name = input("please write your name : ")
print(name)

print("-----------------------")

#always give string
number = input("give me a number : ")
intNumber = int(number)
toMeter = intNumber / 10.8
print(f"the meter is: {toMeter}")

print("-----------------------")

#format number
print(f"meter is {toMeter:.2f}")

print("-----------------------")

#booleans
friends = ["can", "banu"]
abroad = ["can", "banu"]
print(friends == abroad)

#this is false because the two lists have different areas in memory
#checks if the two is same thing
print(friends is abroad)
print(friends is friends)

print("-----------------------")

#if statements, make letters lowersace so cases match (case insensitive)
letter = input("give me a letter:").lower()

if letter == "a":
    print("that is an a")
elif letter == "b":
    print("that is a b")
else:
    print("not an a")