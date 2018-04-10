from __future__ import print_function
import sys
import time
start_time = time.time()

class Brainfuck:
	def __init__(self, src):
		self.src = self.clean(list(src))
		self.stack = [0]*2
		self.ptr = 0
		self.code_ptr = 0		
		self.open_bracket_indexes = []
		self.close_bracket_indexes = []
		self.pair_brackets()
		
		
	def clean(self, code):
		return ''.join(filter(lambda x:x in ['+','-','.',',','[',']','>','<'], code))
		
	def pair_brackets(self):
		"""
		_open_bracket_indexes[i] is paired with _close_bracket_indexes[i].
		"""
		stack = []

		for index, command in enumerate(self.src):
			if command == '[':
				stack.append(index)

			elif command == ']':
				self.open_bracket_indexes.append(stack.pop())
				self.close_bracket_indexes.append(index)
	

	def evaluate(self):
		while self.code_ptr < len(self.src):
			command = self.src[self.code_ptr]
						
			
			if command == '+':
				self.stack[self.ptr] += 1 if self.stack[self.ptr] < 255 else 0
				
			elif command == '-':
				self.stack[self.ptr] -= 1 if self.stack[self.ptr] > 0 else 255

				
			elif command == '>':
				self.ptr += 1
				if self.ptr > len(self.stack)-1:
					self.stack.append(0)
					
			elif command == '<':
				self.ptr -= 1 if self.ptr > 0 else  0
				
			elif command == '.':
				print(chr(self.stack[self.ptr]),end = '')
				
			elif command == ',':
				self.stack[self.ptr] = ord(sys.stdin.read(1))
			   
			elif command == ']' and self.stack[self.ptr] != 0:
				index = self.close_bracket_indexes.index(self.code_ptr)
				self.code_ptr = self.open_bracket_indexes[index]
			
			elif command == '[' and self.stack[self.ptr] == 0:
				index = self.open_bracket_indexes.index(self.code_ptr)
				self.code_ptr = self.close_bracket_indexes[index]
			self.code_ptr += 1
			
			
def main():	
		src = open(sys.argv[1], 'r').read()
		bf = Brainfuck(src)
		bf.evaluate()




if __name__ == '__main__':
	main()
	print("--- %s seconds ---" % (time.time() - start_time))
