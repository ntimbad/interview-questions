#Python interview migration:

## Reading materials: 

- Deque, counter, defaultDict: https://docs.python.org/3/library/collections.html
- Python general review: https://developers.google.com/edu/python
- Heap libs:  https://docs.python.org/3/library/heapq.html
- List comprehension : https://www.w3schools.com/python/python_lists_comprehension.asp
- https://www.geeksforgeeks.org/python-dictionary-comprehension/
- https://www.pythonforbeginners.com/basics/set-comprehension-in-python
- Regex : https://developers.google.com/edu/python/regular-expressions
- OOP : https://realpython.com/python3-object-oriented-programming/

### Convert tuple to list 
```
tuple(list)
tuple(i for i in list)
```

### Ascii value 

```
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))
```

### Loop over Dict
- https://developers.google.com/edu/python/dict-files


### Sorted dict 
```
 ## Common case -- loop over the keys in sorted order,
  ## accessing each key/value
  for key in sorted(dict.keys()):
    print(key, dict[key])
```

### NamedTuple 
```buildoutcfg
>>> # Basic example
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(11, y=22)     # instantiate with positional or keyword arguments
>>> p[0] + p[1]             # indexable like the plain tuple (11, 22)
33
>>> x, y = p                # unpack like a regular tuple
>>> x, y
(11, 22)
>>> p.x + p.y               # fields also accessible by name
33
>>> p                       # readable __repr__ with a name=value style
Point(x=11, y=22)
```
