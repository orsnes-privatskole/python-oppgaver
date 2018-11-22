# Animasjon

Vi bygger videre på det vi lærte i [Tilfeldig kunst oppgaven](https://github.com/orsnes-privatskole/python-oppgaver/blob/master/random-art.md). Nå skal vi utvide med å lage bevegelige bilder (animasjon). Basisprinsippet for animasjon er at man tegner mange bilder i rask rekkefølge samtidig som vi endrer på noen parametre (f.eks. posisjon til et objekt) for hvert bilde. Dermed skaper vi inntrykk av at objektet beveger seg.

Koden vår begynner nå å bli mer kompleks, og vi vil derfor ta i bruk klasser og objekter som gjør det lettere å organisere koden. Det gjør det også mulig å basere oss på kode som allerede finnes. For eksempel i [Python Arcade](http://arcade.academy) så finnes det en *klasse* for å håndtere et *vindu* som har kontroll på tegning av grafikk som stadig oppdateres, samt håndtere bruker-input, f.eks at brukere trykker på en tast på tastaturet eller beveger muspekeren.

Dette kan vi dra nytte av ved å lage vår egen klasse som *arver* fra Python Arcade sin [arcade.application.Window](http://arcade.academy/arcade.html?#module-arcade.application). At den arver betyr at vi får med alt som finnes i den klassen fra før, og at vi i tilleg kan lage vår egen kode for hva som skal skje når en tast trykkes f.eks.

## Del A - Basiskode

Først lager vi en "basiskode" som gjør klart et lerret som tegnes på nytt og på nytt basert på ``Window`` klassen beskrevet ovenfor. I første omgang vil det bare være et "tomt skall" som vi fyller på funksjonalitet i etterhvert. For funksjoner som ikke er ferdig, så kan vi bruke Python kodeordet ``pass`` for å indikere at "her kommer det mer kode, ikke bry deg med det enda". For et mer komplett eksempel på bruk av ``Window`` klassen, se Python Arcade sin [Starting template](http://arcade.academy/examples/starting_template.html#starting-template)


Kopier koden nedenfor inn i en ny Python fil:

```python
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyWindow(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK_BEAN)

    def on_draw(self):
        arcade.start_render()

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass


def main():
    """ Main method """
    MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()

```

## Del B - Bevegelig objekt

![moving-object](gfx/animation-part-b.png)

Nå som vi har basiskoden på plass, vil vi lage et nytt objekt som skal bevege seg. Objektet skal holde rede på egen posisjon og fart, samt være istand til å "tegne seg selv".

Vi kalle klassen vår for ``Shape``, og legger følgende kode til på over ``MyWindow`` klassen:

```python
class Shape:
    
    def __init__(self, x, y):
        # Object position
        self.x = x
        self.y = y
        
        # Object velocity (speed) 
        self.vel_x = 5
        self.vel_y = 0
        
    def update(self):
        # Calculate new position based on velocity
        self.x += self.vel_x
        self.y += self.vel_y
        
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 50, arcade.color.LIGHT_CORAL)
        
```

For å ta i bruk denne klassen, så går vi til ``__init__()`` funksjonen i ``MyWindow`` klassen og oppretter en *instans* av ``Shape`` slik:

```python
# Create a shape object at 0 (left) x position, and centre of height
self.shape = Shape(0, SCREEN_HEIGHT // 2)
```

I tillegg må vi sørge for at det nye objektet blir oppdatert og tegnet for hver gang vinduet tegnes på nytt (frame). Det gjøres i ``MyWindow`` klassen slik:

```python
def on_draw(self):
    arcade.start_render()
    self.shape.draw()

def on_update(self, delta_time):
    self.shape.update()
```

Vi har nå et vindu som animerer en sirkel som beveger seg fra venstre mot høyre med 5 piksler (``vel_x``) for hver gang bildet tegnes på nytt.

- Hvor fort vil den bevege seg per sekund?
- Hvordan kan vi også bevege den i høyde-retningen (y-aksen)?
- Kan vi få den til å snu når "den møter veggen"?
- Hva med flere objekter?