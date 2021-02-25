userinput = input("write an 8 bit string: ")

"""byte_array = bytearray(userinput,"utf8")

byte_list = []

for byte in byte_array:
    binary = bin(byte)
    byte_list.append(binary)

print(byte_list)
"""
def String2Byte(string):
    # denne funktion tager en string og laver den om til 
    byte_array = bytearray(userinput,"utf8")

    byte_list = []

    for byte in byte_array:
        binary = bin(byte)[2:]
        byte_list.append(binary)

    print(byte_list)









