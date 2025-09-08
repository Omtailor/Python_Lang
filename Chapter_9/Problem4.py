# A file contains word donkey multiple times. Replace word Donkey with Yash

with open ("donkey.txt", "r") as f:
    content = f.read()
with open ("donkey.txt", "w") as f:
    if ("donkey" in content):
        new_content = content.replace("donkey", "Yash Yadav")
        
        f.write(new_content)
    