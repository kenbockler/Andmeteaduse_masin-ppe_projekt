a_tulu = float(input("Sisesta aastatulu: "))
while a_tulu <= 0:
    a_tulu = float(input("Sisesta aastatulu (peab olema mittenegatiivne arv): "))
m_tulu = 0.0
määr_1 = float(6000)
määr_2 = float(14400)
määr_3 = float(25200)
if a_tulu < määr_1:
    m_tulu = a_tulu
elif a_tulu < määr_2:
    m_tulu = määr_1
elif a_tulu < määr_3:
    m_tulu = määr_1-määr_1/10800*(a_tulu-määr_2)
print("Maksuvaba tulu:", round(m_tulu, 2))