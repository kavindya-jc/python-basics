# === PRACTICE 1: VARIABLES & LISTS ===
print("=== PRACTICE 1 ===")

# 1. Create variables
name = "Alice"
age = 25
hobbies = ["reading", "coding", "gaming"]

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Hobbies: {hobbies}")

# 2. List operations
hobbies.append("cooking")
print(f"Updated hobbies: {hobbies}")

# 3. Access list elements
print(f"First hobby: {hobbies[0]}")
print(f"Last hobby: {hobbies[-1]}")



# === PRACTICE 2: DICTIONARIES ===
print("\n=== PRACTICE 2 ===")

# 1. Create dictionary
student = {
    "name": "Bob",
    "age": 22,
    "courses": ["Math", "Science"]
}

print(f"Student: {student}")
print(f"Student name: {student['name']}")

# 2. Add new key
student["grade"] = "A"
print(f"Updated student: {student}")



# === PRACTICE 3: LOOPS ===
print("\n=== PRACTICE 3 ===")

# 1. For loop with list
print("All hobbies:")
for hobby in hobbies:
    print(f"- {hobby}")

# 2. For loop with range
print("\nCounting 1-5:")
for i in range(1, 6):
    print(i)

# 3. While loop
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")



# === PRACTICE 4: FUNCTIONS ===
print("\n=== PRACTICE 4 ===")

# 1. Simple function
def square(number):
    return number * number

result = square(5)
print(f"Square of 5: {result}\n")

# 2. Function with multiple parameters
def introduce(name, age):
    return f"My name is {name} and I'm {age} years old."

intro = introduce("Charlie", 30)
print(intro)

# 3. Function with list
def count_items(items):
    return len(items)

hobby_count = count_items(hobbies)
print(f"\nI have {hobby_count} hobbies")



# === PRACTICE 5: CONDITIONALS ===
print("\n=== PRACTICE 5 ===")

def check_age(age):
    if age < 18:
        return "Minor"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

print(f"Age 15: {check_age(15)}")
print(f"Age 25: {check_age(25)}")
print(f"Age 70: {check_age(70)}")

