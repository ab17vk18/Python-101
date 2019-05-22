#EXPLANATION FOR if __name__ == "__main__":

def onefunc():
	print("Inside the onefunc of one.py")

print("Top level of one.py")

if __name__ == '__main__':
	print("one.py is executing directly")

else:
	print("one.py is imported and executing")