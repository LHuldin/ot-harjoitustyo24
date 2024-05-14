# Käyttöohje



## Sovelluksen käynnistys

1. Riippuvuuksien asennus komennolla:

```bash
poetry install
```

2. Asenna sovelluksen SQLite tietokanta komennolla:

```bash
poetry run invoke build
```

3. Sovelluksen käynnistys komennolla:

```bash
poetry run invoke start
```


## Kirjautuminen ja rekisteröityminen
kirjautumisnäkymä josta pääsee reksteröitymään:

![](./kuvat/login.png)

rekisteröitymisnäkymä jossa voit luoda uuden käyttäjän antamalla vähintään 4 merkkiä pitkän käyttäjänimen ja salasanan:

![](./kuvat/register.png)

Rekisteröinnin jälkeen palaat vielä kirjautumis näkymään jossa voit kirjautua sisään

## Kirjasto ja tuotteiden lisäys ja poisto

Kirjasto näkymä jossa voit lisätä ja poistaa tuotteita.
Täällä myös näet listattuna laitteet pelit jotka ovat tietokannassa:
![](./kuvat/kirjasto.png)

Laitteen ja pelien lisäämisen mahdollistavat näkymät:
![](./kuvat/lisaalaite.png)
![](./kuvat/lisaapeli.png)

Ja viimeisenä näkymä jossa on ID numeron perusteella mahdollista poistaa tuote tietokannasta:

![](./kuvat/poistatuote.png)






