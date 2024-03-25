def RLE_compress(input_string):
    input_list = list(input_string)
    run_length = 1
    output_string = ""
    i = 0
    for i in range (len(input_list) - 1):
        current_letter = input_list[i]
        next_letter = input_list[i + 1]

        if current_letter == next_letter:
            run_length += 1
            i += 1

        else:
            output_string += (current_letter + str(run_length))
            run_length = 1
    output_string += (input_list[len(input_list) - 1] + str(run_length))
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


