a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(a is b)


a = [1, 2, 3]
b = a[:]
b.append(4)
print(a)
print(a is b)

names = ['Amelia','Renee','Aurora']
scores = [95,96,94]

eng2sp = {'one':'uno', 'two':'dos','three':'tres'}

for word in eng2sp:
    print

for eng in eng2sp:
    sp = eng2sp[eng]
    if sp == 'dos':
        print(eng)

# Start empty, add entries
prices = {}
prices['AAPL'] = 178.50
prices['GOOG'] = 141.80
prices['MSFT'] = 415.20

# Update an existing key
prices['AAPL'] = 182.30

# Delete a key
del prices['GOOG']

print(prices)   # {'AAPL': 182.30, 'MSFT': 415.20}
