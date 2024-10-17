# The maximum index for the list below is 4
my_list = [75, 88, 82, 91, 97]

try:
    # Attempt to access an out of range index
    index = 10
    print(my_list[index])
except IndexError:
    print(f"Error: Index {index} is out of range for the list.")


# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age < 0:
#             raise ValueError("Age cannot be negative.")
#         break
#     except ValueError as e:
#         print(f"Invalid input: {e}")

# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age < 0:
#             raise ValueError("Age cannot be negative.")
#         break
#     except ValueError as e:
#         print(f"Invalid input: {e}")
