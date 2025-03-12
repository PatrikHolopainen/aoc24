import re



with open('input.txt') as f:
    for l in f.readlines():
        if 'A:' in l:
            # Search the only number in the line using re
            A = int(re.search(r'\d+', l).group())
        elif 'B' in l:
            B = int(re.search(r'\d+', l).group())
        elif 'C' in l:
            C = int(re.search(r'\d+', l).group())
        else:
            if ',' in l:
                ops = [int(i) for i in l.split()[1].split(',')]


print(A)
print(B)
print(C)
print(ops)

def operate(A,B,C,ops,ins_pointer,output):
    # print("A:",A,"B:",B,"C:",C,"ops:",ops[ins_pointer:ins_pointer+2])
    
    opcode = ops[ins_pointer]
    operand = ops[ins_pointer+1]

    def combo(n):
        if n < 4:
            return n
        elif n == 4:
            return A
        elif n == 5:
            return B
        elif n == 6:
            return C

    if opcode == 0:
        A = A//(2**combo(operand))
        return A,B,C,ops,ins_pointer+2,output
    elif opcode == 1:
        B = B^operand
        return A,B,C,ops,ins_pointer+2,output
    elif opcode == 2:
        B = combo(operand)%8
        return A,B,C,ops,ins_pointer+2,output
    elif opcode == 3:
        if A != 0:
            ins_pointer = operand
            return A,B,C,ops,ins_pointer,output
        else:
            return A,B,C,ops,ins_pointer+2,output
    elif opcode == 4:
        B = B^C
        return A,B,C,ops,ins_pointer+2,output
    elif opcode == 5:
        output += str(combo(operand)%8) + ","
        return A,B,C,ops,ins_pointer+2,output
    elif opcode == 6:
        B = A//(2**combo(operand))
        return A,B,C,ops,ins_pointer+2,output
    elif opcode == 7:
        C = A//(2**combo(operand))
        return A,B,C,ops,ins_pointer+2,output


program_s = ""
target_s = (',').join([str(o) for o in ops]) + ','

global best
best = 0

def run_program(A,B,C,ops,target_s):
    ins_pointer = 0
    output = ""

    while ins_pointer < len(ops): # 
        # print(output == target_s[0:len(output)])
        global best
        if len(output) > best:
            best = len(output)
            # print(best,A2,output)
        A,B,C,ops,ins_pointer,output = operate(A,B,C,ops,ins_pointer,output)
        # print(output,target_s[0:len(output)])
    return output

test = 0

global A2

a_485 = ''
bs =   "11001110101111001100111111101"
# bs = "11000100101001 0 11000001"
bs = "101011000 0 011101 0 011 01"

print(bs)

print(193,bin(193))
print(12585,bin(12585))
print(6443713,bin(6443713))
print(433560061,bin(433560061))
# 433560061 2,4,1,3,7,5,4,0,



bs = '1011100110001000011101011110101100011010000000'


A2 = int(bs.replace(" ", ""), 2)



single_run = False


# 2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0

# 193 -> 1,3,0,
# 12586 -> '3,5,5,3,0,'



# Ajettu 175M iteraatiota ilman modulo_filtterii.
# Ajettu 540M iteraatiota ilman modulo_filtterii.

# Ajettu 1,5B itearaatiota filtterin kanssa
# Ajettu 3,0B itearaatiota filtterin kanssa

# target_s = '2,4,1,3,7,5,4,0,'
target_s = '2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0,'
# target_s = '1,3,0,3,5,5,3,0,'

subs = []
aas = []


low  = 108_107_614_000_000
high = 108_107_631_000_000


low = 45_000_000_000_000
high = 281_000_000_000_000

A2 = low

def evenly_spaced_integers(a, b, n):
    if n <= 1:
        return [a]
    step = (b - a) / (n - 1)
    return [round(a + i * step) for i in range(n)]


def inner(low,high,right_idx,target_s):
    print("Starting inner")
    outputs = [(k, run_program(k,B,C,ops,target_s)) for k in evenly_spaced_integers(low,high,1000)]
    new_low = low
    new_high = high
    seq = False
    for i in range(len(outputs)):
        value,output = outputs[i]
        if output == target_s:
            print(output,target_s,value,"FOUND ITTT!!!!")
            exit()
        if target_s[-right_idx:] == output[-right_idx:]:
            
            print("Matching number",value,output,right_idx,target_s[-right_idx:],output[-right_idx:])
            seq = True
        else:
            if seq: # Lopetetaan seq
                seq = False
                new_high = value
                inner(new_low,new_high,right_idx+2,target_s)
            else:
                new_low = value
                


inner(low,high,2,target_s)

"""o = run_program(281*10**12,B,C,ops,target_s)

print(o,len(o))"""

"""

print(target_s)
while program_s != target_s and target_s and A2 < high+1:
    program_s = run_program(A2,B,C,ops,target_s)
    # print(A2,program_s,"vs",target_s)
    # print(program_s,len(program_s)/2)
    #print(target_s,program_s)
    
    # print(A2)
    # print(target_s)
    if A2 % 1_000_000 == 0:
        print(A2)
    A2 += 1
    if single_run:
        break
    

print(A2)
print(target_s)
print(program_s)

"""