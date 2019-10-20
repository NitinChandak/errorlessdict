# ErrorlessDict
Pretty much just makes it so you can do
```py
dictionary = {}
dictionary['value'] += 2
```
without a getting a KeyError by instead doing
```py
dictionary = ErrorlessDict(0)
dictionary['value'] += 2
```
It uses the value provided in the constructor as a default value when a key doesn't already exist.
So now 'value' is equal to 2 and accessing anything else would return 0.
This is really only useful for like 2 scenarios but I was bored so here's this abomination.