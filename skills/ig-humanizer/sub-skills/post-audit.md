# Audit d'un post Instagram

Passe n'importe quelle légende (et le texte des slides de son carrousel) dans
la checklist de classement Instagram 2026. Attrape les tics d'IA, les
infractions de format (hook dans les 125 premiers caractères, longueur de la
légende, calibrage des hashtags, emojis), les freins à la portée (appât à
engagement, médias mélangés) et les faiblesses de structure avant publication.
C'est le déroulé de `ig-humanizer --mode audit` : détection seule, sans
réécriture.

## Quand l'utiliser

- Avant de publier une légende ou un carrousel écrit à la main ou rédigé par une IA
- Quand `ig-caption-writer` ou `ig-carousel-planner` termine un brouillon (appel automatique)
- Quand un post récent a sous-performé et que l'utilisatrice veut un post-mortem

## Entrée

- Une légende, et pour un carrousel le texte des slides
- En option : l'audience visée, l'heure de publication prévue, le support (image / carrousel / reel)

## Sortie

- Un en-tête **Validé / Refusé**
- **Bloquants** (à corriger avant de publier) : tiret long ou tiret moyen
  entre deux propositions, paragraphes à 3 marqueurs d'IA ou plus, ponts de
  révélation, annonce de candeur en ouverture, appât à engagement, hook qui
  déborde du pli, mur de hashtags
- **Avertissements** (risqué de publier tel quel) : rafales de fragments,
  marqueurs de candeur ou atténuations au milieu de la légende (en ouverture,
  c'est un bloquant), chiffres sans référent, CTA générique
- **Corrections proposées** pour chaque problème
- **Densité de tics par paragraphe** (marqueurs, tirets, fragments, triades).
  Pas de score de détecteur : sur un texte de la taille d'une légende c'est du
  bruit, et la skill ne promet pas de les battre
- **Recommandation de créneau** selon l'audience

## Vérifications

### Bloquants (échec automatique)

1. Un tiret long, n'importe où (légende ou slide) ; un tiret moyen entre deux
   propositions ; un double tiret. Le trait d'union des mots composés ne compte pas.
2. Le hook a besoin de la deuxième ligne pour avoir un sens (les 125 premiers
   caractères ne tiennent pas seuls).
3. Légende de plus de 2 200 caractères.
4. 20 à 30 hashtags, ou des hashtags au milieu d'une phrase.
5. Appât à engagement (« commente OUI », « tague 3 amies », « double tap si tu es d'accord »).
6. Ouverture sur « Dans un monde où » ou équivalent, sur un pont de
   révélation (« Voilà le truc : », « Parlons de… », « Arrête de X, commence
   à Y ») ou sur une annonce de candeur (« franchement », « on ne va pas se
   mentir », « POV : » sur quelque chose qui n'est pas un point de vue).
7. Fin sur « Et toi, qu'en penses-tu ? », « Ton avis ? » ou « Laisse ça
   infuser. » (une invitation à enregistrer ou à envoyer avec une raison, ça va).
8. Un paragraphe avec 3 marqueurs de vocabulaire ou de grammaire ou plus, ou
   un parallélisme négatif / pont de révélation « Le résultat ? » (voir
   `../references/scrub-rules.md`).
9. Le carrousel mélange images et vidéos, ou dépasse 10 slides.
10. Aucun visuel prévu (Instagram refuse les posts sans image ni vidéo).

### Avertissements (signaler avec une correction proposée)

11. Plus de 5 hashtags, ou un jeu tout en large dans lequel un petit compte ne peut pas se classer.
12. 4 emojis ou plus, des emojis saupoudrés sur chaque ligne, ou la suite
    signature fusée/étincelles/feu.
13. Un paragraphe qui sonne plat comme une machine (4 phrases ou plus toutes
    de la même longueur, aucune proposition qui travaille). Signaler ce
    paragraphe seulement ; ne jamais suggérer d'ajouter de la variance comme
    tactique. La mise en page à une idée par ligne, ça va.
13a. Rafales de fragments (« Court. Percutant. Fini. », « Pas de X. Pas de Y.
    Juste Z. »), lignes d'un mot pour le drame, plus de 2 fragments isolés, ou
    une balançoire long/court/long/court.
14. Aucun chiffre à précision bizarre avec un référent nommé là où
    l'affirmation en permettrait un (un chiffre nu ne valide pas ce point).
15. Aucune entité nommée (personne, marque, outil).
16. Règle de trois empilée ou parfaitement parallèle, triade creuse sans
    éléments concrets, ou 3 triades ou plus dans la légende (une triade
    naturelle passe).
16a. Pile d'atténuations (« peut-être », « il me semble ») ou marqueur de
    candeur / confession cadrée au milieu de la légende (« franchement, ça a
    fait mal : … ») ; le même marqueur en ouverture est le bloquant 6. Un fait
    daté énoncé à plat, ça va.
16b. Surcorrection (seulement quand on audite une réécriture de l'humaniseur
    avec l'original sous la main pour comparer ; un brouillon frais qui n'a
    jamais eu de triade n'est pas surcorrigé) : ton uniformément plat, toutes
    les triades parties d'une longue légende, les emojis ou le registre
    minuscule de l'autrice disparus, aucune réaction ni opinion nulle part.
17. La slide 1 du carrousel est un titre nu, pas une promesse + une boucle ouverte.
18. Le point le plus fort du carrousel est enterré sur la dernière slide de corps.
19. Aucun objectif principal clair : le brouillon court après les
    enregistrements, les partages, les commentaires et les abonnements en même
    temps. Choisis-en un (voir `../../../references/hook-formulas.md`,
    « Répartition par objectif d'engagement »).
20. Le CTA est générique, ou trois CTA se font concurrence.

### Infos (notes neutres)

21. Créneau de publication suggéré selon l'audience.
22. Support recommandé (image seule, carrousel ou reel) selon la matière.
23. Opportunité d'enregistrement ou d'envoi : si le brouillon est une liste,
    un cadre ou un tutoriel, noter qu'il doit être structuré pour maximiser
    les enregistrements ; si c'est une prise de position à contre-courant ou
    un mythe démonté, le structurer pour maximiser les envois.

## Étapes

1. Détecter le support : image seule, carrousel ou reel.
2. Mesurer la légende : nombre de caractères, là où les 125 premiers
   caractères coupent, nombre et calibrage des hashtags, nombre d'emojis,
   présence de tirets longs ou moyens.
3. Dérouler les vérifications bloquantes. Si l'une échoue, renvoyer
   **REFUSÉ** avec des corrections précises ; proposer en option de passer la
   main à `ig-humanizer` pour une réécriture automatique.
4. Sans bloquant, dérouler les avertissements.
5. Rapporter la densité de tics par paragraphe. Ne pas estimer un score de détecteur.
6. Renvoyer le rapport structuré avec une note de créneau et le rappel du
   visuel. Si le texte est validé, le livrer dans un bloc à copier-coller et
   rappeler d'ajouter l'image ou la vidéo dans l'app Instagram.

## Liés

- `ig-humanizer` : réécriture proportionnelle si l'audit échoue
- `ig-caption-writer` / `ig-carousel-planner` : regénérer avec une formule qui a fait ses preuves
