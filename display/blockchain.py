import hashlib
import json
from time import time
import random


class Blockchain(object):
    def __init__(self):
        self.chain  = []
        self.pending_input = []
        #Genesis block
        self.new_block(previous_hash = "geese", proof=100)
    
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            #this is the info of each block that 
            'timestamp': time(),
            'info': self.pending_input,
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


def automation(name, address, email):

    blockchain.new_input(name, address, email)
    blockchain.new_block(random.randint(10000, 10000000))
    
    chain_list = blockchain.chain
        
    with open(r'./test.txt','w') as fout:
            #json.dump(object to be added goes here, filename goes here)
            # data = {
            #     "hashed_block" : chain_list
            # }
            # json.dump(str(chain_list), fout)
            fout.write(str(chain_list))
            fout.write('\n')
            fout.close()


    # with open('./chain.json','r') as read_file:
    #         mydata = json.load((read_file))
    # print(chain_list)
    

    
