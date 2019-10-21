from errorlessdict import ErrorlessDict

# Features are arrays in format: [Appearance, Intelligence, Personality]
feature_weights = [1, 2, 3]

#this is just a joke
waifus = {
    'Aqua': [10, 0, 5],
    'Emilia': [7, 6, 7],
    'Fumino Furuhashi': [10, 10, 10],
    'Makise Kurisu': [10, 10, 9.9],
    'Miku Nakano': [10, 4, 8],
    'Raphiel Ainsworth Shiraha': [10, 9, 9],
    'Satanichia Kurumizawa McDowell': [8, 5, 9]
}

# Example 1 - Without ErrorlessDict
waifu_scores = {}
for waifu, features in waifus.items():
    for i in range(len(feature_weights)):
        if waifu in waifu_scores.keys():
            waifu_scores[waifu] += features[i] * feature_weights[i]
        else:
            waifu_scores[waifu] = features[i] * feature_weights[i]

# Example 2 - ErrorlessDict for storing total scores
waifu_scores = ErrorlessDict(0)
for waifu, features in waifus.items():
    for i in range(len(feature_weights)):
        # Doesn't throw KeyError on first assignment, instead uses default value first
        waifu_scores[waifu] += features[i] * feature_weights[i]

# Example 3 - ErrorlessDict for both data and total score, uses helper methods for needless one liner
# Plus bonus points because this one is sorted
waifus = ErrorlessDict.from_dict(waifus)
waifu_scores = waifus.map(
    lambda v: sum([v[i] * feature_weights[i] for i in range(len(feature_weights))]),
    default=0
).sorted(reverse=True)

# Because printing each item in a dict is a pretty common pattern, here's a helper
# that takes a formatter function (index param is optional).
waifu_scores.print_each(lambda i, k, v: f'{i + 1}. {k} - {v}')
