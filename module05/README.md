
# Module: Loop

Do not repeat code, write a `loop`.

Python has two main loops: 

- `for` loop. This is really a `for each` loop from `C++`
- `while` loop. 

## For Loop
- Good for known number of iterations.
- Great choice for `Collections`: list, dictionaries, tuples, etc.

```python
# Template for for loop
for item in items:
    print(item) # access each element
```


## While Loops
One candidate if you have an unknown number of
iterations.

```python
while <COND>:
    # Update COND
    pass
```

NOTE: Make sure you do NOT create `infinite loops`. 
To avoid them, make sure you `update` the test condition
`EVERY` time.