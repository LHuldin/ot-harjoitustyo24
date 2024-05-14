# Ohjelmistotekniikka, harjoitustyö

## Retro kokoelma sovellus

### Releaset

[Release viikko 5](https://github.com/LHuldin/ot-harjoitustyo24/releases/tag/viikko5)

[Release viikko 5.2](https://github.com/LHuldin/ot-harjoitustyo24/releases/tag/Viikko5.2)

[Release viikko 6](https://github.com/LHuldin/ot-harjoitustyo24/releases/tag/Viikko6)

[Final Release](https://github.com/LHuldin/ot-harjoitustyo24/releases/tag/FinalRelease)


### Dokumentaatio

[vaatimusmäärittely](https://github.com/LHuldin/ot-harjoitustyo24/blob/main/sovellus/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito](https://github.com/LHuldin/ot-harjoitustyo24/blob/main/sovellus/dokumentaatio/tuntikirjanpito.md)

[changelog](https://github.com/LHuldin/ot-harjoitustyo24/blob/main/sovellus/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/LHuldin/ot-harjoitustyo24/blob/main/sovellus/dokumentaatio/arkkitehtuuri.md)


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
