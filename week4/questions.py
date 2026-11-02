print("=== LIST (Mutable) ===")
my_list = [1, 2, 3]
print("Original list:", my_list)
print("ID before modification:", id(my_list))

my_list[0] = 99
my_list.append(4)

print("After modification:", my_list)
print("ID after modification: ", id(my_list))   

print("\n=== STRING (Immutable) ===")
my_string = "hello"
print("Original string:", my_string)
print("ID before:", id(my_string))

new_string = "H" + my_string[1:]
print("New string created:", new_string)
print("ID of new string:  ", id(new_string))   
print("Original string:   ", my_string)         
print("ID of original:    ", id(my_string))