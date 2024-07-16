def find_kth_number(K):
    # Kを2進数に変換し、その各桁の'1'を'2'に置き換える
    binary_representation = bin(K)[2:]  # '0b'を取り除く
    return int(binary_representation.replace('1', '2'))

K = int(input())
print(find_kth_number(K))


