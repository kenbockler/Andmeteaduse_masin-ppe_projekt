def sünnikuupäev(n):
    date = n[5:7]
    month = n[3:5]
    year = n[1:3]
    monthlist = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    if (n[0] == "1" or n[0] == "2"):
        year = f"18{str(year)}"
    elif(n[0] == "3" or n[0] == "4"):
        year = f"19{str(year)}"
    elif(n[0] == "5" or n[0] == "6"):
        year = f"20{str(year)}"
    else:
        year = f"21{str(year)}"
    return f"{date}. {monthlist[int(month)-1]} {year}"
