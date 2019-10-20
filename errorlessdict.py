import operator
from inspect import signature

class ErrorlessDict:
    def __init__(self, default=None):
        self.default = default
        self.dict = {}

    def __getitem__(self, key):
        return self.dict[key] if key in self.dict.keys() else self.default
    
    def __setitem__(self, key, value):
        self.dict[key] = value

    # Create instance from existing dict
    @classmethod
    def from_dict(cls, dictionary, default=None):
        edict = cls(default=default)
        edict.dict = dictionary
        return edict

    # Create new instance with mapped values
    def map(self, f, default=None):
        mapped = ErrorlessDict(default=default)
        for k, v in self:
            mapped[k] = f(v)
        return mapped

    def __iter__(self):
        return iter(self.items())

    def keys(self):
        return self.dict.keys()
    
    def values(self):
        return self.dict.values()

    def items(self):
        return self.dict.items()

    # TODO: there has to be a better way
    def item(self, index):
        return list(self.items())[index]

    def key(self, index):
        return list(self.keys())[index]

    # Return internal dict sorted
    def sorted_dict(self, key=operator.itemgetter(1), reverse=False):
        return dict(sorted(self.dict.items(), key=key, reverse=reverse))

    # Set internal dict to sorted version
    def sort(self, key=operator.itemgetter(1), reverse=False):
        self.dict = self.sorted(key=key, reverse=reverse)

    # Return new instance from sorted internal dict
    def sorted(self, key=operator.itemgetter(1), reverse=False, default=None):
        return ErrorlessDict.from_dict(self.sorted_dict(key=key, reverse=reverse), default=default)

    def print_each(self, formatter, end='\n'):
        param_count = len(signature(formatter).parameters)
        if param_count == 3:
            for i, kv in enumerate(self):
                print(formatter(i, kv[0], kv[1]), end=end)
        elif param_count == 2:
            for k, v in self:
                print(formatter(k, v), end=end)
        else:
            raise ValueError('Expected function with 2 or 3 paramaters')