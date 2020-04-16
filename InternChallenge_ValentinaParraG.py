#### Intern Challenge - Valentina Parra Garcés

from collections import Counter # Dict subclass to count, makes algorithm faster

# Method to calculate N-grams, paremete words or sentence and size of n-gram
def calculateNGrams(wrd,n):

  ngram_array=[] # Variable to save result
  
  # O(n) complexity iterating over the necessary amount of times to acquire N-grams
  for i in range(len(wrd)-n+1):
    ngram=wrd[i:n+i] # Calculating the i N-gram moving forward with a window_size=n & step=1
    ngram_array.append(ngram) #Merge in array
  return ngram_array



# Method to calculate the most frequent N-gram, if it doesn't contain repeated returns the first N-gram
def mostFrequentNGram(wrd,n):
  
  ngram_array=[] # Variable to save result
  
  # O(n) complexity iterating over the necessary amount of times to acquire N-grams
  for i in range(len(wrd)-n+1):
    ngram=wrd[i:n+i] # Calculating the i N-gram moving forward with a window_size=n & step=1
    ngram_array.append(ngram) #Merge in array

  # Obtains the most common result in selected vector & extracts the first position from the dict result
  return Counter(ngram_array).most_common(1)[0][0] 

#Excecuting some examples
example1=calculateNGrams("Complexity",5)
example2=mostFrequentNGram("funny fun funniest",3)
print(example1)
print(example2)