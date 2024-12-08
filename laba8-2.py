def IncTime(h,m,s,t):
    s+=t
    sost=s//60
    s=s-(sost*60)
    m+=sost
    most=m//60
    m=m-(most*60)
    h+=most
    return(h,"часов",m,"минут",s,"секунд")

while True:
    h=input("Введите часы: ")
    if h.isdigit():
        h=int(h)
        break

while True:
    m=input("Введите минуты: ")
    if m.isdigit():
        m=int(m)
        break

while True:
    s=input("Введите секунды: ")
    if s.isdigit():
        s=int(s)
        break

while True:
    t=input("Введите добавочное время: ")
    if t.isdigit():
        t=int(t)
        break

print(*IncTime(h,m,s,t))