# Write a program to check whether post is talking about Om or not.

post = input("Enter post: ")
if ("Om".lower() in post.lower()):
    print("Post is talking about Om")
else:
    print("Post is not talking about Om")