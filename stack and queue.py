print("Stack and queue")
class Stack:
	def __init__(self):
		self.items = []
	def push(self,items):
		self.items.append(items)
	def pop(self):
		return self.items.pop()
	def is_empty(self):
		if self.items == []:
			return True
		return False

s = Stack()
s.push(1)
s.push(2)
s.push(3)
while not s.is_empty():
	item = s.pop()
	print(item)
print("Balanced or not"")
def is_balnced(input_str):
	s = []

	for i in input_str:
		if i == '(':
			s.append(i)
		if i == ')':
			s.pop()
	return  not s


if __name__ == "__main__":
	input_str = input()

	if is_balnced(input_str):
		print(input_str,"balanced")
	else:
		print(input_str,"not balanced")
