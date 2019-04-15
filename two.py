#TWO.PY

import one

print("At the top level of two.py")

one.onefunc()

if __name__ == '__main__':
	print("two.py is executing directly")

else:
	print("two.py is imported and executing")