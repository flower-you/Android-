
with open("test.txt", "w") as f:
    f.write(str(1.5))

with open("test.txt", "r") as f:
    content=f.read()
    print(content)