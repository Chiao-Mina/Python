#除非用到大數據，不然一般不常使用
#解決浮點數 (float) 計算不精確的問題。
import decimal #把 Python 的 decimal 模組載入。
f1,f2=10.0,3.0
d1=decimal.Decimal(10)
d2=decimal.Decimal('3.0')
print(type(d1))
print(f1/f2)#小的會成大的，自動(隱含)型別轉換。與int強制型別轉換
print(d1/d2)
d3=decimal.Decimal('2.345')#自串常值轉換Decimal型別變數
d4=decimal.Decimal('6.78')
print(d3+d4)
print(d3*d4)
#float：一般浮點數，精度有限; Decimal：十進位高精度數值
#Decimal
# 運算 ｜規則                    ｜案例
# +、- ｜取小數點後最多的(最精確的)｜max(3,2)=3
# *、/ ｜兩者小數點後位數相加      ｜3+2=5