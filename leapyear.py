def leap():
  year=input()
  if year%4==0 and year%100!=0 or year%400==0:
    print("yes")
  else:
    print("no")
if __name__=='__main__':
  leap()
