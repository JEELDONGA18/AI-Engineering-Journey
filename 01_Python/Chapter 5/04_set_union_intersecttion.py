s1={1,3,44,645,534,434,43}
s2={1323,534,6534,4323,434}
print(s1.union(s2))
print(s1.intersection(s2))

print({1,3}.issubset(s1))
print(s1.issuperset({1,3,55}))