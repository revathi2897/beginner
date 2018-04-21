def alpha():
  alpha=raw_input()
  if ord(alpha)>=65 and ord(alpha)<=90 or ord(alpha)>=97 and ord(alpha)<=122:
    print("ALPHABET")
  else:
    print("NO")
if __name__=='__main__':
  alpha()
