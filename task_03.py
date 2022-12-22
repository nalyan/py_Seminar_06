#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Текст, содержащий абвгд'
print(' '.join(list(filter(lambda txt: 'абв' not in txt, text.split()))))

