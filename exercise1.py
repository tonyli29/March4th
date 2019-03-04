digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']



translated = {}
for num in range(0, len(digits)):
    current = digits[num]
    translated[current] = {'french': fr[num], 'English': en[num]}

print(translated)
