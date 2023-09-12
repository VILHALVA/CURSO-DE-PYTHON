from CLASSE import A

a1 = A()
a2 = A()

a1.VC = 321

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

print()

print(a1.VC)
print(a2.VC)

