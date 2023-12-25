balls_ids =[]
GREEN ="green"
BLUE ="blue"
RED ="red"
colors ={
    RED:12,
    GREEN:13,
    BLUE:14
}
with open("day_2.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        flag = True
        key = line.split(":")[0]
        key = key.split(" ")[1]
        # print(key)
        line_value = line.split(":")[1]
        sets = line_value.split(";")
        for s in sets:
            s.strip()
            # print(f"value {v}")
            balls = s.split(",")
            for ball in balls:
                color = ball.split()[1]
                num = ball.split()[0]
                # print()
                if colors[color] < int(num):
                    # print(f"color: {color}, num: {num}, key: {key}")
                    flag = False
        # print(key)
        if flag:
            balls_ids.append(int(key))
# print(balls_ids)
        
print(sum(balls_ids))