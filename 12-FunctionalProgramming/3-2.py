sentence = 'I completely agree with you'
split = sentence.split(" ")
result = list(map(lambda split:len(split), sentence))
print(result)