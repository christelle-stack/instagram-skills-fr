# Checklist d'audit avant publication (Instagram)

Les seuils que la passe `--mode audit` applique. Miroir de la checklist du
fichier racine `../../../references/algorithm-heuristics.md`, avec les distinctions de
bloquants propres à l'humaniseur. V3 (2026-09) : les tics d'IA sont scorés par
densité par paragraphe ; le rythme forcé est un tic. Règle française : zéro
tiret long, zéro tiret moyen entre deux propositions.

## Bloquants (échec automatique)

- [ ] Aucun tiret long (U+2014), nulle part dans la légende ni sur une slide.
      Aucun tiret moyen (U+2013) entre deux propositions, aucun double tiret
      (`--`). Le trait d'union des mots composés est normal.
- [ ] Les 125 premiers caractères tiennent seuls comme hook (le pli « plus » coupe le reste).
- [ ] Légende dans la limite des 2 200 caractères.
- [ ] 3 à 5 hashtags calibrés, pas 20 à 30, jamais au milieu d'une phrase.
- [ ] Aucun appât à engagement (« commente OUI », « tague 3 amies », « double tap si »).
- [ ] Aucune ouverture « Dans un monde où » ou équivalent ; aucune ouverture
      en pont de révélation (« Voilà le truc : », « Parlons de… », « Arrête de
      X, commence à Y ») ; aucune ouverture en annonce de candeur
      (« franchement », « on ne va pas se mentir », « POV : » sur quelque chose
      qui n'est pas un point de vue).
- [ ] Aucune clôture morte « Et toi, qu'en penses-tu ? » / « Ton avis ? » /
      « Laisse ça infuser. » (une invitation à enregistrer ou à envoyer avec
      une raison est bienvenue, et même voulue).
- [ ] Aucun paragraphe avec 3 marqueurs de vocabulaire ou de grammaire ou
      plus (un marqueur par paragraphe, ça va) ; aucun parallélisme négatif
      « Ce n'est pas X, c'est Y » ; aucun pont de révélation « Le résultat ? ».
- [ ] Carrousel : toutes des images ou toutes des vidéos (pas de mélange), 2 à 10 slides.
- [ ] Un visuel est prévu (Instagram refuse les posts sans image ni vidéo).

## Avertissements (signaler avec une correction)

- [ ] Le jeu de hashtags est calibré (2 à 3 niche, 1 à 2 intermédiaires, 0 à 1 large), pas tout en large.
- [ ] 0 à 3 emojis, placés avec intention, aucun saupoudré ; aucune suite
      signature fusée/étincelles/feu.
- [ ] Aucun paragraphe ne sonne plat comme une machine (4 phrases ou plus
      toutes de la même longueur, aucune proposition qui travaille). Signaler
      ce paragraphe seulement ; ne jamais suggérer d'ajouter de la variance
      comme tactique. La mise en page à une idée par ligne, ça va.
- [ ] Aucune rafale de fragments (« Court. Percutant. Fini. », « Pas de X. Pas
      de Y. Juste Z. »), aucune ligne d'un mot pour le drame, au plus 2
      fragments isolés dans la légende, aucune balançoire long/court/long/court.
- [ ] Au moins un chiffre à précision bizarre AVEC un référent nommé là où
      l'affirmation le permet (un chiffre nu ne valide pas ce point).
- [ ] Au moins une entité nommée.
- [ ] Au plus une règle de trois naturelle ; aucune triade empilée ou
      parfaitement parallèle, aucune triade creuse sans éléments concrets,
      jamais 3 ou plus dans une légende.
- [ ] Aucune pile d'atténuations (« peut-être », « il me semble », « je me
      trompe peut-être mais ») et aucune confession cadrée (« franchement, ça a
      fait mal : … »). Un fait daté énoncé à plat, ça va.
- [ ] Seulement quand on audite une réécriture de l'humaniseur avec
      l'original sous la main, pas un brouillon frais : pas de surcorrection,
      c'est-à-dire que le ton de l'autrice, ses réactions, son registre
      minuscule, sa triade naturelle et ses emojis voulus ont survécu.
- [ ] La slide 1 du carrousel promet + ouvre une boucle, pas un titre nu.
- [ ] Le point le plus fort du carrousel est en avant (slide 2 ou 3), pas enterré en dernier.
- [ ] Un seul objectif principal clair (enregistrements / partages / commentaires / abonnements).
- [ ] Un seul CTA, pas trois ; il nomme une raison.

## Seuils en un coup d'œil

| Mesure | Limite |
|---|---|
| Légende | 2 200 caractères (hook dans les ~125 premiers) |
| Hashtags | 3 à 5 calibrés (30 est le plafond technique, mais ça sent le spam) |
| Emojis par légende | 0 à 3 |
| Tirets longs et tirets moyens entre propositions | 0 (légende comme slide) |
| Marqueurs de vocabulaire / grammaire par paragraphe | 0 à 2 |
| Fragments isolés | 2 par légende |
| Slides de carrousel | 2 à 10 |
| Durée d'un reel | jusqu'à 3 min ; 5 à 90 s pour l'onglet Reels |
| Ratio d'image | de 4:5 à 1.91:1 |

## Notation

- Un bloquant, n'importe lequel : **REFUSÉ**, renvoyer les corrections,
  proposer la réécriture automatique via `ig-humanizer`.
- Aucun bloquant, des avertissements : **VALIDÉ avec avertissements**, lister
  chacun avec une correction.
- Rien à signaler : **VALIDÉ**, ajouter la note de créneau de publication, la
  vérification de support, le rappel du visuel, et livrer le texte dans un
  bloc à copier-coller pour l'app Instagram.
- Rapporter la densité de tics par paragraphe (marqueurs, tirets, fragments,
  triades). Ne pas estimer un score de détecteur : sur un texte de la taille
  d'une légende c'est du bruit, et cette skill ne promet pas de les battre.
