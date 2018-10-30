def num_split(num):
    a = []
    for i in str(num):
        a.append(int(i))
    return a

print(num_split(240))

def tranfer(num):
    f0 = {
        0: "khong",
        1: "mot",
        2: "hai",
        3: "ba",
        4: "bon",
        5: "nam",
        6: "sau",
        7: "bay",
        8: "tam",
        9: "chin"
    }

    prefix = " "

    f1 = ["", "muoi", "tram"]
    f2 = ["", "nghin", "trieu", "ti"]

    digits = len(str(num)) % 3
    loop = len(str(num)) / 3
    word = ""
    level2 = 0
    
    while(num > 0):
        result = ""
        level1 = 0
        for i in num_split(num % 100):
            result = result + f0[i] + f1[level1] + prefix 
            level1 += 1
        word = result + f2[level2] + word
        level2 += 1
        num = int(num / 100)
    
    return word
    

nums = [11, 15, 10, 1234, 20, 21, 100, 1000, 12300, 151100]
for i in nums:
    print(tranfer(i))

# print(tranfer(nums[0]))
