"""7. Write a program to find out whether a given post is talking about “Isha” or not."""
s="Isha"
post=input("Enter the post : ")

if s.lower() in post.lower():
    print("Post is talking about Isha")

else:
    print("Post is not talking about Isha")