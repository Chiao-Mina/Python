#
import decimal
d1=decimal.Decimal.from_float(123.4567)#from_float() 是把 float 轉成 Decimal資料型別;但是要注意，123.4567 和 34.5678 在變成 float 時，可能早已有些微誤差，所以轉成 Decimal 後，常會看到很長的數字。例如概念上可能接近：123.456699999999...
d2=decimal.Decimal.from_float(34.5678)#同上
print(decimal.getcontext())#getcontext() 是查看目前 Decimal 的運算環境，裡面包含：精度 prec、四捨五入方式 rounding、指數範圍、例外處理設定
print(decimal.getcontext().prec)#查看目前 Decimal 的有效位數。預設通常是28(一個運算結果最多保留 28 位有效數字；不是「小數點後 28 位」。)
#123.456總共有 6 位有效數字。
print(decimal.getcontext().rounding)#查看目前採用的取捨方式。預設通常是：ROUND_HALF_EVEN這叫「四捨六入五成雙」。(也就是遇到剛好是 5 時，會讓前一位變成偶數，而不一定每次都進位。)
print(d1+d2)#用目前預設精度進行加法:123.4567 + 34.5678 = 158.0245(from_float()，內部可能帶有 float 誤差，所以實際顯示可能不完全正好是 158.0245。)
decimal.getcontext().prec=8#把 Decimal 的有效位數改為 8 位；注意，這個設定主要影響「之後的運算結果」，不會直接改掉已建立的 d1、d2 內容。
print(d1+d2)#再次計算時，結果只保留 8 位有效數字:158.02450
#decimal.getcontext().prec=控制的是 有效位數，不是固定小數位數。
#decimal.getcontext().rounding=控制超過精度時，要用哪一種取捨規則。