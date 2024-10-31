
# Module: Intro to Functions

We want to organize our code using function (modularize).

General form: 
```python
def function_name(arguments):
    return 
```

Basic information you need from your function:
- Name
- Does it take any parameters?
- Does it return something to me?

## First function
This function takes:
- No parameters
- Does not returns anything

```python
def function_name():
    pass
```

## Function that take input parameters

This function takes:
- One input parameter
- Does not returns anything

```python
def function_name(info):
    pass
```

## Function that take input parameters AND return values

This function takes:
- One input parameter
- Returns values to us. Uses the keyword `return`

```python
def function_name(number):
    number += 10
    return number
```