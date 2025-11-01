import math
#input: an integer in base 10, the desired base
#output: the same integer but in the desired base

def base_converter(input,base_in,base_out):

    #handling errors
    '''
    if input<base_out:
        raise ValueError("Base cannot be larger than input")
    elif type(input) is not int or input<1:
        raise ValueError("Input must be a possitive integer")
    elif type(base_out) is not int or base_out<2:
        raise ValueError("Base must be a positive integer") 
    '''


    
    input = list(str(input))
    input_10 = 0
    length_input = len(input)

    #turning input number into base 10
    dictionary_in = {
     'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
     'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
     'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
     'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
     'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34,
     'Z': 35
    }

    #turning input number into base 10

    for i in range(len(input)):
        if input[i].isdigit() == False:
            input_10 += int((int(dictionary_in[input[i]])*(base_in**(length_input-1-i))))
        else:
            input_10 += int((int(input[i])*(base_in**(length_input-1-i))))



    #for handling bases above 10
    dictionary = {
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
    15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J',
    20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O',
    25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T',
    30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y',
    35: 'Z'
    }


    input = input_10
    #code
    out = []
    explanation = []
    largest = math.floor(math.log(input,base_out))
    while largest >= 0:
        if input >= base_out**largest:
            appending = input//(base_out**largest)
            input = input - ((base_out**largest)*appending)
            explanation.append(f'{appending} x {base_out**largest}')
            if appending>9:
                appending = dictionary[appending]#handles case where multiple larger than 9
            out.append(appending)
        else:
            out.append(0)
            explanation.append(f'{0} x {base_out**largest}')
        largest -= 1
        output = "".join(str(x) for x in out)
        inputs = " + ".join(str(x) for x in explanation)
    return output, inputs


'''Enter values here'''
input_number = "THORSTENROLFERIKCHRISTIANSSON"
base_out = 2
base_in = 36

print('')
print(f'The given number ({input_number} ,in base {base_in}) can be written as {base_converter(input_number,base_in,base_out)[0]} in base {base_out}.')
print(f'({base_converter(input_number,base_in,base_out)[1]} = {input_number})')
print('')