def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)


n = int(input("How many terms? "))

# check if the number of terms is valid
if n <= 0:
  print("Invalid number of terms")
else:
  # print the first n terms of the Fibonacci series
  print("The first", n, "terms of the Fibonacci series are:")
  for i in range(n):
    print(fibonacci(i))