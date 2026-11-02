# --- Mutable: list ---
my_list = [1, 2, 3]
print("Original list:", my_list)
print("id(my_list) before:", id(my_list))

my_list[0] = 99          # in-place modification
my_list.append(4)

print("After modification:", my_list)
print("id(my_list) after: ", id(my_list))   # same id → same object

print()

# --- Immutable: string ---
my_string = "hello"
print("Original string:", my_string)
print("id(my_string) before:", id(my_string))

# my_string[0] = 'H'   # TypeError: 'str' object does not support item assignment

# The only way to “change” it is to create a new string
new_string = "H" + my_string[1:]
print("new_string:", new_string)
print("id(new_string):", id(new_string))     # different id → new object
print("Original still:", my_string)           # unchanged
print("id(my_string) still:", id(my_string))  # same as before