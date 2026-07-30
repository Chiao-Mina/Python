#這段是在教 整數轉浮點數、判斷浮點數是否為整數，以及四捨五入。
f, i=1.2345,12345  #動態資料型別可(f是float)浮點數<轉換>(i)整數
print(type(f))  #表示 f 的資料型態是浮點數。
f2=float(i)#把整數 12345 轉成浮點數12345.0
print(f2)#因為f2轉為浮點，所以輸出12345.0
print(float.is_integer(f))#s_integer() 是用來判斷：這個浮點數有沒有小數部分？f是1.2345，有小數部分，所以輸出false
print(float.is_integer(f2))#f2是12345.0雖然型態是浮點數，但數值上等於整數，沒有有效的小數部分，所以結果是True;也可以寫成比較常見的形式：print(f.is_integer())、print(f2.is_integer())
print(round(f,2))#把 f 四捨五入到小數點後 2 位1.23，因為第三位小數是 4，不用進位。
print(round(f))#不指定小數位數時，會取最接近的整數1
#這段的核心是：float(i)把整數轉成浮點數。
#f.is_integer()判斷一個浮點數的數值是否等同整數。
#round(數值, 位數)進行四捨五入。