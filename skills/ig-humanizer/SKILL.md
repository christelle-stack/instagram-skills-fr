---
name: ig-humanizer
description: "Enlève ce qui sonne IA dans une légende ou une slide de carrousel Instagram : vocabulaire IA scoré par densité, ponts de révélation, rafales de fragments, triades empilées, candeur annoncée, pluies d'emojis ; zéro tiret long. Inclut --mode audit (hook dans les 125 premiers caractères, longueur, hashtags, emojis, CTA, visuel prévu) et --mode profile. Ne sert pas à tromper les détecteurs d'IA (aucune réécriture ne le fait de façon fiable). Ne sert pas à écrire de zéro (utilise ig-caption-writer ou ig-carousel-planner). Déclencheurs : enlève ce qui sonne IA dans cette légende, humanise ce texte, vérifie ce post avant que je publie, ça sonne robot, audit avant publication."
---

# Humaniseur Instagram V3

Réécrit n'importe quelle légende ou texte de slide de carrousel pour en retirer
les tics d'IA que les lectrices humaines repèrent, et audite une légende finie
contre la checklist Instagram 2026. Fondé sur la taxonomie « Signs of AI
writing » de Wikipédia, la littérature de stylométrie 2025-2026, notre propre
corpus de légendes Instagram (n = 284, prévalence seulement) et les schémas
propres à Instagram (le pli des 125 premiers caractères, le registre casual en
minuscules, les hashtags calibrés, la structure pensée pour les partages et
les enregistrements). **V3 (2026-09) :** recalibrée sur les données 2026. Le
vocabulaire est scoré par densité, le rythme forcé devient un tic au lieu d'un
remède, et un garde-fou anti-surcorrection a été ajouté. **Adaptation
française :** le tiret long est interdit, sans exception, dans les textes que
cette skill produit comme dans ceux qu'elle corrige.

**Ce que cette skill ne fait pas :** elle ne fait pas « passer » un texte sur
GPTZero, Pangram, Turnitin ou Originality. Ce sont des classifieurs entraînés
sur la signature stylistique de l'instruction tuning ; les réécritures façon
« écris comme une vraie personne » sont repérées dans 92 à 95 % des cas, et une
réécriture mécanique légère augmente la détectabilité. Sur un texte de la
taille d'une légende (moins de 300 mots), les scores des détecteurs sont du
bruit. La vraie valeur est ailleurs : les lectrices expertes citent le
vocabulaire (53 %) et la structure des phrases (36 %) comme ce qui trahit un
texte IA, et sur Instagram une légende qui sonne comme un compte de marque ne
gagne ni l'enregistrement ni le partage. Cette skill retire ce à quoi ces
lectrices réagissent.

## Ce qui a changé en V3

Niveau de preuve entre crochets : [fort] = répliqué dans au moins deux études
indépendantes 2025-2026 ou dans notre propre corpus ; [éditeur] = jeu de
données d'une seule plateforme ou d'un seul fournisseur ; [faible] = une seule
étude ou un rapport de panel d'expertes.

- **Le vocabulaire est passé d'une liste à supprimer à un score de densité.**
  Les mots de 2023-24 (« plonger dans », « tapisserie », « voyage », « au cœur
  de ») s'effacent parce que les humaines les évitent désormais [fort]. Les
  marqueurs durables de 2026 sont des mots courants (significatif, crucial,
  notamment, complet, insights, robuste, exploiter, favoriser, paysage, nuancé,
  optimiser, sublimer) plus de la grammaire : nominalisations et phrases qui
  s'ouvrent sur un participe présent, à 5,3 fois le taux humain [fort]. Le
  vocabulaire IA apparaît dans 10 % des légendes humaines de notre corpus
  [fort], donc un marqueur dans un paragraphe n'est pas un verdict. Trois, oui.
- **Le tiret long : règle française, zéro.** Les données 2026 montrent que le
  caractère seul n'est plus un signal statistique (GPT-5.4 en émet 1,43 pour
  1 000 mots, sous la base humaine de 3,23) [fort]. Ce bundle tranche quand
  même pour une règle simple et stricte, parce qu'en français écrit pour
  Instagram le tiret long entre deux propositions reste le réflexe le plus
  visible des textes générés : zéro tiret long, zéro tiret moyen entre deux
  propositions, zéro double tiret. On remplace chaque occurrence par une
  virgule, deux-points, des parenthèses ou un retour à la ligne. Jamais par un
  point (un tiret coupé en deux empile des fragments). Le trait d'union des
  mots composés (porte-clés, c'est-à-dire) reste normal.
- **Le rythme forcé est le tic numéro 1 de 2026, pas le remède.** L'alternance
  mécanique long/court est une empreinte d'humaniseur apprenable [faible], et
  « Court. Percutant. Fini. », « Pas de X. Pas de Y. Juste Z. », les lignes
  d'un seul mot pour le drame et les révélations « Le résultat ? » sont les
  tics les plus cités par les lectrices en ce moment [fort]. Les légendes sont
  de longueur moyenne, donc la passe 2 n'est qu'un garde-fou anti-uniformité :
  on corrige un paragraphe qui sonne plat comme une machine, on ne fabrique
  jamais de variance.
- **La règle de trois reste un tic, à partir d'une certaine densité.** Le
  tricolon tourne à 2 fois le taux des expertes humaines sur les modèles 2026
  [fort], et 23 % des légendes humaines en contiennent un [fort : corpus].
  Donc une triade naturelle avec des éléments concrets reste. Les triades
  empilées, parfaitement parallèles ou creuses, et toute troisième triade dans
  une légende, sont nettoyées.
- **L'injection d'empreintes humaines était à moitié fausse.** Les noms
  propres et la concrétude sont confirmés [fort] ; un chiffre à précision
  bizarre avec un référent dans les 125 premiers caractères est le hook le plus
  fort. Un chiffre nu ne discrimine rien, et les hésitations et confessions
  insérées se retournent contre le texte : l'hésitation jouée est 2 fois plus
  fréquente dans les textes de LLM, et les annonces de candeur (« franchement »,
  « pour être honnête », « POV : » sur quelque chose qui n'est pas un point de
  vue) sont un tic nommé de 2026 [fort]. La passe 3 demande à la place un fait
  plat, daté, inconfortable.
- **Garde-fou anti-surcorrection.** La sortie d'un humaniseur a sa propre
  empreinte [faible]. La passe 4 vérifie si les passes 1 à 3 ont introduit les
  schémas qu'elles devaient retirer. Les retouches sont proportionnelles aux
  vrais problèmes. Dans le doute, on laisse.

## Quand l'utiliser

- Avant de publier toute légende ou tout carrousel rédigé par une IA (mode réécriture)
- Relecture avant publication d'une légende finie (mode audit, voir `sub-skills/post-audit.md`)
- Quand une légende sonne faux sans que tu arrives à dire pourquoi

## Entrée

N'importe quel texte : une légende, le texte incrusté d'un carrousel, ou la
légende d'un reel. En option : des échantillons de la voix cible (les anciennes
légendes de l'utilisatrice).

## Sortie

- Le texte réécrit, tics d'IA retirés
- Un diff qui montre ce qui a changé et pourquoi
- Le nombre de caractères de la légende (avec alerte si le hook déborde des 125 premiers caractères)
- La densité de tics par paragraphe (marqueurs par paragraphe ; 3 ou plus ont déclenché une réécriture)
- Une estimation de lecture humaine : « sonne humain », « mitigé », « sonne IA » (une estimation de ce qu'une lectrice perçoit, pas un score de détecteur)

## Modes

```bash
# Par défaut : nettoyer les tics d'IA (forensique + strict) et corriger les problèmes de format Instagram
ig-humanizer <texte>

# Forensique seul : toucher au minimum, retirer uniquement les fuites de modèle
ig-humanizer --mode forensic <texte>

# Audit : relecture détection seule, verdict validé/refusé, sans réécriture
# Déroule la checklist Instagram 2026 : hook dans les 125 premiers caractères, longueur
# de la légende, hashtags calibrés, limite d'emojis, qualité du CTA, rappel du visuel.
# Renvoie Bloquants + Avertissements + corrections proposées. Voir sub-skills/post-audit.md.
ig-humanizer --mode audit <texte>

# Profil : construire ou mettre à jour le Profil de voix et de marque de l'utilisatrice. Voir plus bas.
ig-humanizer --mode profile
```

## Les quatre passes

### Passe 1 : NETTOYER (scorer, puis supprimer ou remplacer)

Applique les catalogues par niveau de `references/scrub-rules.md`. L'unité de
jugement est le **paragraphe (ou la slide), pas le mot** : on compte les
marqueurs par paragraphe, on réécrit le paragraphe à partir de 3, on laisse un
marqueur isolé tranquille sauf s'il s'agit d'un pont de révélation, d'un
parallélisme négatif, d'un marqueur de candeur ou d'une fuite forensique.

- **Forensique** (toujours actif) : les vraies fuites de modèle qu'aucune
  humaine ne tape. Marqueurs d'outils IA (oaicite, contentReference,
  turn0search0), avertissements de date de connaissance (« À la date de ma
  dernière mise à jour »), blancs de gabarit ([Ton prénom]), et tout tiret
  long ou tiret moyen entre deux propositions.
- **Strict** (actif par défaut) : ce à quoi les lectrices réagissent. Le jeu
  de vocabulaire durable de 2026 scoré par densité (significatif, crucial,
  notamment, particulièrement, complet, insights, robuste, exploiter,
  favoriser, paysage, nuancé, optimiser, sublimer, booster, incontournable,
  véritable), les marqueurs grammaticaux (nominalisations, phrases ouvertes
  sur un participe présent), la couche d'idiomes de modèle 2026
  (« discrètement », « X, ça compte. », « l'effet cumulé », « un signal »,
  « le vrai travail », « construite différemment », « laisse ça infuser »), les
  ponts de révélation sur une seule occurrence (« Le résultat ? », « Voilà ce
  qui », « Arrête de X, commence à Y », « plot twist : », « Spoiler : »),
  toutes les formes de parallélisme négatif, les triades empilées ou
  parfaitement parallèles et toute troisième triade dans une légende, les
  nettoyages de formules (« dans un monde où », « à l'ère de », « game-changer »,
  « révolutionner », « plonger dans »), les pluies d'emojis, et les clôtures
  mortes (« et toi, qu'en penses-tu ? », « double tap si tu es d'accord »).
- **Nettoyages de format Instagram** (toujours appliqués) : un hook qui tient
  seul dans les 125 premiers caractères, des hashtags calibrés, la limite
  d'emojis, la promesse de la slide 1 du carrousel, la longueur de la légende.

### Passe 2 : RYTHME (garde-fou anti-uniformité seulement)

Les détecteurs ne scorent pas la burstiness, et les légendes sont de longueur
moyenne (la médiane de notre corpus est bien sous 200 mots), donc le rythme
n'est ni un levier de portée ni un remède. Ce que les lectrices remarquent,
c'est le tic d'uniformité mécanique (chaque ligne de la même longueur, plate
comme une machine) et, pire, la variance mise en scène qu'ajoutent les
humaniseurs de deuxième génération. La passe 2 a donc deux boulots : corriger
le rythme seulement là où il sonne plat, et retirer la variance fabriquée
partout. Elle n'ajoute jamais de variance comme tactique.

- Par paragraphe : une phrase vraiment longue à côté d'une courte, c'est bien,
  et c'est à ça que ressemble la variance humaine. Deux ou trois phrases de
  longueur moyenne à la suite, c'est bien aussi. On retouche seulement quand
  chaque phrase du paragraphe fait la même longueur et sonne plat, et alors on
  retouche une phrase, pas le paragraphe.
- Fragments isolés : au plus 2 par légende, au total. « à chaque fois. » une
  fois, c'est une manie de voix. Trois dans une légende, c'est un schéma.
- Interdits d'office (réécrire en phrases complètes) : les révélations « Le
  X ? Y. » ; « Pas de X. Pas de Y. Juste Z. » ; « Tous les X. Aucun des Y. » ;
  les empilements d'adjectifs « Simple. Efficace. Facile. » ; les lignes d'un
  mot pour le drame (« Voilà. » « Exactement. ») ; les pseudo-questions
  socratiques (« Pourquoi ? Parce que… ») ; les rafales « Court. Percutant.
  Fini. ». Ce sont les enchaînements de fragments qui trahissent.
- La mise en page n'est pas du rythme. Une idée par ligne avec des lignes
  vides entre elles, c'est la mise en forme native d'une légende, et ça reste.
  Le fragment-pour-le-drame à l'intérieur de ces lignes, c'est le tic. On
  garde la mise en page, on corrige les phrases.
- Le texte d'une slide de carrousel est court par conception ; on ne hache ni
  ne rembourre jamais une slide pour le rythme. On n'alterne jamais
  long/court/long/court entre slides ou entre lignes. Cette balançoire est
  l'empreinte de l'humaniseur.

La vérification est « est-ce qu'un paragraphe sonne plat comme une machine, et
est-ce que j'ai ajouté une rafale de fragments », pas un chiffre de variance.

### Passe 3 : AJOUTER (empreintes humaines)

À exiger quand le contenu le permet :
- Un chiffre à précision bizarre AVEC un référent nommé : qui, quoi, quand, ou
  ce que ça a coûté (« de 0 à 10k en 4 mois, en postant 3 fois par semaine »,
  pas « ça a grandi vite » et pas « 10k »). Un chiffre nu n'est pas une
  empreinte ; c'est le référent qui porte le signal.
- Une entité nommée (une vraie personne, une marque, une date, un outil)
- Un détail concret à la première personne (ce que tu as vu, ce que ça a coûté, ce qui a cassé)
- Un fait précis, daté, inconfortable, énoncé à plat, sans phrase de cadrage
  avant ni après. Pas « franchement, celle-là a fait mal : j'ai perdu la
  cliente. » Juste « j'ai perdu ma plus grosse cliente le 14 février. » Le
  fait porte la vulnérabilité. Le cadre la transforme en sincérité jouée, que
  les lectrices lisent maintenant comme le tic.
- Le registre casual en minuscules si la voix le demande

Interdits en ouverture ou en pivot (annonces de candeur, un tic nommé de
2026) : « franchement », « pour être honnête », « soyons honnêtes », « on ne
va pas se mentir », « je vais être cash », « la version honnête, c'est que »,
« en toute transparence », « sans mentir », « je peux être vulnérable deux
secondes ? », « avis impopulaire : » devant un avis en fait populaire,
« POV : » sur quelque chose qui n'est pas un point de vue. Interdits aussi en
insertion : les atténuations que l'autrice n'a pas écrites (« peut-être »,
« je me trompe peut-être mais », « il me semble »). L'hésitation jouée est 2
fois plus fréquente dans les textes de LLM que chez les expertes humaines ; en
ajouter rend le brouillon plus IA, pas moins.

Si l'entrée ne contient pas ces éléments, demande à l'utilisatrice un chiffre,
un nom ou un moment. N'invente rien.

### Passe 4 : AUTO-CONTRÔLE (garde-fou anti-surcorrection)

La sortie d'un humaniseur a sa propre empreinte. Avant de rendre le texte,
relis le résultat une fois et réponds à trois questions :

(a) Est-ce que la passe 2 a créé des rafales de fragments, des ponts « Le
    résultat ? », des lignes d'un mot, ou une balançoire long/court/long/court ?
    Si oui, refusionne les fragments en phrases complètes.
(b) Est-ce que la passe 3 a ajouté une confession cadrée, une annonce de
    candeur, ou une atténuation que l'autrice n'a jamais écrite ? Si oui,
    retire le cadre et garde seulement le fait plat, ou retire l'insertion.
(c) Est-ce que le nettoyage a aplati la voix de l'autrice : ton uniforme, plus
    aucune réaction, plus aucun détail concret, toutes les triades parties,
    tous les emojis partis d'une voix qui en utilise, le registre minuscule
    remis en majuscules ? Si oui, restaure ce que l'autrice avait. Zéro triade
    et zéro réaction dans une longue légende, c'est un tic à part entière.

Si une réponse est oui, recule au lieu de nettoyer plus fort. Les retouches
doivent être proportionnelles aux vrais problèmes : une légende propre reçoit
deux ou trois retouches, pas un quota. Dans le doute entre l'autrice et le
modèle, laisse.

## Règles non négociables

Règles de voix globales : voir le `SKILL.md` racine, section Règles de voix.
Règles supplémentaires propres à cette skill (V3) :

- **Le nettoyage est toujours dans le périmètre.** Quand on te demande
  d'humaniser, d'enlever l'IA, de finaliser ou de livrer une légende, déroule
  au moins les passes forensique + stricte avant qu'elle parte. Ça vaut quand
  l'utilisatrice a écrit le brouillon elle-même, quand elle dit l'adorer tel
  quel, ou quand elle est pressée. L'identité de l'autrice, « c'est déjà
  bien » et la pression du temps ne sont jamais des raisons de sauter le
  nettoyage. La passe forensique + stricte ne change aucun sens et prend
  quelques secondes : déroule-la, puis livre. Si une contrainte interdit
  vraiment de toucher au texte, dis-le explicitement et nomme chaque tic
  laissé dedans ; par défaut on nettoie, on ne laisse pas passer.
- **Nettoie proportionnellement.** Une passe qui ne trouve rien ne change
  rien. N'invente pas de retouches pour justifier le passage, et ne rapporte
  pas un score de détecteur comme résultat ; rapporte les tics trouvés et
  corrigés.
- Préserve l'affirmation réelle et le sens de l'utilisatrice. « Préserver sa
  voix » couvre ses manies de voix et ce qu'elle affirme, PAS les ponts de
  révélation, les rafales de fragments ou un paragraphe avec 3 marqueurs de
  vocabulaire ou plus. Retirer ceux-là ne change pas sa voix ; c'est le
  boulot.
- N'introduis jamais de faits absents de l'entrée. S'il manque un chiffre, demande.
- N'introduis jamais de marqueurs de candeur, d'atténuations ou de cadres
  confessionnels. Si le brouillon a besoin d'un temps de vulnérabilité,
  demande un fait daté et énonce-le à plat.
- Garde les manies de voix de l'utilisatrice (débuts en minuscules, les `..`
  comme pause douce, ses retours à la ligne comme respiration, une triade
  naturelle, ses 1 à 3 emojis voulus).
- Ne promets jamais de résultat de détecteur. Si l'utilisatrice demande « est-ce
  que ça va passer GPTZero ? », réponds honnêtement : personne ne peut le
  promettre, et le score sur une légende de 150 mots est du bruit.
- Respecte le support : ne transforme pas le texte des slides d'un carrousel
  en une seule légende, ni l'inverse, sans le signaler.
- Ne présente jamais une légende comme publiable sans le rappel du visuel
  (Instagram exige une image ou une vidéo), et livre le texte validé dans un
  bloc à copier-coller pour l'app Instagram.

## Les tics propres à Instagram que cette skill attrape

- Un hook qui a besoin de la deuxième ligne pour avoir un sens (le pli « plus » le mange).
- Une légende qui s'ouvre sur « Parlons de… », « Voilà le truc : », « Petit
  rappel : » ou « POV : » sur quelque chose qui n'est pas un point de vue.
- 20 à 30 hashtags entassés en haut au lieu d'un jeu calibré de 3 à 5.
- Des emojis saupoudrés sur chaque ligne (4 ou plus par légende).
- Un titre nu sur la slide 1 du carrousel au lieu d'une promesse + une boucle ouverte.
- Des règles de trois empilées ou creuses (« plus vite, moins cher, mieux ») ;
  une triade naturelle avec des éléments concrets reste.
- L'appât à engagement (« commente OUI », « tague 3 amies », « double tap si »).
- Les rafales de fragments et les lignes d'un mot pour le drame (l'empreinte de
  l'humaniseur), ou un paragraphe où chaque ligne sonne plat comme une machine.

## Exemple

Voir `references/examples.md` pour des réécritures avant/après commentées.

## Fichiers

- `SKILL.md` : ce fichier (nettoyeur en réécriture + entrée du mode audit)
- `references/scrub-rules.md` : motifs regex V3 par niveau, score de densité, règle du tiret long, règles de rythme, insertions interdites
- `references/examples.md` : réécritures avant/après commentées pour légendes et slides
- `references/audit-checklist.md` : la checklist avant publication avec ses seuils
- `sub-skills/post-audit.md` : le déroulé d'audit avant publication (détection seule, sans réécriture)
- `sub-skills/voice-profile.md` : construire ou mettre à jour le Profil de voix et de marque (`--mode profile`)
- `sub-skills/illustration.md` : brief visuel optionnel (prompt d'image, texte à incruster, format, palette)

## Mode profil de voix (`--mode profile`)

`ig-humanizer --mode profile` construit ou met à jour le Profil de voix et de
marque de l'utilisatrice dans `../../references/voice-profile.md` à partir de
3 à 6 de ses vrais posts Instagram collés dans la conversation (portable, sans
token) ou, si un token de lecture est configuré, à partir de son activité
récupérée. Une fois rempli, chaque skill d'écriture du bundle rédige
automatiquement dans sa voix. Voir `sub-skills/voice-profile.md`. Déclencheurs :
« construis mon profil de voix », « apprends ma voix », « apprends comment
j'écris ».

## Skills liées

- `ig-caption-writer` : génère des légendes qui passent déjà l'humaniseur
- `ig-carousel-planner` : génère des carrousels qui passent déjà l'humaniseur
