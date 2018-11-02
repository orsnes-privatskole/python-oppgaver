[<< Tilbake til oppgaver](https://github.com/orsnes-privatskole/python-oppgaver)

# Kalkulator i Python - tekstbasert

Bruk Python til å lage en kalkulator. Oppgaven er delt i to, «basic-edition» og «deluxe-edition» som er to vanskelighetsgrader på oppgaven. Begynner du med den enkle, kan du bygge den ut til «deluxe» etterpå.

Nyttig informasjon om Python funksjoner du trenger finner du på [https://orsnes-privatskole.github.io](https://orsnes-privatskole.github.io)

## Basic-Edition
Dette er en kalkulator som bare kan en type regneoperasjon. Du bestemmer om det er pluss, minus, gange eller deling. Lag et Python program som spør brukeren om å taste inn to tall, og så skriver du ut svaret når du behandler disse to tallene med den regneoperasjon du har valgt.
Eksempel på hvordan det kan se ut når det brukes:

```
**************************************************
Welcome to My Calculator - Basic Edition v0.1
This calculator let you add two numbers
**************************************************

Please input the first number: 34
Please input the second number: 54
The two numbers added are: 88

Thank you for using My Calculator - Basic Edition v0.1
Goodbye...
```

### Del A - Regn et enkelt stykke

- Start med å lage en variabel som inneholder informasjon om navn og versjon på kalkulatoren
- Skriv ut en velkomsttekst som forteller hva kalkulatoren heter, og hva den kan gjøre
- Be brukeren om å skrive inn tall 1 og tall 2
- Skriv ut svaret

#### Relevante avsnitt i hjelpeteksten
- [Skriv ut på skjermen](https://orsnes-privatskole.github.io/#skriv-ut-tekst-p%C3%A5-skjerm)
- [Les inn data fra brukeren](https://orsnes-privatskole.github.io/#les-inn-tekst--tall-fra-bruker)
- [Gjør om innlest tekst til tall](https://orsnes-privatskole.github.io/#gj%C3%B8r-om-input-til-tall)
- [Beregninger og operatorer](https://orsnes-privatskole.github.io/#beregninger-og-operatorer)

<details>
<summary>Løsningsforslag - Kalulator Basic - Del A</summary>

```python
# Calculator - Basic Edition

# Name and version info
version_info = "MyCalculator - Basic Edition v0.1"

# Print welcome text
print('\n')
print('*' * 50)
print("Welcome to " + version_info)
print("This calculator let you add two numbers")
print('*' * 50 + '\n')

# Get user to input numbers to be calculated
number_a = int(input("Please input the first number: "))
number_b = int(input("Please input the second number: "))

# Calculate answer
result = number_a + number_b

# Print answer
print(f"The two numbers added are: {result}")

# Print goodbye message
print("\nThank you for using " + version_info)
print("Goodbye...")
```

</details>

### Del B - Regn flere stykker

Når brukeren har fått regnet ut et stykke i Del A, så avslutter programmet. I denne delen utvider vi det til å kunne regne ut flere stykker helt til brukeren velger å avslutte, det kan f.eks. se slik ut:

```

The two numbers added are: 118

Do you want to calculate more? (y/n) y
Please input the first number: 564
Please input the second number: 943
The two numbers added are: 1507

Do you want to calculate more? (y/n) n

```

Det kan nå passe å flytte selve utregningen inn i en funksjon, det vil også komme til nytte når vi går over til Deluxe utgaven.

#### Relevante avsnitt i hjelpeteksten
- [Variabel typer](https://github.com/orsnes-privatskole/orsnes-privatskole.github.io#variabel-typer)
- [Funksjoner](https://github.com/orsnes-privatskole/orsnes-privatskole.github.io#funksjoner)

<details>
<summary>Løsningsforslag - Kalkulator Basic - Del B</summary>

```python
# Calculator - Basic Edition

# Name and version info
version_info = "MyCalculator - Basic Edition v1.0"


# Function to add two numbers, and returning the result
def add_numbers(a, b):
    return a + b


# Print welcome text
print('\n')
print('*' * 50)
print("Welcome to " + version_info)
print("This calculator let you add two numbers")
print('*' * 50 + '\n')

# Variable to keep track of the user choice to continue or exit
user_exit = False

# Repeat until the user choose to exit
while not user_exit:

    # Get user to input numbers to be calculated
    number_a = int(input("Please input the first number: "))
    number_b = int(input("Please input the second number: "))

    # Calculate result
    result = add_numbers(number_a, number_b)

    # Print answer
    print(f"The two numbers added are: {result}")

    # Ask if user want to do more calculations
    answer = input("\nDo you want to calculate more? (y/n) ")
    # Ensure input is in lower case so both y/n and Y/N are valid inputs
    answer = answer.lower()
    if answer != 'y':
        user_exit = True

# Print goodbye message
print("\nThank you for using " + version_info)
print("Goodbye...")


```

</details>

## Deluxe-Edition

I *Deluxe* utgaven av kalkulatoren vår, så vil vi ha minst 4 regneoperasjoner, som f.eks pluss, minus, gange og deling. Får du det til kan du også legge til flere som kvadratrot.

Kalkulatoren skal tilby en meny hvor brukeren først velger regneoperasjon, så leser inn hvilke tall som skal brukes og gjennomfører regneoperasjon.

Kalkulatoren bør sjekke at brukeren skriver inn gyldige verdier, - f.eks. at det er et tall der det forventes et tall, - og at det brukes et gyldig menyvalg. Hvis ikke skal det gis en fornuftig feilmelding og sjanse til å rette opp.

Eksempel på hvordan det kan se ut i bruk:

```
******************************
Welcome to MyCalculator
 - Deluxe Edition v1.0
******************************
Choose type of calculation or exit
******************************
* Addition:       +
* Subtraction:    -
* Multiplication: *
* Division:       /
* Exit:           e
******************************
Please choose your option: /
Please input number: 48
Please input number: 8

** Calculation 48 / 8 = 6.0
```

### Del A - Vis meny og la bruker velge

Vi starter med å lage en funksjon som viser menyen over tilgjengelige valg, og som ber brukeren velge. Funksjonen skal *validere* (sjekke om input er gyldig), før den returnerer valgt funksjonalitet. Om brukeren ikke velger et valg som er tilgjengelig, så vil funksjonen informere om dette og så spørre igjen.

#### Tips
For å sjekke om input er gyldig, så kan man ha en ``liste`` med gyldige valg, og så bruke Python funksjonen ``in`` for å sjekke om det brukeren har tastet inn finnes i listen.

Eksempel:
```python
# Liste (variabel) med alle gyldige menyvalg
valid_choices = ['+', '-', '/', '*', e]

# variabel der vi har lest inn brukerens valg
user_choice = 'x'

# Nå kan vi teste om innholdet i user_choice er det samme som en av elementene i valid_choices slik:

if (user_choice in valid_choices):
    # Gyldig!
else:
    # Ugyldig!
```

Deretter lager vi en "main loop", altså en løkke for selve programmet, - som kjører meny-funksjonen på nytt og på nytt helt til brukeren velger å avslutte. Foreløpig skriver vi bare ut hva brukeren valgte for å teste menyfunksjonaliteten, den faktiske utregningen kommer senere.

#### Relevante avsnitt i hjelpeteksten
- [Funksjoner](https://github.com/orsnes-privatskole/orsnes-privatskole.github.io#funksjoner)
- [Løkker](https://github.com/orsnes-privatskole/orsnes-privatskole.github.io#l%C3%B8kker)
- [Lister](https://github.com/orsnes-privatskole/orsnes-privatskole.github.io#lister) (kan f.eks. brukes for å lagre hva som er gyldige menyvalg)

<details>
<summary>Løsningsforslag - Kalulator Deluxe - Del A</summary>

```python
import time

# Calculator - Deluxe Edition
# Name and version info
version_info = "MyCalculator - Deluxe Edition v0.3"


# Function for getting menu choice
def get_menu_choice():
    # Variable used to align the menu to a common width
    menu_width = 30

    # List of available menu options
    valid_menu_choice = ['+', '-', '*', '/', 'e']

    # Loop until valid choice is made. If illegal input, ask the user again
    while True:
        print('\n')
        print('*' * menu_width)
        print("Welcome to " + version_info)
        print('*' * menu_width)
        print("Choose type of calculation or exit")
        print('*' * menu_width)
        print("* Addition:       +")
        print("* Subtraction:    -")
        print("* Multiplication: *")
        print("* Division:       /")
        print("* Exit:           e")
        print('*' * menu_width)
        choice = input("Please choose your option: ")

        # If the user input is valid, exit the loop by returning from the function with the user choice
        if choice in valid_menu_choice:
            return choice

        # If the user did not input a valid choice, inform about valid options, and ask again
        else:
            print(f"\n\t** Illegal menu option, please use one of {valid_menu_choice}")
            time.sleep(1)


# Variable for storing the user menu choice
menu_choice = get_menu_choice()

# Loop the whole program until the user choice is 'e' (exit)
while menu_choice != 'e':    
    print(f"Your choice was {menu_choice}")
    menu_choice = get_menu_choice()


# The loop is finished and we exit the program
print(f"\nThank you for using {version_info}")
print("Goodbye")

```

</details>

### Del B - Les inn tall til regnestykket
En svakhet med løsningen på *Basic* kalkulatoren var at vi ikke håndterte det hvis brukeren tastet noe som ikke var et tall. Vi brukte funsjonen ``int()`` til å gjøre om fra tekst til tall, - og det fungerer fint så lenge brukeren kun taster inn tall. Om brukeren taster inn bokstaver eller andre tegn, så vil programmet krasje...

I denne versjonen skal vi gjøre noe med det.

Lag en ny funksjon som ber brukeren skrive inn et tall, og som sjekker om det er et tall før den returnerer tallet.

#### Tips
Den innebygde Python funksjonen ``isdigit()`` er nyttig her. Den kan f.eks brukes slik:

```python
# Variabel med det brukeren har tastet inn
input_number = input("Please input number")

if input_number.isdigit():
    # It is a number!
else
    # This is not a number!
```

Bruk den nye funskjonen til å lese inn to tall etter at brukeren har gjort sitt menyvalg, og skriv dem ut på skjermen. I neste del bygger vi den faktiske fonksjonaliteten for å regne på tallene.

#### Relevante avsnitt i hjelpeteksten
- [Gjør om input til tall](https://github.com/orsnes-privatskole/orsnes-privatskole.github.io#gj%C3%B8r-om-input-til-tall)

<details>
<summary>Løsningsforslag - Kalkulator Deluxe - Del B</summary>

```python
import time

# Calculator - Deluxe Edition
# Name and version info
version_info = "MyCalculator - Deluxe Edition v0.7"


# Function for getting menu choice
def get_menu_choice():
    # Variable used to align the menu to a common width
    menu_width = 30

    # List of available menu options
    valid_menu_choice = ['+', '-', '*', '/', 'e']

    # Loop until valid choice is made. If illegal input, ask the user again
    while True:
        print('\n')
        print('*' * menu_width)
        print("Welcome to " + version_info)
        print('*' * menu_width)
        print("Choose type of calculation or exit")
        print('*' * menu_width)
        print("* Addition:       +")
        print("* Subtraction:    -")
        print("* Multiplication: *")
        print("* Division:       /")
        print("* Exit:           e")
        print('*' * menu_width)
        choice = input("Please choose your option: ")

        # If the user input is valid, exit the loop by returning from the function with the user choice
        if choice in valid_menu_choice:
            return choice

        # If the user did not input a valid choice, inform about valid options, and ask again
        else:
            print(f"\n\t** Illegal menu option, please use one of {valid_menu_choice}")
            time.sleep(1)


# Function for reading in a number, and ensuring that the input is valid
def read_input_number():
    while True:
        input_number = input("Please input number: ")
        if input_number.isdigit():
            return int(input_number)
        else:
            print(f"\n\t** {input_number} is not valid, try again")
            time.sleep(1)


# Variable for storing the user menu choice
menu_choice = get_menu_choice()

# Loop the whole program until the user choice is 'e' (exit)
while menu_choice != 'e':    
    print(f"Your choice was {menu_choice}")
    
    # Get the two numbers from the user
    number_a = read_input_number()
    number_b = read_input_number()
    print(f"You did input the numbers {number_a} and {number_b}")

    menu_choice = get_menu_choice


# The loop is finished and we exit the program
print(f"\nThank you for using {version_info}")
print("Goodbye")

```

</details>

### Del C - Lag regneoperasjonene

Vi har nå strukturen i programmet på plass, brukeren kan se valg, velge, lese inn tall og avslutte. Siste bit er å lage funksjoner for de regneoperasjoene vi tilbyr i menyen, og bruke disse basert på hva brukeren velger.

Eksempel:
```python
def addition(a, b):
    return a + b
```

I tillegg kan vi lage en funskjon som tar tre parametre:
1. Tall A
1. Tall B
1. Regneoperasjon

I denne funskjonen må vi kalle en av regneoperasjon funksjonene basert på hvilken regneoperasjon som er valgt.

Eksempel:
```python
def calculate(a, b, operator):
    if operator == '+':
        return addition(a, b)
    elif operator == '-':
```

Når regneoperasjon er utført, så skriver vi ut resultatet.

#### Relevante avsnitt i hjelpeteksten
- [Beregninger og operatorer](https://github.com/orsnes-privatskole/orsnes-privatskole.github.io#beregninger-og-operatorer)
- [Logiske tester](https://github.com/orsnes-privatskole/orsnes-privatskole.github.io#logiske-tester)
- [Skrive ut med flere variable](https://github.com/orsnes-privatskole/orsnes-privatskole.github.io#skriv-ut-med-flere-variable)

<details>
<summary></summary>

```python
import time

# Calculator - Deluxe Edition
# Name and version info
version_info = "MyCalculator - Deluxe Edition v0.3"


# Function for getting menu choice
def get_menu_choice():
    # Variable used to align the menu to a common width
    menu_width = 30

    # List of available menu options
    valid_menu_choice = ['+', '-', '*', '/', 'e']

    # Loop until valid choice is made. If illegal input, ask the user again
    while True:
        print('\n')
        print('*' * menu_width)
        print("Welcome to " + version_info)
        print('*' * menu_width)
        print("Choose type of calculation or exit")
        print('*' * menu_width)
        print("* Addition:       +")
        print("* Subtraction:    -")
        print("* Multiplication: *")
        print("* Division:       /")
        print("* Exit:           e")
        print('*' * menu_width)
        choice = input("Please choose your option: ")

        # If the user input is valid, exit the loop by returning from the function with the user choice
        if choice in valid_menu_choice:
            return choice

        # If the user did not input a valid choice, inform about valid options, and ask again
        else:
            print(f"\n\t** Illegal menu option, please use one of {valid_menu_choice}")
            time.sleep(1)


# Function for reading in a number, and ensuring that the input is valid
def read_input_number():
    while True:
        input_number = input("Please input number: ")
        if input_number.isdigit():
            return int(input_number)
        else:
            print(f"\n\t** {input_number} is not valid, try again")
            time.sleep(1)


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def calculate(a, b, operator):
    if operator == '+':
        return addition(a, b)
    elif operator == '-':
        return subtraction(a, b)
    elif operator == '*':
        return multiplication(a, b)
    elif operator == '/':
        return division(a, b)


# Variable for storing the user menu choice
menu_choice = get_menu_choice()

# Loop the whole program until the user choice is 'e' (exit)
while menu_choice != 'e':
    # Get the two numbers from the user
    number_a = read_input_number()
    number_b = read_input_number()

    # Calculate based on chosen operator and input numbers
    result = calculate(number_a, number_b, menu_choice)

    # Print results of calculation
    print(f"\n** Calculation {number_a} {menu_choice} {number_b} = {result}\n")
    time.sleep(1)

    menu_choice = get_menu_choice()


# The loop is finished and we exit the program
print(f"\nThank you for using {version_info}")
print("Goodbye")

```

</details>

[<< Tilbake til oppgaver](https://github.com/orsnes-privatskole/python-oppgaver)