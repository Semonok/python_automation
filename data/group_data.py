import os.path
import random
import string
import jsonpickle

from model.group import Group


def random_string(maxlen):
    symbols = string.digits + string.ascii_letters + string.punctuation + ' '
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ['', random_string(10)]
    for header in ['', random_string(10)]
    for footer in ['', random_string(10)]]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))
