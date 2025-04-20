s = "00111"
"""
0|0111
"""
r = s.count("1")
l = ans = 0
print(s[:-1])
for i in s:
    if i == "0":
        l += 1
        print("Left score is",l)
    else:
        r -= 1
        print("Right score is",r)
    ans = max(ans,l+r)
print(ans,r+l)