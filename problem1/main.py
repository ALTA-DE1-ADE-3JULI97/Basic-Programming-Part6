def compare(a, b):
    pattern = ""
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                substring = a[i]
                k = 1
                while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                    substring += a[i + k]
                    k += 1
                if len(substring) > len(pattern):
                    pattern = substring
    return pattern

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA