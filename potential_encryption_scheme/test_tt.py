import tt
"""
With the test-file used contains 39 characters and the leading character in the
file being an 'a', the following tests should pass
"""

A = ['0', '1', '1', '0', '0', '0', '0', '1']

assert tt.prepend_zero('a', 4) == ['0', '0', '0', 'a']

assert tt.make_char_bin('a') == A

test_file = open('tt_test_text.txt')
ret_bin_test = tt.return_binary(test_file)
assert len(ret_bin_test) == 39
assert ret_bin_test[0] == A
test_file.close()

test_file = open('tt_test_text.txt')
conv_correct_len_test = tt.convert_to_correct_length(test_file)
assert len(conv_correct_len_test) == 2
assert len(conv_correct_len_test[0]) == tt.length_of_bin
test_file.close()


# Multiply
test_file = open('tt_test_text.txt')
MULTIPLIER = 5
multiply_test_data = tt.convert_to_correct_length(test_file)
multiply_test = tt.factor(multiply_test_data, MULTIPLIER)
assert int(multiply_test[0], 2) == int(multiply_test_data[0], 2) * MULTIPLIER
test_file.close()
