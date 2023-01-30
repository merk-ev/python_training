from training.model.contact import Contact
import random
import string
import jsonpickle
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['number og groups', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = 'data/contact.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits *10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits(maxlen):
    digits = string.digits
    return ''.join([random.choice(digits) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string('firstname-', 10),  middlename=random_string('middlename-', 10),
            lastname=random_string('lastname-', 10), nickname=random_string('nickname-', 10),
            title=random_string('title-', 10), company=random_string('company-', 10),
            address=random_string('address-', 10), home=random_digits(10), mobile=random_digits(10),
            work=random_digits(10), fax=random_digits(10), email=random_string('email-', 10),
            email2=random_string('email2-', 10), email3=random_string('email3-', 10),
            homepage=random_string('homepage-', 10), bday=random_digits(2), bmonth=random_digits(2),
            byear=random_digits(4), aday=random_digits(2), amonth=random_digits(2),
            ayear=random_digits(4), address2=random_string('address2-', 10),
            phone2=random_digits(10), notes=random_string('notes-', 30))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))
