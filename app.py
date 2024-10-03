import random
import time

# Simuloidaan valuutan hinta ja palautetaan kahden desimaalin tarkkuudella
def simulate_price(price: int):
    change_percentage = random.uniform(-1.5, 1.5)
    new_price = price * (1 + change_percentage / 100)

    return round(new_price, 2)


# Lasketaan prosentuaalinen muutososuus ja palautetaan kahden desimaalin tarkkuudella
def calculate_percentage(new_price: int):
    start_price = 1000
    percentage = ((new_price - start_price) / start_price) * 100

    return round(percentage, 2)


def print_stocks(stock_dict: dict):
    print(f"\nOstetut valuutat:")
    for key, value in stock_dict.items():
        print(f"ID: {key} -> H: ${value[0]} || %: {value[1]}%")
    
    return None


def sell_stocks(stocks: dict):
    print()

    while True:
        if not stocks:
            print("Ei osakkeita myytävänä.")
            break

        for key, value in stocks.items():
            print(f"ID: {key} -> Hinta: {value[0]} USD || Muutos: {value[1]}%")
        
        try:
            id = int(input("Myytävän osakkeen id, 0 palataksesi: "))
        except ValueError:
            print("Virheellinen syöte. Anna numero kokonaislukuna.")
            continue

        if id == 0:
            break
        elif id in stocks:
            stock = stocks.pop(id) # Poiistetaan osake myynnin jälkeen
            print()
            print(f"Osake myyty hintaan {stock[0]} USD ({stock[1]}%)")
            print()

    return None



## PÄÄOHJELMA ##
def main():
    # Muuttujat
    stock_dict = {}
    current_price = 1000  # Valuutan alkuhinta
    print("Simuloidaan kryptovaluutan hinnan vaihtelua. Aloitushinta on:", current_price)

    while True:
        # Päivitä hinta
        current_price = simulate_price(current_price)
        print(f"Kryptovaluutan hinta: {current_price} USD")

        # Lasketaan prosentuaalinen muutos
        change_percentage = calculate_percentage(current_price)
        print(f"Prosentuaalinen muutos: {change_percentage}%")

        # Tallennetaan osto tupleen (current_price, change_percentage)
        user_select = input("Haluatko (O)staa, (M)yydä tai (X) lopettaa? ").lower()

        if user_select == "o":
            stock_dict[len(stock_dict) + 1] = (current_price, change_percentage)
            print(f"Valuutta ostettu hintaan {current_price} USD, muutos {change_percentage}%")
        elif user_select  == "m":
            sell_stocks(stock_dict)
        elif user_select == "p":
            print_stocks(stock_dict)
        elif user_select == "x":
            break

        # Odota ennen seuraavaa päivitystä
        print("\n" + "#" * 10 + "\n")

if __name__ == "__main__":
    main()
