# sort methodundan istifade olunacaq 
# sort()elifba sirasi ve ya artan sira ile gosterir
# sort(reverse=True) elifba sirasinin eksi,azalan sira ile gosterecek
L = [3, 6, 7, 4, -5, 4, 3, -1]

#1.
if sum(L)>2:
    print(len(L))

#2.
if abs(max(L)-min(L))>10:
    print(sorted(L))
else: 
    print("Ferq 10-dan kichik-beraberdir.")