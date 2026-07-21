flavor = "fig pie"
print(flavor[0:3])#FIG
print(flavor[3:7])#PIE
print(flavor[3:])#從3開始PIE
print(flavor[:])#FIG PIE
print(flavor[:14])#開始沒有指定就從頭開始FIG PIE
print(flavor[13:15])#並13及15空值，輸出空字串，不會報錯

print(flavor[-7:-4])#FIG
print(flavor[-7:0])#相同位置，等同於[0:0]，得到空值
print(flavor[-7:])#沒有指定結尾FIG PIE
print(flavor[-2:])#PIE
#對應如下:
#F   I   G       P  I  E
#0   1   2   3   4  5  6
#-7 -6  -5  -4  -3 -2 -1