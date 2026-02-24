fruit = 'banana'
fruit[0]     # 'b'
fruit[1]     # 'a'
fruit[-1]    # 'a' (last character)
len(fruit)   # 6
fruit[6]     # IndexError! (valid indices: 0 to 5)

fruit = 'banana'
fruit[0:3]   # 'ban'  (includes start, excludes end)
fruit[3:6]   # 'ana'
fruit[:3]    # 'ban'  (omit start = from beginning)
fruit[3:]    # 'ana'  (omit end = to end)
fruit[:]     # 'banana' (copy the whole string)


