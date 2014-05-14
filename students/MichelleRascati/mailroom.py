#!/usr/bin/env python
from safe_input import safe_input


def thanks(ty_name):
    """Prompt for donation amount and return amount."""
    amt = u'' + safe_input("What is %s's donation amount? " % ty_name)
    if amt == u'quit':
        return None
    else:
        while True:
            try:
                amt = float(amt)
            except ValueError:
                amt = u'' + safe_input("%s is not a number, please enter \
donation amount [or 'quit']: " % amt)
                if amt == u'quit':
                    return None
            else:
                break
        print "Dear %s, \n \
    Thank you for your donation of $%.2f to our charity.  We appreciate \
your support. \n \
    Sincerely,\n Michelle Rascati" % (ty_name, amt)
        return amt


def create(c_list):
    """Print a report of donations."""
    don_rep = []
    for donor in donations.keys():
        total = sum(donations[donor])
        count = len(donations[donor])
        don_rep.append([donor, total, count, total / count])
    don_rep.sort(key=second, reverse=True)
    # Find longest name to use for formatting
    n_long = max([len(col[0]) for col in don_rep])
    print "%*s %8s %8s %8s" % (-n_long, "Name", "Total",
                               "Count", "Average")
    for donor in don_rep:
        print "%*s %8i %8i %8d" % \
            (-n_long, donor[0], donor[1], donor[2], donor[3])


def second(l_list):
    """Return second variable in list."""
    return l_list[1]


if __name__ == '__main__':
    donations = {u'Larry': [10.00, 150.50, 75.00],
                 u'Sue': [40.00, 35.00],
                 u'Julie': [35.50],
                 u'Bob': [60.25, 100.00],
                 u'Karen': [83.50, 72.45, 90.25]}
    while True:
        do = u''
        while do.lower() not in (u'ty', u'cr', u'quit'):
            do = u'' + safe_input("Send a Thank You [ty] or Create a Report \
[cr] or [quit]? ")

        if do.lower() == u'ty':
            # Prompt for full name
            name = ''
            while name not in donations.keys():
                name = u'' + safe_input("Type full name for Thank You letter\
or [list] for existing donors. (or [quit]): ")
                if name.lower() == u'list':
                    for donor in donations.keys():
                        print donor
                elif name == u'quit':
                    break
                elif name not in donations.keys():
                    donations[name] = []
            if not name == u'quit':
                amount = thanks(name)
                if not amount is None:
                    donations[name].append(amount)
                else:
                    # Remove name if quit thanks()
                    del donations[name]
        elif do.lower() == u'cr':
            create(donations)
        elif do.lower() == u'quit':
            break
