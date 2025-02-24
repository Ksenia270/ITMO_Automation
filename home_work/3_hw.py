def arbitrary_number(number_1,number_2):
 if number_1>=number_2: print(number_1)
 else: print(number_2)
arbitrary_number(135,136)


def arbitrary_number(number_1,number_2):
 if (number_1-number_2)==135: print("YES")
 else: print("NO")
arbitrary_number(135,1)

def season_of_the_year(month_number):
 if month_number == 1 or month_number == 2 or month_number == 12:
    print("Зима")
 elif month_number in range(3,6):
    print("Весна")
 elif month_number in range(6,9):
    print("Лето")
 elif month_number in range(9,12):
    print("Осень")
season_of_the_year(1)



def arbitrary_number(number_1,number_2,number_3):
 if number_1 > 10 and number_2 > 10 and number_3 > 10:
    print("yes")
 else:
    print("no")
arbitrary_number(67,15,20)



