def wordcount(words):
  count=0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      count += 1
  return count

print(wordcount(['abc', 'xyz', 'aba', '1221','xx']))
