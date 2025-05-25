#Goal: check if integer n is a palindrome
  #n is a nonnegative integer
  #n will not contain leading zeros
def isPalindrome(n):
  #convert to string
  nStr = str(n)

  #compare first and last (moving pointers inward)
  for i in range(0, int(len(nStr)/2)): 
    if nStr[i] != nStr[(len(nStr) -1) - i]:
      return False
    
  return True 


#Goal: get nTH largest item in array
def nthmax(n, a):
  if(n > len(a) - 1): 
    return None
  
  a.sort() 
  a.reverse()

  return a[n]


#Goal: find most frequent character in s
  #capitilization matters A != a 
def freq(s):
  if len(s) == 0: 
    return ""
  
  freq = {}
  #get frequencies
  for i in range(0, len(s)): 
    #if character has not been encountered yet
    if freq.get(s[i], 0) == 0: 
      freq[s[i]] = 1
    else:
      freq[s[i]] = freq.get(s[i]) + 1

  max = ("", 0)
  #find heighest frequency
  for k, v in freq.items():
    if v > max[1]:
      max = (k, v)
    
  return max[0] 

#Goal: create a dictionary such that corrsponding items in the lists are key value pairs
  #EX: zipHash([1, 5], [2, 4]) --> {1: 2, 5: 4}
def zipHash(arr1, arr2):

  if len(arr1) != len(arr2): 
    return None
  
  map = {}

  for i in range(0, len(arr1)):
      map[arr1[i]] = arr2[i]

  return map

#Goal: convert dictionary to list of key value pairs
  #hash is supposed to be a dictionary 
def hashToArray(hash):
  result = [] 
  for key in hash.keys(): 
    result.append([key, hash.get(key)])
  return result

#Goal: given an initial operand and a list of single argument lambda functions, return the maximum value that can be obtained 
# by running all the lambda functions once but in any order. 
def maxLambdaChain(init, lambdas):
  
  #returns all the possible combinations for a list
  def combinations(combos): 
    #base case list has one element
    if len(combos) == 1: 

      #create new list
      result = []

      #append a set consisting of this last item
      result.append(set([combos[0]]))
      
      return result
    
    #recurse so we can do operation on the way up 
    combosFromSmallerSet = combinations(combos[1:])

    #new list is equal to old list
    newCombos = combosFromSmallerSet.copy()
    #add set corresponding to just this current item
    newCombos.append(set([combos[0]]))

    #now for each set in the smaller combo set, add current element
    for combo in combosFromSmallerSet:
      #create a copy so we can modify during iteration
      comboCopy = set(combo)
      #add this item to previous combo 
      comboCopy.add(combos[0]) 
      #add this new combo to the list of combos
      newCombos.append(comboCopy)

    #return all combos
    return newCombos
  
  indicies = [] 

  #construct a list consisting of 0 to n 
  for i in range(0, len(lambdas)):
    indicies.append(i)
  
  #use helper function to get a list of sets where each set represents
  # one possible combination 
  combos = combinations(indicies)

  #start currMax at init
  currMax = init

  #now run all every set in the list which corresponds to one choice possibility 
  # and determine which gives the maximum value
  for possibility in combos: 
    currSum = init
    for index in possibility: 
      currSum = lambdas[index](currSum)

    #make currMax the maximum of this "combination's" final value and last max 
    currMax = max(currSum, currMax)
  
  return currMax
