import hashlib
import json
from time import time

class Blockchain():
	def __init__(self):
		self.chain = []
		self.pending_transactions = []
		
		self.add_new_block(previous_hash="Hello world!", proof = 100)
	
		def add_new_block(self, proof, previous_hash = None):
			block = {}
			
			return block