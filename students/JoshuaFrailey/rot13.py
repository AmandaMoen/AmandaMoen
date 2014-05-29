<<<<<<< HEAD
import string


def _rot13_table():
    u"""Return rot13 encrpytion table for string.translate()"""
    alpha = string.ascii_lowercase
    alpha13 = alpha[13:] + alpha[:13]
    alpha += string.ascii_uppercase
    alpha13 = alpha13 + alpha[-13:] + alpha[-26:-13]
    return string.maketrans(alpha, alpha13)


def rot13(text, table=_rot13_table()):
    u"""Return ROT13 encrypted text"""
    return text.translate(table)

if __name__ == "__main__":

    # Generate translation table and convert common characters using rot13().
    table = _rot13_table()
    vals = []
    for i in (range(32, 127)):
        input_ = chr(i)  # Unsure why it won't work if input is unichr(i).
        trans = rot13(input_)
        trans_ord = ord(trans)
        vals.append((input_, i, trans, trans_ord))

    # Assert that alpha characters are translated by "rotating" the position
    # of the character by 13.  Assert that punctuation and whitespace are
    # not changed.  Print the translation of each character so that the user
    # can visually verify output.
    for val in vals:
        ord_diff = abs(val[1] - val[3])
        if val[0].isalpha():
            assert ord_diff == 13
        else:
            assert ord_diff == 0
        print u"{} is converted to {}".format(val[0], val[2])

    # Allow the user to translate a phrase of their choosing to further
    # demonstrate that the function meets the specification.
    user_text = raw_input(u"Enter text to translate: ")
    msg = u"The ROT13 translation of "
    msg += u"{} is: {}".format(user_text, rot13(user_text, table))
    print msg  # Is there a better way to format this for code readability?
||||||| merged common ancestors
=======
import string


def _rot13_table():
    u"""Return rot13 encrpytion table for string.translate()"""
    alpha = string.ascii_lowercase
    alpha13 = alpha[13:] + alpha[:13]
    alpha += string.ascii_uppercase
    alpha13 = alpha13 + alpha[-13:] + alpha[-26:-13]
    return string.maketrans(alpha, alpha13)


def rot13(text, table=_rot13_table()):
    u"""Return ROT13 encrypted text"""
    return text.translate(table)

# if __name__ == "__main__":

#     # Generate translation table and convert common characters using rot13().
#     table = _rot13_table()
#     vals = []
#     for i in (range(32, 127)):
#         input_ = chr(i)  # Unsure why it won't work if input is unichr(i).
#         trans = rot13(input_)
#         trans_ord = ord(trans)
#         vals.append((input_, i, trans, trans_ord))

#     # Assert that alpha characters are translated by "rotating" the position
#     # of the character by 13.  Assert that punctuation and whitespace are
#     # not changed.  Print the translation of each character so that the user
#     # can visually verify output.
#     for val in vals:
#         ord_diff = abs(val[1] - val[3])
#         if val[0].isalpha():
#             assert ord_diff == 13
#         else:
#             assert ord_diff == 0
#         print u"{} is converted to {}".format(val[0], val[2])

#     # Allow the user to translate a phrase of their choosing to further
#     # demonstrate that the function meets the specification.
#     user_text = raw_input(u"Enter text to translate: ")
#     msg = u"The ROT13 translation of "
#     msg += u"{} is: {}".format(user_text, rot13(user_text, table))
#     print msg  # Is there a better way to format this for code readability?
>>>>>>> upstream/master
