import hashlib as hl
import json

def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    hashable_lock = block.__dict__.copy()
    hashable_lock['transactions'] = [tx.to_ordered_dict() for tx in hashable_lock['transactions']]
    return hash_string_256(json.dumps(hashable_lock, sort_keys=True).encode())
