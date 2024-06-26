# Ohjelmistotekniikka, harjoitustyö

## Retro kokoelma sovellus

### Releaset

[Release viikko 5](https://github.com/LHuldin/ot-harjoitustyo24/releases/tag/viikko5)

[Release viikko 5.2](https://github.com/LHuldin/ot-harjoitustyo24/releases/tag/Viikko5.2)

[Release viikko 6](https://github.com/LHuldin/ot-harjoitustyo24/releases/tag/Viikko6)

[Loppupalautus](https://github.com/LHuldin/ot-harjoitustyo24/releases/tag/FinalRelease1.1)


### Dokumentaatio

[Vaatimusmäärittely](https://github.com/LHuldin/ot-harjoitustyo24/blob/main/sovellus/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/LHuldin/ot-harjoitustyo24/blob/main/sovellus/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/LHuldin/ot-harjoitustyo24/blob/main/sovellus/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/LHuldin/ot-harjoitustyo24/blob/main/sovellus/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/LHuldin/ot-harjoitustyo24/blob/main/sovellus/dokumentaatio/kayttoohje.md)

[Testausdokumentti](https://github.com/LHuldin/ot-harjoitustyo24/blob/main/sovellus/dokumentaatio/testaus.md)


### Asennus

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

### Testaus

Testien ajo onnistuu komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin saa generoitua komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Pylintin ajo onnistuu komennolla:

```bash
poetry run invoke lint
```
