import datetime
from dis import get_instructions
from distutils.ccompiler import gen_lib_options
from errno import ENOTCONN

data=datetime.datetime.now()
nasc=datetime.datetime(2002, 1, 3)

print(f"{data.day}/{data.month}/{data.year}")
print(nasc)
print(nasc.strftime("%A"))

# %a - dia da semana abreviado
# %A - dia da semana 
# %w - número do dia da semana => 0: Dom, 1: Seg, etc 
# %W - número da semana do ano
# %d - dia do mês
# %b - nome mês abreviado
# %B - nome mês 
# %m - número do mês
# %y - ano com dois dígitos
# %Y - ano com quatro dígitos
# %H - hora com dois dígitos 24h
# %I - hora com dois dígitos 12h
# %p - AM/PM 
# %M - minutos
# %S - segundos
# %f - microssegundos
# %j - dia do ano 001 - 366