# this is a testing file for copilot
# write a function that scans an array for an integer and returns the index of the integer
def find_integer_index(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1  # return -1 if the target integer is not found in the array

# test the function
arr = [1, 2, 3, 4, 5]
target = 2
print(find_integer_index(arr, target))  # should print 2

# write a function that takes a string and returns the reverse of the string
def reverse_string(s):
  return s[::-1]

def rev_string2(s):
  return ''.join(reversed(s))

s = "Hello World"

print(reverse_string(s))  # should print "dlroW olleH"
print(rev_string2(s))  # should print "dlroW olleH"

def array_sum(arr):
  return sum(arr)

arr = [1, 3, 5, 7, 9]
print(array_sum(arr))  # should print 25