import hashlib
import json
from time import time
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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
            #'info': self.pending_input,
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
    a = blockchain.new_block(random.randint(10000, 10000000))
    
    chain_list = blockchain.chain

    spreadsheetId = "1qTITycZDJZLm3VNvRUMXxaHLcjIu_frw5Aylny7AkOI"  # Please set the Spreadsheet ID.
    sheetName = "test1"  # Please set the sheet name.
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive'] 
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    header_to_key =  a


    spreadsheet = client.open(sheetName)
    worksheet = spreadsheet.worksheet(sheetName)

    sheet = client.open(sheetName)
    ws = sheet.worksheet('myWorksheet')
    ws.update_acell('A1', str(chain_list))

    
