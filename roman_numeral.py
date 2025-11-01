'''input: roman numeral'''
'''output: arabic numeral'''

input = str(input("Enter roman numeral: "))


priority = ['I','V','X','L','C','D','M']
meaning = [1,5,10,50,100,500,1000]
output = 0
conventional = []

print(f'Roman numeral in input : {input}')

for i in input:
    conventional.append(meaning[priority.index(i)])

while len(conventional):
    if len(conventional) == 1:
        output += conventional[0]
        break
    elif conventional[0] >= conventional[1]:
        output += conventional[0]
        conventional = conventional[1:]
    else:
        output = output + conventional[1] - conventional[0]
        conventional = conventional[2:]

print(f'Output in Arabic numerals : {output}')