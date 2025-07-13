def divide(a, b):
  try:
      result = a / b
      return result
  except ZeroDivisionError:
      print ('ZeroDivisionError')
      b=int(input('B can not be 0 please enter another number: '))
      divide(a,b)
  except ValueErro:
      print('ValueError')
      if a.type==int:
        b=int(input('please enter a number: '))
        divide(a,b)
      else:
        a=int(input('please enter a number: '))
        divide(a,b)
  else:
      print('please change the inputs!')
      a=int(input('a: ')
      b=int(input('b: ')
      divide(a,b)
  finally:
      print('succesful!!!!')

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Result:", divide(num1, num2))
