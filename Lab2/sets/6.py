#Join sets

s1 = {"x", "y", "z"}
s2 = {1, 2, 3}

s3 = s1.union(s2)
print(s3)

s1 = {"x", "y", "z"}
s2 = {1, 2, 3}

s1.update(s2)
print(s1)