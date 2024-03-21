def RLE_compress(input_string):
    current_letter = input_string[0]
    iteration_count = 0
    output_string = ""
    i = 0
    while i < (len(input_string) - 1):

        while input_string[i] == current_letter and i < (len(input_string) - 1):
            iteration_count += 1
            i += 1
        if i < (len(input_string) - 1):
            output_string += (current_letter + str(iteration_count))
        else:
            if input_string[len(input_string) -1] == 
            output_string += (current_letter + str(iteration_count + 1))
        iteration_count = 0
        current_letter = input_string[i]
    return output_string





print(RLE_compress("AABBBAAAABBBBBAAAAAABBBBBBB"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFF"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFD"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFDD"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFDDD"))
print(RLE_compress("ABCDEF")) # as discussed, this one doesn't actually "compress", but it's a good test case
print(RLE_compress("FFFFFFFFFFFFFFFFFFF"))
print(RLE_compress("F"))
print(RLE_compress("F????"))
print(RLE_compress("Mmmmmmmmmm sooooo goooooood!"))
print(RLE_compress("Booooooooooooo, hisssssssss"))


