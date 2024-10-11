import random
import time

# Simuloidaan valuutan hinta ja palautetaan kahden desimaalin tarkkuudella
def simulate_price(price: int):
    change_percentage = random.uniform(-1.5, 1.5)
    new_price = price * (1 + change_percentage / 100)

    return round(new_price, 2)


# Lasketaan prosentuaalinen muutososuus ja palautetaan kahden desimaalin tarkkuudella
def calculate_percentage(price: int, new_price: int):
    percentage = ((new_price - price) / price) * 100
    return round(percentage, 2)


def print_stocks(stock_dict: dict, current_price: float):
    print(f"\nOstetut valuutat:")
    if stock_dict:
        for key, value in stock_dict.items():
            change = calculate_percentage(current_price, value[1])
            print('change:', change)
            print(f"ID: {key} -> Päivä: {value[0]} || Hinta: {value[1]} USD ({change}%)")
            stock_dict[key] 
    else:
        print("Ei ostettuja valuuttoja.")
    
    return None

def sell_stocks(stocks: dict, current_price: float):
    if not stocks:
        print("Ei osakkeita myytävänä.")
        return
    
    while True:
        print("\nMyytävissä olevat osakkeet:")
        for key, value in stocks.items():
            change_percentage = calculate_percentage(current_price. value[1])
            print(f"ID: {key} -> Ostopäivä: {value[0]} || Hinta: {value[1]} USD ({change_percentage}%)")

        try:
            id = int(input("Anna ID myytävästä osakkeesta, 0 palataksesi: "))
        except ValueError:
            print("Virheellinen syöte. Anna numero.")
            continue

        if id == 0:
            break
        elif id in stocks:
            stock = stocks.pop(id)  # Poistetaan osake, kun se myydään
            print(f"Osake myyty päivänä {stock[0]} hintaan {stock[1]} USD")
            break
        else:
            print("Virheellinen ID. Yritä uudelleen.")
            
    return None

def buy_stock(stocks: dict, buying_price: float, day: int):
    print()
    stocks[len(stocks) + 1] = (day, buying_price)
    print(f"\tOsake ostettu päivänä {day} hintaan: {buying_price} USD")

    return None

# Funktio, joka käsittelee käyttäjän valinnat
def user_selection(stocks: dict, current_price: float, change_percentage: float, day: int):
    while True:

        try:
            user_select = int(input("Vaihtoehdot:\n(1) Osta\n(2) Salkku\n(3) Myy\n(4) Nuku päivä\n(0) Lopeta: "))
        except ValueError:
            print("Virheellinen valinta! Anna valintasi kokonaislukuna")
            continue  # Palaa kysymään valintaa

        if user_select == 1:
            buy_stock(stocks, current_price, day)
            break  # Palataan pääohjelmaan
        elif user_select == 3:
            sell_stocks(stocks, current_price)
            break  # Palataan pääohjelmaan
        elif user_select == 2:
            print_stocks(stocks, current_price)
            break  # Palataan pääohjelmaan
        elif user_select == 4:
            print("Päivä nukuttu.")
            break  # Palataan pääohjelmaan
        elif user_select == 0:
            print("Lopetetaan ohjelma.")
            exit()  # Poistutaan ohjelmasta
        else:
            print("Virheellinen valinta, yritä uudelleen.")

    return None


## PÄÄOHJELMA ##
def main():
    # Muuttujat
    stock_dict = {}
    stock_price = 1000  # Valuutan alkuhinta
    new_stock_price = 0
    day = 1
    print("*** Vtoro ***")

    while True:
     
        # Päivitä hinta
        new_stock_price = simulate_price(stock_price)

        print(f"Osakkeen hinta päivälle {day}: {new_stock_price} USD")

        # Lasketaan prosentuaalinen muutos
        change_percentage = calculate_percentage(stock_price, new_stock_price)
        print(f"Prosentuaalinen muutos eiliseen: {change_percentage}%")

        # Käsitellään käyttäjän valinta
        user_selection(stock_dict, new_stock_price, change_percentage, day)

        # Päivitä uusi hinta
        stock_price = new_stock_price


        # Siirrytään seuraavaan päivään
        day += 1

        # Odota ennen seuraavaa päivitystä
        time.sleep(0.5)
        print("\n" + "#" * 10 + "\n")

if __name__ == "__main__":
    main()
