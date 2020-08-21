import hashlib
import json
from time import time
import random


class Blockchain(object):
    def __init__(self):
        self.chain  = []
        self.pending_input = []
        #Gensis block
        self.new_block(previous_hash = "geese", proof=100)
    
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            #this is the info of each block that 
            # 'timestamp': time(),
            # 'info': self.pending_input,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.pending_input = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):

        return self.chain[-1]
    
    def new_input(self, name, address, email,):     
        info2 = { #look here if there is an error with variable names.
            'name': name,
            'address': address,
            'email': email,
        }
        self.pending_input.append(info2)
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string).hexdigest()
        return raw_hash

blockchain = Blockchain()

# t1 = blockchain.new_input('jhon james', '6 gosling drive', 'kartick2@gmail.com')
# blockchain.new_block(4213123)
# t2 = blockchain.new_input('RJ Dharan', 'ra', 'rjdharan@gmail.com')
# blockchain.new_block(3242342345)
# t3 = blockchain.new_input('jhon james', '6 gosling drive', 'kartick2@gmail.com')
# blockchain.new_block(12334534534654)
# t4 = blockchain.new_input('gunit', 'ara', 'rjdharan@gmail.com')
# blockchain.new_block(4545664566)
# t5 = blockchain.new_input('jjon james', '6 goling drive', 'kartick2@gmal.com')
# blockchain.new_block(455675676)
# t6 = blockchain.new_input('RJ Dhran', '75a', 'rjdharn@gmail.com')
# blockchain.new_block(452342346)

# print("This is our first blockhain: ", blockchain.chain)


def automation():
    while True:
        name = input("Enter your name:").lower()
        address = input("Enter you address: ")
        email = input("Enter your email: ")
        blockchain.new_input(name, email, address)
        blockchain.new_block(random.randint(10000, 10000000))
        print("This is our first blockhain: ", blockchain.chain)

automation()