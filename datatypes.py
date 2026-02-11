
age = 18  #Integer
temperature = 34.89  #Float
greeting = "Hi!" #String
isMarried = True #Boolean

print("I am",age,"years old")
print("The current body temperature of the patient is",temperature, "degrees Celsius")
print(greeting, "Blessed")
print("Are you married? :",isMarried)


# Data Structures - Multiple values stored in a single variable
cars = ["Toyota", "Mercedes", "Audi", "Volvo", "BMW"] #List - Ordered and changeable
fruits = ("apple", "banana", "cherry", "mango") #Tuple -Ordered and unchangeable
countries = {"Italy", "Germany","France", "Spain"} #Set - Unchangeable
student = {
    "firstname" : "John",
    "age" : 19,
    "course" :"FullStack",
    "gender" : "Male"
}

print(cars)
print(fruits)
print(countries)
print(student)
print(student.get("firstname"))

#Typecasting - Converting from one data type to another
print(int(temperature))
