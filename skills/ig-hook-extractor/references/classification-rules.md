# Règles de classification des hooks (Instagram)

L'extraction des indices et les heuristiques de notation que `ig-hook-extractor`
utilise pour rattacher un post à l'une des 10 formules de
`../../../references/hook-formulas.md`.

## Étape 1 : détecter la surface

| Signal | Surface |
|---|---|
| Une photo + une légende | image seule (regarde IG1 à IG4) |
| 2 à 10 images empilées, points de swipe | carrousel (regarde IG5 à IG8) |
| Vidéo, verticale, avec du son | reel (regarde IG9 et IG10) |

L'URL aide : `/reel/` est un reel ; `/p/` est une image seule ou un carrousel
(l'icône ou les points dans l'app les distinguent, donc demande à
l'utilisatrice).

## Étape 2 : extraire les indices du hook

### Hooks de légende (environ 125 premiers caractères)

| Indice dans la première ligne | Formule |
|---|---|
| Un chiffre à la précision bizarre + une promesse « pique-la / voilà comment » | IG1 Résultat chiffré d'abord |
| Une affirmation posée à plat qui contredit le conseil courant | IG2 Vérité à contre-courant |
| Un moment précis que tout le monde connaît, sans préambule, sans chiffre | IG3 Scène du quotidien |
| Un repère temporel à la première personne + un coût ou une surprise avoués | IG4 Confession en mini-récit |

### Hooks de carrousel (slide 1 + structure)

| Indice | Formule |
|---|---|
| La slide 1 promet N éléments numérotés ; le corps en donne un par slide | IG5 Carrousel liste |
| La slide 1 montre un « après » ; la slide 2 l'« avant » ; le corps, des étapes | IG6 Transformation avant/après |
| Les slides du corps associent « Mythe : » et « Vérité : » | IG7 Carrousel casse-mythes |
| La slide 1 nomme une méthode ; la dernière la résume en une slide | IG8 Méthode à piquer |

### Hooks de reel (1 à 3 premières secondes)

| Indice | Formule |
|---|---|
| Une rupture de pattern / un texte à l'écran qui ouvre une boucle, pas d'intro lente | IG9 Reel rupture de pattern |
| « Comment j'ai {résultat} en {durée} » + étapes étiquetées | IG10 Reel « comment j'ai fait » |

## Étape 3 : noter la confiance

- **Haute (0,8 et plus) :** le hook colle proprement au squelette d'une formule
  et le corps suit sa structure.
- **Moyenne (0,5 à 0,8) :** le hook colle mais le corps est lâche, ou deux
  formules se chevauchent (fréquent : IG1 et IG10 utilisent toutes deux un
  résultat + des étapes). Renvoie les 2 premières.
- **Basse (moins de 0,5) :** aucune correspondance nette. Décris la structure
  littéralement et propose la formule la plus proche comme point de départ.

Quand deux collent, ce qui départage, c'est **l'objectif principal** (ci-dessous)
et la surface : un résultat en légende seule est IG1, le même résultat en reel
avec des étapes est IG10.

## Étape 4 : nommer l'objectif principal

Déduis ce pour quoi l'original était optimisé à partir de sa structure et de sa
clôture :

| Clôture / structure | Objectif probable |
|---|---|
| « enregistre ça », une liste, une méthode, un tuto | enregistrements |
| « envoie ça à… », une récompense à contre-courant ou un mythe cassé | partages |
| un moment du quotidien, une question, une confession | commentaires |
| une preuve de transformation, « abonne-toi pour… » | abonnements |

## Étape 5 : construire le gabarit vierge

Copie le squelette de la formule retenue depuis
`../../../references/hook-formulas.md`, garde sa structure d'emplacements et
renomme-les pour le sujet de l'utilisatrice. Retire tout signe d'IA que
l'original avait (ne propage pas une grappe de vocabulaire IA, un tiret long ou
un bloc de 30 hashtags dans le gabarit).

## Étape 6 : auditer la source

Signale, pour que l'utilisatrice ne les recopie pas :
- tout tiret long ou tiret moyen entre deux propositions
- une grappe de vocabulaire IA (3 marqueurs ou plus dans un paragraphe : « plonger dans », « booster », « incontournable », « véritable »)
- 20 à 30 hashtags entassés en haut
- du bait d'engagement (« commente OUI », « tague 3 copines »)
- un hook qui n'a de sens qu'après le pli « plus »
