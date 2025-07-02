import hashlib

text = "hello"
result = hashlib.sha256(text.encode())
print(result.hexdigest())
