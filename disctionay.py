# Dictionary examples

# 1. Basic dictionary creation and access
ebook_1 = {
    'title': 'Passive Income',
    'author': 'Maximus Minimus',
    'price': 0.99,
}

print("Title:", ebook_1['title'])
print("Author:", ebook_1['author'])
print("Price:", ebook_1.get('price'))
print("ISBN (missing):", ebook_1.get('isbn', 'unknown'))

# 2. Build an empty dictionary and add items
terms = {}
terms['variable'] = 'a value stored in memory'
terms['integer'] = 'a whole number'
terms['float'] = 'a floating point decimal number'
print('\nTerms dictionary:', terms)

# 3. Update values and merge dictionaries
terms.update({'boolean': 'True or False', 'string': 'a sequence of characters'})
print('\nUpdated terms:', terms)

# 4. Safe lookup with get() and setdefault()
print('\nLookup integer:', terms.get('integer'))
print('Lookup missing key:', terms.get('tuple', 'not found'))
terms.setdefault('tuple', 'an ordered, immutable collection')
print('Added tuple with setdefault:', terms['tuple'])

# 5. Looping through dictionary keys, values, and items
print('\nKeys:')
for key in terms.keys():
    print('-', key)

print('\nValues:')
for value in terms.values():
    print('-', value)

print('\nItems:')
for key, value in terms.items():
    print('-', key, ':', value)

# 6. Nested dictionary example
library = {
    'ebook_1': {
        'title': 'Passive Income',
        'author': 'Maximus Minimus',
        'price': 0.99,
    },
    'ebook_2': {
        'title': 'Python Basics',
        'author': 'Ada Code',
        'price': 5.99,
    },
}

print('\nLibrary ebook titles:')
for ebook_key, ebook_info in library.items():
    print('-', ebook_key, '->', ebook_info['title'])

# 7. Removing items from a dictionary
removed = terms.pop('float', None)
print('\nRemoved float value:', removed)
print('Terms after pop:', terms)

if 'boolean' in terms:
    del terms['boolean']
    print('Removed boolean with del')

print('\nFinal terms dictionary:', terms) 