def largest():
  num1=input()
  num2=input()
  num3=input()
  if num1>num2 and num1>num3:
    print(num1)
  elif num2>num3:
    print(num2)
  else:
    print(num3)
if __name__=='__main__':
  largest()
