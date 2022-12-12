fail1nimi = str(input("Sisestage lähtefaili nimi: "));
fail2nimi = str(input("Sisestage sihtfaili nimi: "));
with open((fail1nimi), "r") as file1:
    file1andmed = file1.read();
vahetatudkogus = file1andmed.count("Hello");
file1andmed = file1andmed.replace("Hello", "Tere");
with open(fail2nimi, "w") as file2:
    file2.write(file1andmed);
print(vahetatudkogus);