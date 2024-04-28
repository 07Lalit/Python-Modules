"""
                      USING STRING MODULE
                      -------------------

 # IMPORT STRING

 1) string.ascii_letters    # this all are not methods but variables
 2) string.ascii_lowercase
 3) string.ascii_uppercase
 4) string.punctuation
 5) string.hexdigits
 6) string.octdigits
 7) stirng.capwords(" Lalit")
 8) string.digits
 9) string.printable

"""
import string

print(f"printing (a-z-A-Z) string.ascii_letters: {string.ascii_letters}")
print(f"printing (a-z) string.ascii_lowercase: {string.ascii_lowercase}")
print(f"printing (A-Z) string.ascii_uppercase: {string.ascii_uppercase}")
print(f"printing (punctuation) string.punctation: {string.punctuation}")
print(f"printing  string.printable: {string.printable}")
print(f"printing  string.digits: {string.digits}")
print(f"printing  string.hexadigits: {string.hexdigits}")
print(f"printing  string.octdigits: {string.octdigits}")
print(f"printing  string.__all__: {string.__all__}")
print(f"printing (punctuation) string.capwords: {string.capwords("huu my name ies")}")