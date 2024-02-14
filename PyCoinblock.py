import hashlib as hasher
import datetime as date


class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hasher.sha384() #48-bit encryption
    sha.update(str(self.index).encode('utf-8') + 
               str(self.timestamp).encode('utf-8') + 
               str(self.data).encode('utf-8') + 
               str(self.previous_hash).encode('utf-8'))
    return sha.hexdigest()
  
#Creating a gensis block to initiate the blockchain
def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

#Creating new blocks
def next_block(last_block):
  new_index = last_block.index + 1
  new_timestamp = date.datetime.now()
  new_data = "Hey! I'm block " + str(new_index)
  new_hash = last_block.hash
  return Block(new_index, new_timestamp, new_data, new_hash)

#Creating our blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# #Asking user for number of blocks
# number_of_blocks = int(input("How many blocks should be included in the blockchain:"))
# #number_of_blocks = 20


# for i in range(number_of_blocks):
#     block_to_add = next_block(previous_block)
#     blockchain.append(block_to_add)
#     previous_block = block_to_add
#     # Tell everyone about it!
#     print("Block {} has been added to the blockchain!".format(block_to_add.index))
#     print("Hash: {}".format(block_to_add.hash)) 
