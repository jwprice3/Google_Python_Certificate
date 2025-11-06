################################
# Title: Google Python Certificate
# Description: Functions
# Change Log:
# JP, Created, 10.31.25
################################


print('Google Python Module_2 Practice.')
# def calculate_storage(filesize):
#     block_size = 4096
#     # Use floor division to calculate how many blocks are fully occupied
#     full_blocks = filesize // block_size
#     # Use the modulo operator to check whether there's any remainder
#     partial_block_remainder = filesize % block_size
#     # Depending on whether there's a remainder or not, return
#     # the total number of bytes required to allocate enough blocks
#     # to store your data.
#     if partial_block_remainder > 0:
#         return (full_blocks + 1) * block_size
#     return full_blocks * block_size

# # Test cases (all should now pass)
# print(calculate_storage(1))    # Outputs: 4096 (1 block for 1 byte)
# print(calculate_storage(4096)) # Outputs: 4096 (exactly 1 block)
# print(calculate_storage(4097)) # Outputs: 8192 (1 full + 1 partial = 2 blocks)
# print(calculate_storage(6000)) # Outputs: 8192 (1 full + partial = 2 blocks)

# # Extra test for larger file
# print(calculate_storage(8193)) # Outputs: 12288 (2 full + partial = 3 blocks)

# print('Google Python Module_2 Quiz.')
# print('big' > 'small')

# def difference(x, y):
#     z = x - y
#     return z
# print(difference(5, 3))

#print(((24 == 5*2) and (24 > 3*5) and (2*6 == 12)))