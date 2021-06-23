str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
splits = str.split()
select_number = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans = {}
for i, word in enumerate(splits):
  if i + 1 in select_number:
    ans[word[:1]] = i + 1
  else:
    ans[word[:2]] = i + 1

print(ans)
