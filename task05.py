  
s = "У лукоморья 123 дуб зеленый 456"
if 'я' in s:
    print(f'1) Bu setirde "я" herfi{s.index("я")}-cu indexdedir')
else:
    print('1) Bu setirde "я" herfi yoxdur')
print(f'2) Bu setirde "у" herfi {s.count("у")} defe istirak edib.')
if s.isalpha() == False:
    print(f'3) Bu setir yalniz herflerden ibaret deyil, Setrin boyuk herflerle gorunusu bu sekildedir:{s.upper()}')
else:
    print('3) Setir ancaq herflerden ibaretdir')
if len(s) > 4:
    print(f'4) Setrin uzunlugu:{len(s)}-dir, Setrin kicik herflerle gorunusu bu sekildedir: {s.lower()}')
print(f'5) О{s[1:]}')
