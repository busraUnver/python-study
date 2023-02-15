name = "busu"

#prints busubusu
print(name * 2)

#this isn't dynamic, if you later change the name and print greeting it'll still print busu
#to make it dynamic just do print(f"hello, {name}") so it'll calculate every time
greeting = f"hello, {name}"

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

#always give string
number = input("give me a number : ")
intNumber = int(number)
toMeter = intNumber / 10.8
print(toMeter)

#format number
print(f"meter is {toMeter:.2f}")