# Assignment: MUTABILITY, REFERENCES, AND MEMORY MODEL IN PYTHON
**Student Name:** Liza Usman  
**Date:** October 26, 2026

---

## 1. Assignment Title
MUTABILITY, REFERENCES, AND MEMORY MODEL IN PYTHON

---

## 2. Theoretical Explanations

### Difference between Mutable and Immutable Objects

**Mutable objects** can be changed after they are created. You can modify their content in-place without creating a new object.  
Examples: list, dict, set

**Immutable objects** cannot be changed after they are created. Any operation that looks like a modification actually creates a *new* object.  
Examples: str, tuple, int, float, bool

---

## 3. Python Program Demonstration

```python
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
print("ID of new string:  ", id(new_string))  
print("Original string:   ", my_string)        
print("ID of original:    ", id(my_string))