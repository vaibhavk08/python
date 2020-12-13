def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("divisor cannot be 0.")
    

    return dividend / divisor

students = [
    {"name":"Bob", "grades": [75, 98]},
    {"name":"Rolf", "grades": [50]},
    {"name":"Jen", "grades": [100,93]}]

print("welocme to avg grades programe.")

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}")

except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!!")
else:
    print("--all student averages calculated--")
finally:
    print("Thank You")
