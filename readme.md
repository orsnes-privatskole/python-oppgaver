# Lag spillet "Gjett riktig tall" i Python

Bruk Python til å lage et spill hvor maskinen velger et tilfeldig tall, og så skal spilleren gjette riktig tall på et gitt antall forsøk. Hvis spilleren gjetter feil, skal spillet fortelle om forslaget var for høyt eller lavt.

Oppgaven er delt i flere del-oppgaver som bygger videre på de første delene. Så første versjon blir helt enkel, og så bygger vi på med mer funksjoner etter hvert.

Hver del har et løsningsforslag, men vent med å se på det til du har *prøvd* selv først! Bruk oversikten på [https://orsnes-privatskole.github.io/](https://orsnes-privatskole.github.io/) for å se hvordan man gjør de forskjellige tingene som trengs for å løse hver deloppgave.

## Del A – Start spillet
- Be spilleren skrive inn navnet sitt, og lagre det i en variabel
- Skriv en velkomst-tekst som ønsker spilleren velkommen, med bruk av spillerens navn

### Relevante avsnitt fra hjelpeteksten:
- [Skrive ut tekst på skjerm](https://orsnes-privatskole.github.io/#skriv-ut-tekst-p%C3%A5-skjerm)
- [Les inn tekst / tall fra bruker](https://orsnes-privatskole.github.io/#les-inn-tekst--tall-fra-bruker)

<details>
<summary>Løsningsforslag A</summary>

```python
# The guess number game
# Made by: 
# Version A
import time

name = input("What is your name? ")
print(f"Hello {name}, lets play the game Guess number!")

time.sleep(1)
```

</details>

## Del B – Lag et tilfeldig tall
Her skal spillet "tenke på et tilfeldig tall". Vi må bestemme oss for hvor stort tallet maks kan være, jo større jo høyere vanskelighetsgrad vil det være på å gjette riktig. For første versjon velger vi at tallet skal være mellom 1 og 10.

Lagre det tilfeldige tallet i en variabel og skriv det ut på skjermen (bare for testing, vi kan selvsagt ikke skrive det ut når spilleren skal gjette det 🙂, men det kommer senere).

### Relevant avsnitt fra hjelpeteksten:
- [Tilfeldige tall](https://orsnes-privatskole.github.io/#tilfeldige-tall)

<details>
<summary>Løsningsforslag B</summary>

```python
# The guess number game
# Made by: 
# Version B
import time
import random

name = input("What is your name? ")
print(f"Hello {name}, lets play the game Guess number!")

time.sleep(1)

# Pick a random number between 1 and 10
secret_number = random.randint(1, 10)

print(f"The random number is {secret_number}")

```

</details>

## Del C – La spilleren gjette!
- Be spilleren gjette hvilket tall du tenker på
- Skriv ut om svaret er riktig, eller om det er feil skriver du hva tallet var

Her må vi bruke en logisk test for å sjekke om svaret er riktig. Siden vi skal sammenligne med et tilfeldig *tall*, så er det viktig å gjøre om innlest svar fra tekst til tall.

### Relevante avsnitt fra hjelpeteksten:
- [Logiske tester](https://orsnes-privatskole.github.io/#logiske-tester)
- [Gjør om input til tall](https://orsnes-privatskole.github.io/#gj%C3%B8r-om-input-til-tall)

<details>
<summary>Løsningsforslag C</summary>

```python
# The guess number game
# Made by: 
# Version C
import time
import random

name = input("What is your name? ")
print(f"Hello {name}, lets play the game Guess number!")

time.sleep(1)

# Pick a random number between 1 and 10
secret_number = random.randint(1, 10)

# Let the player guess
player_guess = int(input("I am thinking of a number between 1 and 10, can you guess which number? "))

# Check player answer
if player_guess == secret_number:
    print("WOW, you are good! The answer is correct.")
else:
    print(f"Sorry, that was wrong. The number was {secret_number}")

```

</details>

## Del D – La spilleren få flere forsøk
Å gjette riktig på første forsøk kan være litt vel flaks-basert, så vi må la spilleren prøve flere gang. Lag en løkke som lar spilleren gjette helt til riktig svar er gitt.

Vi vil også gi brukeren tilbakemelding på om svaret var for høyt eller lavt. Her kan vi bruke flere logiske tester, så om svaret ikke er nøyaktig riktig, så sjekker vi om det er *større* eller *mindre enn* riktig svar.

### Relevante avsnitt fra hjelpeteksten:
- [Løkker](https://orsnes-privatskole.github.io/#l%C3%B8kker)
- [Beregninger og operatorer](https://orsnes-privatskole.github.io/#beregninger-og-operatorer)
- [Logiske tester](https://orsnes-privatskole.github.io/#logiske-tester)

<details>
<summary>Løsningsforslag D</summary>

```python
# The guess number game
# Made by: 
# Version D
import time
import random

name = input("What is your name? ")
print(f"Hello {name}, lets play the game Guess number!")

time.sleep(1)

# Pick a random number between 1 and 10
secret_number = random.randint(1, 10)

# Let the player guess repeatedly until he or she gets it right
player_guess = 0
while not player_guess == secret_number:
    player_guess = int(input("I am thinking of a number between 1 and 10, can you guess which number? "))

    # Check player answer
    if player_guess == secret_number:
        print("WOW, you are good! The answer is correct.")
    else:
        if player_guess > secret_number:
            print("Sorry, that was wrong, your guess was too high!")
        else:
            print("Sorry, that was wrong, your guess was too low!")
        print("Please try again...\n\n")
        time.sleep(1)

```

</details>


## Del E – Vanskelighetsgrad
Det er særlig to ting som kan påvirke vanskelighetsgraden i dette spillet: Hvor mange tall det velges fra, og hvor mange forsøk spilleren får på å gjette.
La spilleren velge vanskelighetsgrad i starten av spillet, f.eks.:

1. Lett (tall fra 1 til 10, 10 forsøk)
2. Middels (tall fra 1 til 20, 5 forsøk)
3. Vanskelig (tall fra 1 til 30, 3 forsøk)

For hvert forsøk kan det skrives ut hvor mange forsøk som er brukt og hvor mange som er igjen.

Nå begynner koden å bli mer kompleks så det kan være fornuftig å bruke funksjoner. På den måten kan vi "gjenbruke" koden flere steder. Vi kan for eksempel lage følgende funksjoner:

- Skriv ut meny: ``print_menu()``
- Gjennomfør spill: ``play_game()``

For eksempel i funksjonen ``play_game()`` så kan vi gjennomføre spillet som i forrige versjon, men nå med ulike verdier på hva maks tall kan være og antall forsøk, basert på valgt vanskelighetsgrad.

### Relevante avsnitt fra hjelpeteksten:
- [Variabler](https://orsnes-privatskole.github.io/#variabler)
- [Funksjoner](https://orsnes-privatskole.github.io/#funksjoner)

<details>
<summary>Løsningsforslag E</summary>

```python
# The guess number game
# Made by: 
# Version E
import time
import random


def print_menu():
    menu_width = 37
    print(menu_width * "-")
    print("* Welcome to the guess number game *")
    print(menu_width * "-")
    print("* 1 - Easy")
    print("* 2 - Intermediate")
    print("* 3 - Hard")
    print(menu_width * "-")
    print("* 4 - Quit game")
    print(menu_width * "=")


max_retries = 5  # How many attempt the user gets to guess the correct number
max_number = 10  # What will be the largest number the user can guess (larger number means more difficult)


def play_game():
    secret_number = random.randint(1, max_number)
    number_of_guesses = 0
    while number_of_guesses < max_retries:
        player_guess = int(input(f"I am thinking of a number between 1 and {max_number}, can you guess which number? "))
        number_of_guesses += 1  # Count number of guesses

        # Check player answer
        if player_guess == secret_number:
            print(f"WOW, you are good! The answer is correct, you made it using {number_of_guesses} attempts!")
            return
        else:
            if player_guess > secret_number:
                print("Sorry, that was wrong, your guess was too high!")
            else:
                print("Sorry, that was wrong, your guess was too low!")

            guesses_left = max_retries - number_of_guesses

            if guesses_left > 0:
                print(f"Please try again... you have {guesses_left} more guesses\n\n")
            else:
                print(f"Sorry, you failed. No more guesses. The number was {secret_number}.")
                return

            time.sleep(1)


name = input("What is your name? ")
print(f"Hello {name}, lets play the game Guess number!\n")

time.sleep(1)

player_choice = 0

while not player_choice == 4:
    print_menu()

    # Ask player for which menu option they want
    player_choice = int(input("Please choose: "))

    if player_choice == 1:
        max_retries = 10
        max_number = 10
        print("OK, you chose the easy option")
        print(f"Easy: you will guess a number between 1 and {max_number}, with {max_retries} attempts.")
        play_game()

    elif player_choice == 2:
        max_retries = 5
        max_number = 20
        print("You chose the intermediate option, not bad")
        print(f"Intermediate: you will guess a number between 1 and {max_number}, with {max_retries} attempts.")
        play_game()

    elif player_choice == 3:
        max_retries = 3
        max_number = 30
        print("WOW, you chose the HARD option, well you have been warned!")
        print(f"Hard: you will guess a number between 1 and {max_number}, with {max_retries} attempts.")
        play_game()

    elif player_choice == 4:
        print(f"You want to quit? OK, it was nice playing with you {name}")

    else:
        print("That is not a valid option, please use 1, 2, 3 or 4\n\n")
```

</details>