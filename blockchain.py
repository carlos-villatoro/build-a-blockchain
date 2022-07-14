import hashlib
import json
from time import time
from pprint import pprint

class Blockchain:
    def __init__(self):
        # list of blocks in the cxhain
        self.chain = []
        # list of trans that have not been added yet
        self.pending_trans = []
        # seed the blockchain with a new block
        self.new_block(previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.", proof=100)
    
    def __len__(self):
        return len(self.chain)

    @property # another decorator
    def last_block(self):
        # return the last block of the chain
        return self.chain[-1] # last index of the chain

    def new_block(self, proof, previous_hash):
        # create a new block based on the pending trans
        # create a new block
        block = {
            'index': len(self) + 1,
            'timestamp': time(),
            'transactions': self.pending_trans,
            'proof': proof, # provided by the miner
            'previous_hash': previous_hash or self.hash(self.last_block)
        }
        # clear out the pending trans
        self.pending_trans = []
        # append the new block to the chain
        self.chain.append(block)

    def new_trans(self, sender, recipient, amount):
        # add a new trans to the list of pending trans
        # create new transaction
        trans = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        # add trans to list of pending trans
        self.pending_trans.append(trans)
        # returns trans that got added
        return trans

    def hash(self, block):
        # hash bloacks
        # order the keys of the block so that they are predictable, encode
        string_block = json.dumps(block, sort_keys=True)
        # return hexdigest
        return hashlib.sha256(string_block).hexdigest()


bc = Blockchain()
print(bc.chain)
bc.new_trans('taylor', 'me', 50)
bc.new_trans('joe', 'taylor', 100)
bc.new_trans('taylor', 'me', 50)
pprint(bc.pending_trans)
pprint(bc.chain)
