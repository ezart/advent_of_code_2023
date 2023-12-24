total = 0
def get_calibration(line):
    res = []
    for i in line:
        if  ord('0')<= ord(i) <= ord('9'):
            res.append(int(i))
    
    print(res)
    return res[0] * 10 + res[-1]



with open("day_1.txt","r") as f:
    lines = f.readlines()
    # breakpoint()
    for line in lines:
        print(line)
        total += get_calibration(line)

print(total)

assert get_calibration("nlnineeightmndkqz8nineonenrqm") == 88 , "nlnineeightmndkqz8nineonenrqm must return 16"
assert get_calibration("bzp292one78rthree") == 28, "bzp292one78rthree should return 28"
# assert get_calibration("nlnineeightmndkqz8nineonenrqm") == 18 , "nlnineeightmndkqz8nineonenrqm must return 16 not 16"
# print(get_calibration("bzp292one78rthree"))