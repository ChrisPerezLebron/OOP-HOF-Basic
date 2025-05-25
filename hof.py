from functools import reduce
def is_present(lst,x):
  raise Exception("Not Implemented")

def count_occ(lst,target):
  raise Exception("Not Implemented")

#GOAL FOR ALL: use higher order functions like map and reduce, accept functions as input, or return 
# functions as output


#Goal: remove any duplicates from the provided list 
def uniq(lst):
  #create a dictionary for the filter function to check against
  existsMap = {}

  def uniqueCheck(n):
    if existsMap.get(n, -111) == -111:
      #add this number to the exists map
      existsMap[n] = 1 
      #return true so filter passes
      return True
    #otherwise number is in the hashmap & no further processing is necessary 
    else: 
        return False 
    
  return list(filter(uniqueCheck, lst))


#Goal: find the max item in the matrix 
def find_max(matrix):
  reductionList = [] 

  #find max in each row using reduce HOF
  for list in matrix: 
    reductionList.append(reduce(max, list))

  #find max in new linear list 
  return reduce(max, reductionList)


#Goal: count the 1s in the matrix 
def count_ones(matrix): 
  #holds the first level reduction 
  reductionList = []

  #define helper function to count the number of ones
  def countOnes(old, new):
    if new == 1: 
      return old + 1
    else: 
        return old 

  #use reduce to find the number of ones per row 
  for list in matrix:
    reductionList.append(reduce(countOnes, list))

  #now sum the list     
  return reduce((lambda x,y: x + y), reductionList) 


#Goal: create partial function that adds the value of x to some input y 
  #addgenerator(10)(2) --> 12 
def addgenerator(x):
  f = lambda x: lambda y: x + y
  return f(x)


#Goal: create a and return function that accepts (val, func) and returns val + func(val)
  # apply_to_self()(2,lambda x: x + 1) --> 5
  # apply_to_self()(4,lambda x: -x) --> 0
def apply_to_self():
  return lambda x, f: x + f(x)


#Goal: given a matrix and a function, apply the function to every element 
  # map2([[1,2,3],[4,5,6]],lambda x: -x) --> [[-1, -2, -3], [-4, -5, -6]]
def map2(matrix,f):
  newMatrix = []
  for lis in matrix:
    newMatrix.append(list(map(f, lis)))
  return newMatrix