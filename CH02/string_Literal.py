word="goal"
#word[0]="f"#報錯(當出現報錯，造成阻斷，可將錯誤段加上註解符號，讓其他行繼續運行直譯)
word="f"+word[1:]#正確
print(word)#