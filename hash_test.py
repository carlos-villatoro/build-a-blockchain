# pythons built in hash lib
import hashlib

# encode a string -- encode to utf-8
encode = 'A'.encode() # no args = utf-8
# str(18).encode()

# digest into a hash
digest = hashlib.sha256(encode).hexdigest()
print(digest)

print(digest == hashlib.sha256('A'.encode()).hexdigest())