import random
YELLOW = "\033[33m"
RESET = "\033[39m"

def pp(poker: list, highlighted: list = []):
    print("当前牌：")
    for i in range(len(poker)):
        print("【", end="")
        highlight = False
        for j in range(len(highlighted)):
            if i == highlighted[j]:
                highlight = True
        if highlight:
            print(YELLOW + poker[i] + RESET, end="")
        else:
            print(poker[i], end="")
        print("】", end="")
    print("\n")

print()
print("撕开的牌假设是【1 和 1-】，【2 和 2-】，【3 和 3-】，【4 和 4-】。将两份各四张牌按顺序放在手上。")
print("顺序：左边为最上面的牌，右边为最下面的牌")
poker = ["1", "2", "3", "4", "1-", "2-", "3-", "4-"]
pp(poker)

#step
print("把最上面的牌放到最下面，名字有几个字，就重复几次。（这一步在藏牌之前，所以都不影响）")
random_1 = random.randint(1,7) # random 1-7, name length
print("名字长度：", random_1)
for i in range(random_1):
    poker = poker[1:] + poker[0:1]
pp(poker)

#step
print("拿起最上面三张，插入中间任意位置，但不要碰到最后一张。（因为一共四张牌，这一步将最后一张牌和第一张牌调成相同。")
random_2 =random.randint(4,7) # 不要碰最后一张
print("插入位置：", random_2)
poker = poker[3:random_2] + poker[0:3] + poker[random_2:]
pp(poker,[0,7])

# step
print("最上面这张卡片，藏起来。（与最后一张相同）")
hide = poker[0]
poker = poker[1:]
print("藏起来的卡片是：" + YELLOW + hide + RESET)
pp(poker,[6])

#step
print("南方人拿起一张，北方人拿起两张，不确定拿起三张，插到剩下的中间，不要碰到最后一张。（这一步不影响最后一张牌）")
random_3 = random.randint(1,3) # 南 1/北 2/不确定 3
print("南 1/北 2/不确定 3：", random_3)
random_4 = random.randint(3,5) # 不要碰最后一张
poker = poker[random_3:random_4] + poker[0:random_3] + poker[random_4:]
pp(poker,[6])

#step
print("男生拿一张，女生拿两张，扔出去。（这一步不影响最后一张牌）")
random_5 = random.randint(1,2) # 男 1/女 2
print("男 1/女 2：", random_5)
poker = poker[random_5:]
pp(poker,[len(poker)-1])

#step 七字真言： “见证奇迹的时刻”
print("七字真言： “见证奇迹的时刻”，将最上面的牌放到最后，重复七次。（这一步让男生的牌是xxxxAx，女生的牌是xxAxx，A是想要的牌，x是其他杂牌）")
for i in range(7):
    poker = poker[1:] + poker[0:1]
if random_5 == 1:
    pp(poker,[4])
else:
    pp(poker,[2])

#step 5 “好运留下来，烦恼丢出去”
print("“好运留下来，烦恼丢出去”，将最上面的牌一张放到最后，一张扔掉。（这一步让上述男女两种顺序的牌都能剩下想要的牌）")
print("男：xxxxAx -> xxAxx -> Axxx -> xxA -> Ax -> A")
print("女：xxAxx，就是男生操作完第一步后的情况")
for i in range(10):
    poker = poker[1:] + poker[0:1]
    poker = poker[1:]
    pp(poker)
    if len(poker)==1:
        break

print("最后剩下的牌是：" + YELLOW + poker[0] + RESET)
print()
