# if-elif-else
age = 25

print("\nBasic if-elif-else:")
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")




# match case
# same as swtich case in c/c++ or java
print("\nUsing match case:")
match age:
    case _ if age < 18:
        print("You are a minor.")
    case _ if 18 <= age < 65:
        print("You are an adult.")
    case _:
        print("You are a senior citizen.")


def day_type(day):
    match day.lower():
        case "monday", "tuesday", "wednesday", "thursday", "friday":
            return "Weekday"
        case "saturday", "sunday":
            return "Weekend"
        case _:
            return "Invalid day"

print("\nDay type:", day_type("tuesday"))
# here its not right!!!

# student's marks
def first_and_last(seq):
    match seq:
        case [first, *middle, last]:
            return first, last, middle

print("\nFirst, last, and middle:", first_and_last([1, 2, 3, 4, 5]))