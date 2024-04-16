# Ohjelmistotekniikka, harjoitustyö

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

2. Sovelluksen käynnistys komennolla:

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
