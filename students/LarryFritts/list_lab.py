#!/usr/local/bin/python

#series one
#step 1
my_list = [u"Apples", u"Pears", u"Oranges", u"Peaches"]
print my_list, "\n"

#step 2
another_fruit = raw_input(u"What fruit would you like to add? ")
my_list.append(unicode(another_fruit))
print my_list, "\n"

#step 3
user_number = raw_input(u"Please enter a number between 1 - 5 ")
print user_number,  u"corresponds to ", my_list[int(user_number) - 1], "\n"

#step 4
my_list[0] = u"Nectarines"
print my_list, "\n"

#step 5
my_list.insert(0, u"Plum")
print my_list, "\n"

#step 6
for fruit in my_list:
    if fruit[0] == 'P':
        print fruit

#series two
#step 1
print "\n", my_list, "\n"

#step 2
my_list.pop()
print my_list, "\n"

#step 3
fruit_delete = raw_input(u"Which fruit should be deleted? ")
found = False
while not found:
    count = 0
    for fruit in my_list:
        if fruit == fruit_delete:
            del my_list[count]
            found = True
        else:
            count += 1
    if not found:
        print u"%s does not match a fruit in the list" % fruit_delete
        fruit_delete = raw_input(u"Which fruit should be deleted? ")
print my_list, "\n"

#series three
#step 1
copy_list = my_list[:]
for fruit in my_list:
    user_answer = raw_input(u"Do you like %s? " % fruit.lower())
    user_answer = user_answer.lower()
    while (user_answer != u"yes" and user_answer != u"no"):
        print "You answered: %s" % user_answer
        user_answer = raw_input(u"Please enter 'yes' or 'no' ")
        user_answer = user_answer.lower()
    if user_answer == u"no":
        copy_list.remove(fruit)
    my_list = copy_list[:]


print my_list, "\n"

#series four
for i in range(len(copy_list)):
    fruit_reverse = []
    fruit = copy_list.pop(i)
    fruit_reverse.extend(fruit)
    fruit_reverse.reverse()
    fruit = "".join(fruit_reverse)
    copy_list.insert(i, fruit)
my_list.pop()
print u"Original list: %s" % my_list
print u"Copied list: %s" % copy_list
