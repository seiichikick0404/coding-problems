# 2023/3/30

s = input()

output = ""
for i in range(len(s)):
    if s[i] == "0": output += "0"
    elif s[i] == "1": output += "1"
    elif s[i] == "B" and output != "": output = output[:-1]


print(output)
