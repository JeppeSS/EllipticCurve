"""
an assumption is made, that the function format(ord(c), 'b')) should never
return a binary number longer than the variable CHAR_LENGTH
"""
import binascii

CHAR_LENGTH = 8
length_of_bin = CHAR_LENGTH * 32

empty_space = '00100000'
FORMAT = '#_#_#'


def prepend_zero(s, intended_length):
    zeroz = ['0' for x in range(0, (intended_length - len(s)))]
    zeroz += s
    return zeroz

def make_char_bin(c):
    c_as_ascii = c.encode('utf-8')
    new_c = ''.join(format(ord(c_as_ascii), 'b'))
    new_c = prepend_zero(new_c, CHAR_LENGTH)
    return new_c

def return_binary(f):
    all_in_one = []
    for l in f:
        tmp = [make_char_bin(c) for c in l]
        all_in_one += tmp
        all_in_one.append(make_char_bin('\n'))
    return all_in_one

def convert_to_correct_length(f):
    l = return_binary(f)
    tmp_str = ''
    for b in l:
        tmp_str += ''.join(b)
        if len(tmp_str) % 8 != 0:
            raise
    while len(tmp_str) % length_of_bin > 0:
        tmp_str += empty_space

    l_correct_length = [tmp_str[i:i + length_of_bin] for i in range(0, len(tmp_str), length_of_bin)]

    return l_correct_length


def factor(l, key, divide=False):
    new_l = []
    for s in l:
        if divide:
            factored_chars = str(bin(int(s, 2) // key))
        else:
            factored_chars = str(bin(int(s, 2) * key))
        if 'b' in factored_chars:
            x_1, x_2 = factored_chars.split('b')
            factored_chars = x_1 + x_2

        new_l.append(factored_chars)
    return new_l



def decrypt(f_name, key):
    f = open(f_name)
    encrypted_lines = [x for x in f]
    f.close()
    str_lines = []
    for l in encrypted_lines:
        a, b, c = l.split(FORMAT)
        str_lines.append(b)
    decrypted_l = factor(str_lines, key, True)

    asd = []
    for l in decrypted_l:
        asd += [l[i:i+CHAR_LENGTH] for i in range(0, len(l), CHAR_LENGTH)]
    return asd


def encrypt(f_name, key):
    f = open(f_name)
    l = convert_to_correct_length(f)
    m = factor(l, key)

    new_f = open(('encrypted_' + f_name), "w+")
    for entry in m:
        new_f.write(FORMAT+entry+FORMAT+'\n')
    f.close()


f = open('some.txt')

encrypt('some.txt', 40)

wwww = decrypt('encrypted_some.txt', 40)


for qq in wwww:
    n = int(qq, 2)
    try:
        print(binascii.unhexlify('%x' % n))
    except:
        print('--------------------')
        print(qq)
        print('--------------------')


print('lol')
#print(make_char_bin('a'))
#print(wwww)
#for y in wwww:
#    print(y)
#    o = int(y, 2)
#    print(o.to_bytes(1, 'big').decode())

