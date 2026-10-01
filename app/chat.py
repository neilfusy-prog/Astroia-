import os

BASE = os.path.join(
os.path.dirname(**file**),
"..",
"knowledge",
"astronomie.txt"
)

def charger_connaissances():
with open(BASE, "r", encoding="utf-8") as fichier:
return fichier.read()

def repondre(question):
connaissances = charger_connaissances()

```
question = question.lower()

mots_cles = [
    mot for mot in question.split()
    if len(mot) > 3
]

correspondances = []

for ligne in connaissances.splitlines():
    ligne_lower = ligne.lower()

    if any(mot in ligne_lower for mot in mots_cles):
        correspondances.append(ligne)

if correspondances:
    return "Voici ce que je trouve dans mes connaissances :\n\n" + \
           "\n".join(correspondances)

return (
    "Je ne trouve pas encore cette information dans "
    "ma base de connaissances."
)
```

if **name** == "**main**":
print("🔭 AstroIA est démarrée !")

```
while True:
    question = input("\nToi : ")

    if question.lower() in ["quit", "exit", "stop"]:
        break

    print("\nAstroIA :", repondre(question))
```
