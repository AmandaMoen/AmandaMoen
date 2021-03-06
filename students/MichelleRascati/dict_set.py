<<<<<<< HEAD
### 1 ###
# Create Dictionary
d = dict(name='Chris', city='Seattle', cake='Chocolate')
# Display Dictionary
print d
 # Delete entry for 'cake'
del d['cake']
# Display Dictionary
print d
# Add entry for 'fruit' with 'Mango' and Display Dictionary
d['fruit'] = 'Mango'
print 'Dictionary Keys:'
for k in d.keys():
    print k
print 'Dictionary Values:'
for v in d.values():
    print v

print 'cake in dictionary?', 'cake' in d.keys()
print 'Mango in dictionary?', 'Mango' in d.values()

### 2 ###
# Create list of 0-15
z_15 = range(16)
# Create list of 0-15 in hexidecimal
hex_z_15 = []
for num in z_15:
    hex_z_15.append(hex(num))
# Zip two lists to make a dictionary
d_hex = dict(zip(z_15, hex_z_15))

print '0-15 and hex values:', d_hex

### 3 ###
# Make a dictionary with keys in d number of 'a's as vals
d_a = {}
for k in d.keys():
    d_a[k] = d[k].count('a')

print "Number of a's in original dict", d_a

### 4 ###
# Create a set of containing 0-20 divisible by 2, 3, and 4 respectively
s2 = set()
s3 = set()
s4 = set()
for n in range(21):
    if n % 2 == 0:
        s2.add(n)
    if n % 3 == 0:
        s3.add(n)
    if n % 4 == 0:
        s4.add(n)
print s2
print s3
print s4
# Display if s3 is subset of s2
print s3.issubset(s2)
# Display if s4 is subset of s2
print s4.issubset(s2)

### 5 ###
sP = {'P', 'y', 't', 'h', 'o', 'n'}
sP.add('i')
frozen = frozenset({'m', 'a', 'r', 'a', 't', 'h', 'o', 'n'})
print "Union:", sP.union(frozen)
print "Intersection:", sP.intersection(frozen)
||||||| merged common ancestors
=======
### 1 ###
# Create Dictionary
food_prefs = dict(name=u'Chris', city=u'Seattle', cake=u'Chocolate',
                  fruit=u'mango', salad=u'greek', pasta=u'lasagna')
# Display Dictionary
print '1) {name} is from {city}, and he likes {cake} cake, {fruit} fruit, \
{salad} salad, and {pasta} pasta.'.format(**food_prefs)


### 2 ###
# Create list of 0-15
z_15 = range(16)
# Create list of 0-15 in hexidecimal
hex_z_15 = [hex(num) for num in z_15]
# Zip two lists to make a dictionary
d_hex = dict(zip(z_15, hex_z_15))

print '2) 0-15 and hex values:', d_hex

### 3 ###
# Create dict of hex values with dict comprehension
hex_dict = {i: hex(i) for i in range(16)}

print '3) 0-15 and hex values:', hex_dict

### 4 ###
# Make a dictionary with keys in d number of 'a's as vals
food_prefs_a = {k: food_prefs[k].count('a') for k in food_prefs.keys()}

print "4) Number of a's in original dict", food_prefs_a

### 5 ###
# Create a set of containing 0-20 divisible by 2, 3, and 4 respectively
(s2, s3, s4) = ({n for n in range(21) if not n % x} for x in range(2, 5))

print '5)'
print 's2:', s2
print 's3:', s3
print 's4:', s4
>>>>>>> upstream/master
