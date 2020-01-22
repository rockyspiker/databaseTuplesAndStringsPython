import re

with open('Strings.txt', 'r') as file:
    data = file.read()
    regex = re.compile('[^a-zA-Z]+', )
    data = regex.sub(' ', data)
    data = data.lower()
    wordList = data.split()

    wordAlignSpace = 0
    di = {}
    for word in wordList:
      di[word] = di.get(word, 0) + 1
      if len(word) > wordAlignSpace:
        wordAlignSpace = len(word)

    freqAlignSpace = 0  
    wordAndFreq = []
    for word, freq in di.items():
      wordAndFreq.append((freq, word))
      if len(str(freq)) > freqAlignSpace:
        freqAlignSpace = len(str(freq))
    
    wordAndFreq.sort(reverse=True)
    for freq, word in wordAndFreq:
      print(word.rjust(wordAlignSpace, ' ') + ':\t' + str(freq).rjust(freqAlignSpace, ' '))