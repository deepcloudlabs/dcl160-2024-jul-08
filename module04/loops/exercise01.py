names = ["jack", "kate", None, "ben", None, "james", None, "sun", "jin"]
# name -> loop variable
for name in names[::-1]:
    if name is not None:
        print(name)
