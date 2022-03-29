import random
import string
from interact_with_db import create_keys_table

if __name__ == '__main__':
    keys = set()
    while len(keys) < 180:
        key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        keys.add(key)
    create_keys_table(keys)
