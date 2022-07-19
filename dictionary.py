jj = {"candy": 1, "snack": 2, "pen": 3}
print(jj)
hh = {}
print(hh)

kk = ["apple", "banana", "avocado", "mango"]
print(kk)

#difference between dictionary and list
jj["pen"] = 4
kk[0] = "pineapple"
print(jj)
print(kk)

#count things with dictionary
things = {"books": 1, "phone": 1, "pc": 1, "headphone": 1}
# things["books"] = things["books"] + 1
# print(things)

#set a histogram
counts = dict()
new_things = ["books", "headphone", "macbook", "notebook", "bag", "headphone", "headphone"]
# for thing in new_things:
#     if thing not in counts:
#         counts[thing] = 1
#     else:
#         counts[thing] += 1
# print(counts)   
#collapsing the loop(works the same as the loop above)
for thing in new_things:
    counts[thing] = counts.get(thing, 0) + 1
print(counts)   


#
for thing in counts:
    if thing in counts:
        x = counts[thing]
    else:
        x = 0
print(x)
#or
y = counts.get(thing, 0)
print(y)

#loop and dictionaries
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
#counting patterns
print("Enter a text:")
text = input('')
txt_words = text.split()
print("Words", txt_words)
count_words = dict()
for word in txt_words:
    count_words[word] = count_words.get(word, 0) + 1 #get(key, optional(value)) to view the value of a key in dictionaries. If that value doesn't exist in the dict, then when you input the key, value => that pairs of thing will be added to the dict
print("Counts", count_words)

#retrieving list of keys and values
print(list(jj))
print(jj.keys())
print(jj.values())
print(jj.items())

#wo iterations variables. loop through key-value pairs in a dictionary
for aa, bb in jj.items():
    print(aa, bb)

#i.e
d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)
