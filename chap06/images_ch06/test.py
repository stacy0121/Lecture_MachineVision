users={'hsn':'man','jane':'woman','john':'man','lenna':'woman'}

for u,sex in users.copy().items():
    if sex == 'man':
        del users[u]

print(users)