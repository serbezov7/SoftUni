def tribonacci_sec(num):
    trib_first = 0
    trib_second = 0
    trib_third = 1
    tribonacci_numbers = ["1"]
    for current_num in range(num - 1):
        tribonacci_current = trib_first + trib_second + trib_third
        tribonacci_numbers.append(str(tribonacci_current))
        trib_first = trib_second
        trib_second = trib_third
        trib_third = tribonacci_current
    return tribonacci_numbers


number = int(input())
print(" ".join(tribonacci_sec(number)))
