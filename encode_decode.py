strs = ["neet","code","love","you"]
encode_str = ''
# for index,str in enumerate(strs):
#     for char in str:
#         encode[index] += f"+{ord(char)}"
#     encode[index] += f"thisIsARandomSplitter"
# for index,str in enumerate(strs):
#     encode_str += str
#     encode_str += f"thisIsARandomSplitter"
    
# print(encode_str)

# decode_str = encode_str.split("thisIsARandomSplitter")
# print(decode_str)

for str in strs:
    encode_str += f"{len(str)}#{str}"
print(encode_str)
i = 0
decode_strs = []
while i < len(encode_str):
    j = i
    length_sub_s = 0
    while j < len(encode_str):
        if encode_str[j] == "#":
            # print(encode_str[i:j])
            # print(int(encode_str[i:j]))
            len_of_sub_string = int(encode_str[i:j])
            print(len_of_sub_string)
            length_sub_s = len_of_sub_string
            # print(len_of_sub_string)
            # print(f"{j+1}      {j+len_of_sub_string}")
            print(encode_str[j+1:j+len_of_sub_string+1])
            decode_strs.append(encode_str[j+1:j+len_of_sub_string+1])
            # pass
            break
        j += 1
    i = j+length_sub_s+1
print(decode_strs)