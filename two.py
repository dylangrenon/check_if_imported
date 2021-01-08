import one

print("top level two.py")

# calls function 'func()' from one.py
one.func()

# tests if this script is being called directly by checking if
# the script's __name__ is the string '__main__'.  If it is, then
# the script is being ran directly and not imported.

if __name__ == '__main__':
    print("two.py being run directly")
else:
    print("two.py is being imported")
