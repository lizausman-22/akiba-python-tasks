# Week 4 python tasks: MUTABILITY, REFERENCES, AND MEMORY MODEL IN PYTHON
**Student Name:** Liza Usman  
**Date:** October 26, 2026 
---

## Question 1: Difference between Mutable and Immutable Objects

### Explanation
**Mutable objects** can be changed after they are created. You can modify their content in-place without creating a new object.  
Examples: list, dict, set

**Immutable objects** cannot be changed after they are created. Any operation that looks like a modification actually creates a *new* object.  
Examples: str, tuple, int, float, bool

### Code 

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
```

## Question 2: References and Object Identity

### Explanation 
a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)
print(a == c)

The output: 
True
False
True

**Difference between is and ==:** is checks if two variables point to the same object in memory
== checks if two variables have the same value.

Why a and c have same values but different identities:

a and c both contain [10, 20, 30], so a == c is True
But they are two different lists created separately, so a is c is False
b = a means b is just another name for the same list, so a is b is True
