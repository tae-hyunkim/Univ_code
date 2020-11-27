a = 16 + 4 + 2 + 1
b = 4 + 1

print()
print( "a = ", bin(a))
print( "b = ", bin(b))

print()
print(" a & b = ", a & b, "Binary =", bin(a & b))
print(" a | b = ", a | b, "Binary =", bin(a | b))
print(" a ^ b = ", a ^ b, "Binary =", bin(a ^ b))
print(" ~ b = ", ~ b, "Binary =", bin(~b & 0xff))

print()
print("1<<3 :", 1<<3)
print("8>>3 :", 8>>3)

print()
print("11>>1 :", 11>>1)
print("11>>2 :", 11>>2)

x = 1024
print()
print(">> 11th bit of %d:"%x,1 & (x>>10))

x = 4
print()
print(">> 1st bit of %d :"%x,1 & (x>>0))
print(">> 2nd bit of %d :"%x,1 & (x>>1))
print(">> 3rd bit of %d :"%x,1 & (x>>2))

x = 100000
print("%d is %s in binary" %(x,bin(x)))
print("%d is %s in binary" %(x,oct(x)))
print("%d is %s in binary" %(x,hex(x)))
