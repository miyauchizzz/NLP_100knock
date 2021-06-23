str1 = "パトカー"
str2 = "タクシー"
ans = "".join([c1 + c2 for c1, c2 in zip(str1, str2)])

print(ans)
