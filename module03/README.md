
# Module 3: First look at Collections

## Strings
Continue to explore `strings` and some of its properties. 

Strings is a sequence of characters or a collection of characters. 

Get `help` on strings using the following command: 

Open the `python` REPL
```
python
>>> help(str)
```

Properties: 
- Is an immutable sequence of `Unicode` code points

## List 
- Unlike strings, list are `mutable`.
- Use `[ ]` to define a list
- Use commas to separate values
- Order sequence of objects
- Have many methods to use with them
- Use `append()` method to add elements 

```python
# example
numbers = [33, 44, 55, 66]
```

List support the following built-in functions: 
- `len()`: get number the elements
- `sum()`: get the sum of elements (when applicable)
- `max()`: get the max value of elements (when applicable)
- `min()`: get the min value of elements (when applicable)

Open the `python` REPL
```
python
>>> help(list)
```

## Tuple
- `Immutable` sequence of arbitrary objects.
- Use the `tuple()` constructor
- Define them with `( )` 
- Access elements with `index` notation using `[ ]`

```python
# example of tuple
numbers = (33, 44, 55, 66)
# Access elements with [index]
numbers[2]  # will get '55'
```

## Sets
- An `unordered` collection of `unique` elements.
- Use the `set()` constructor
- Do operations as a whole. 
- Use `{ }` to define a set.
They are mostly use for operations at the group or collection level.

```python
# Example
unique_values = {44, 66, 77, 44}
# It will eliminate duplicates
print(unique_values) # prints: {44, 66, 77}
```

## Dictionary

- Has a collection of `key:value` unordered elements.
    - `key` values are usually `strings`, and they MUST be `unique`
- Use `{ }` to define the list of `key:value` objects.
- Use the `dict()` constructor.
- Access one element by `['key']` key values.

```python
# Define a dict()
teams = {'best':'Real Madrid', 'worst':'Barcelona'}
# Print one element
teams['best']  # will print/get 'Real Madrid'
```