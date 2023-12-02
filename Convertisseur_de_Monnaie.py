from forex_python.converter import CurrencyRates

def convert_and_save(to_currencies, filename):
    amount = float(input("Veuillez entrer le montant que vous souhaitez convertir : "))
    from_currency = input("Veuillez entrer la devise d'origine (par exemple 'EUR') : ")
    
    # Ajout de la possibilité d'ajouter des devises préférées
    add_favorite = input("Voulez-vous ajouter une devise préférée ? (Oui/Non) : ").lower()
    if add_favorite == 'oui':
        favorite_currency = input("Veuillez entrer la nouvelle devise préférée : ")
        to_currencies.append(favorite_currency.upper())
    
    forex_python = CurrencyRates()
    for to_currency in to_currencies:
        try:
            result = forex_python.convert(from_currency, to_currency, amount)
            with open(filename, 'a') as f:
                f.write(f"{from_currency} to {to_currency}, {amount} : {result}\n")
            print(f"{amount} {from_currency} est égal à {result} {to_currency}")
        except Exception as e:
            print(f"La conversion de {from_currency} à {to_currency} n'est pas possible.")

# Exemple d'utilisation avec des devises préférées
convert_and_save(['USD', 'JPY', 'GBP', 'PLN', 'THB', 'NOK'], 'history.txt')