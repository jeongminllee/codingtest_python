def polynomial_rolling_method_v1(string_list):
    """
    문자열 해시 함수 수정 (전)
    hash(s) = ((s[0] * p^0) + (s[1] * p^1) + (s[2] * p^2) + ...(s[n - 1] * p^n-1)) mod m
    """
    p = 31
    maximum_hashsize = 0
    hash_list = []

    for string in string_list:
        hash = 0
        for idx, char in enumerate(string):
            hash_value = ord(char) * pow(p, idx)
            hash += hash_value
        maximum_hashsize += hash
        hash_list.append(hash)

    for idx in range(len(hash_list)):
        hash_list[idx] = hash_list[idx] % maximum_hashsize

    return hash_list


print(polynomial_rolling_method_v1(['apple', 'banana', 'cherry']))