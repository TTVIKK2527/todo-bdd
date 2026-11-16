# #334 Ülesannete nimekiri BDD ja TDD järgi

Kolm kasutuslugu: ülesande lisamine, tehtuks märkimine ja tegemata ülesannete
loetlemine. Igal kasutuslool on eraldi .feature fail Given/When/Then sammudega.
Step definition'id kutsuvad otse rakenduse avalikku API-t; domeeniloogikat ei mockita.

## Käivitamine

Vaja on ainult Python 3.10+ standardteeki. IDE-d ega pakettide paigaldust pole vaja.

```sh
python3 demo.py
./test.sh
python3 bdd_runner.py
```

src/todo.py sisaldab domeeni, tests/test_todo.py ühikteste, features/ kasutuslugude
stsenaariume ja steps.py seob tekstisammud avaliku API-ga. Andmed on mälus, nagu
ülesanne lubab. all() ja open_tasks() tagastavad koopiad; klient ei saa tagastatud
andmeid muutes rakenduse sees olevaid ülesandeid rikkuda.

## BDD tööriist

bdd_runner.py on teadlikult väike range Gherkini alamhulga käivitaja. Toetab
Feature, Scenario, Given, When, Then ja And märksõnu. Ei toeta Scenario Outline'i,
tag'e ega andmetabeleid; toetamata süntaks ja puuduvad sammud annavad vea.
See ei ole väide täielikust Cucumberi ühilduvusest. Väikese kolme kasutusloo jaoks
on kõik kasutatud sammud selgesõnaliselt defineeritud ja parser kontrollib, et
Given/When/Then on olemas ning õiges järjekorras.

## Tegelik TDD protsess

Kõigepealt loodi lisamise .feature ja pending step definition, mille käivitus
andis NotImplementedError vea. Seejärel kirjutati ebaõnnestuvad ühiktestid.
Iga järgmise kasutusloo puhul lisati uus .feature ja test enne teostust.

| Kasutuslugu | Red | Green | Refactor |
|---|---|---|---|
| Lisamine | 1fd76c9 | e565f70 | 6c92401 |
| Lõpetamine | aa1bdfc | cce255f | b421d65 |
| Tegemata loend | b0b9fb3 | 90d4192 | ef3e804 |

`git log --oneline --reverse` näitab tegelikku tööjärjekorda. Commit'ide autor on
Codex; ajalugu pole esitatud õppija iseseisva töö tõendina.

## Kontrollitud seis

16.11.2026: seitse ühiktesti ja kolm BDD stsenaariumi PASS. Veajuhud katavad tühja
pealkirja ja vigase ID; erijuht on tühi või täielikult lõpetatud nimekiri.
CI workflow käivitab nii BDD kui ühiktestid, kuid edukat GitHub Actionsi logi
ei ole enne tegelikku avaldamist/jooksu olemas. Individuaalne kaitsmine jääb alles.
Kaheminutilise demo jaoks käivita demo.py ja bdd_runner.py ning näita üht rohelist
stsenaariumi; seda ei pea pikaks esitluseks venitama.
