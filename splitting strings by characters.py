s = 'SHEMDEGI SADGURI DIDUBE'

s = s.upper()

words1, words2, words3 = s.split()



list1 = list(words1)
list2 = list(words2)
list3 = list(words3)



print('-'.join(list1), '-'.join(list2), '-'.join(list3))
