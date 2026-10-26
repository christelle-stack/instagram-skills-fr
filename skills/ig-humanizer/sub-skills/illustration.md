# Sous-skill : rédiger le brief visuel d'un post Instagram

Ajoute un brief d'image optionnel à un brouillon (image de feed, slide de
carrousel ou carte-citation). Cette skill n'engendre aucune image et ne
téléverse rien : elle rédige le BRIEF (prompt d'image, texte à incruster,
format, palette) que l'utilisatrice génère ou compose elle-même avec l'outil
de son choix (Canva, Freepik, Midjourney, ou une photo à elle), puis ajoute au
post dans l'app Instagram.

## Quand ça se déclenche

- L'utilisatrice dit « ajoute une image », « fais-moi une illustration »,
  « fais-moi une carte-citation », « il me faut un visuel » ou « fais un
  carrousel » pour un post Instagram.
- À proposer une fois, après validation d'un brouillon, quand un visuel
  augmenterait la portée.

## Deux façons de produire le visuel

- **Génération** : l'utilisatrice colle le prompt dans son générateur d'images
  (Freepik, Midjourney, Canva IA, ou un autre), puis ajoute le texte et le
  logo par-dessus dans Canva ou dans l'outil de son choix.
- **Photo à elle** : le brief décrit alors le cadrage, la lumière et le texte à
  incruster, et l'utilisatrice part d'une photo de sa pellicule.

Dans les deux cas, le brief ne bloque jamais un brouillon : la légende est
livrée, le brief vient en plus.

## Étapes

1. **Choisir le type.** Par défaut pour Instagram : `carrousel` (ratio 4:5,
   1080 x 1350 px). Autres types : miniature 16:9, carrousel / citation /
   portrait 4:5, story / couverture 9:16 (1080 x 1920 px), large / lien 16:9,
   carré 1:1 (1080 x 1080 px). Change le ratio seulement si le post le demande.
2. **Rédiger le prompt.** Décris le sujet, la composition, le style, la
   palette. Par défaut un rendu propre et professionnel, sauf si le Profil de
   voix et de marque fixe un style visuel en §6. N'inclus PAS les mots du post
   dans l'image générée (le texte s'ajoute par-dessus, voir l'étape 3) : les
   générateurs écrivent mal, et un texte incrusté après coup reste net et
   modifiable.
3. **Appliquer l'habillage de marque (si le profil en a un).** Lis
   `../../../references/voice-profile.md` §6. Si un identifiant, une couleur de
   marque ou un logo y sont définis, écris un bloc « Texte à incruster » qui
   précise quoi, où et en quelle couleur, pour que l'utilisatrice le pose
   pixel-net dans Canva :
   ```
   Texte à incruster : @identifiant
   Position : bas droite
   Couleur : #RRGGBB
   Police : celle de la marque (sinon une sans-serif lisible)
   ```
   Pour une **carte-citation**, le texte à incruster est la ligne de hook
   extraite du post (pas dans le prompt), type `citation`, ratio 4:5.
4. **Choisir l'outil.** Propose l'outil le plus simple pour le besoin : une
   photo à elle quand le post parle d'elle, de son lieu ou de son produit ;
   Canva quand il s'agit surtout de texte sur fond ; un générateur d'images
   quand il faut une scène qui n'existe pas. Le texte étant ajouté après, un
   générateur d'entrée de gamme suffit ; n'envoie pas l'utilisatrice vers un
   outil payant sans qu'elle l'ait demandé.
5. **Livrer et confirmer.** Présente le brief dans un bloc à copier-coller
   (format, prompt, palette, texte à incruster, outil conseillé). L'utilisatrice
   génère ou compose l'image, la regarde, et décide. Sur validation du texte,
   livre la légende validée dans son bloc à copier-coller et rappelle d'ajouter
   l'image ou la vidéo dans l'app Instagram au moment de publier.
6. **Sans outil de génération.** Si l'utilisatrice n'a aucun générateur, le
   brief devient un brief photo (cadrage, lumière, accessoires, texte à
   incruster) ou un brief Canva (fond, blocs de texte, couleurs).

## Format du brief

```
BRIEF VISUEL
Type : carrousel (4:5, 1080 x 1350 px)
Prompt : <sujet, composition, style, palette, lumière, sans texte dans l'image>
Palette : <2 ou 3 couleurs, codes hex si le profil les donne>
Texte à incruster : <ligne exacte, position, couleur>
Outil conseillé : <photo à toi / Canva / générateur d'images>
```

## Ajuster plutôt que repartir de zéro

Quand l'utilisatrice veut une retouche (« ciel plus sombre », « change le
titre », « plus d'espace blanc »), ne réécris PAS un prompt neuf. Donne-lui
une consigne de modification à appliquer sur la même image : la plupart des
outils ont une fonction de variation ou de retouche à partir de l'image
précédente, et c'est moins cher et plus cohérent qu'une nouvelle génération.

```
RETOUCHE (à appliquer sur l'image précédente)
Garder : la composition et la palette
Changer : assombrir l'arrière-plan et augmenter le contraste
Texte à incruster : inchangé
```

Si le changement ne porte que sur le texte incrusté, c'est une modification
dans Canva, pas une nouvelle image. Enchaîne les retouches autant de fois que
nécessaire.

## Garde-fou de budget

- Chaque génération coûte des crédits sur les outils payants ; propose un seul
  brief par demande, pas cinq variantes « au cas où ».
- Par défaut, la définition standard (1080 px de large) suffit pour Instagram ;
  ne suggère la haute définition que si l'utilisatrice la demande ou si
  l'image sert aussi ailleurs (impression, site).
- Si l'utilisatrice dit que ses crédits sont bas, oriente vers une photo à
  elle ou une composition Canva avant de proposer une génération de plus.

## Règles dures

- Une image par demande ; les slides d'un carrousel se briefent une par une,
  numérotées.
- Les vrais mots vont dans « Texte à incruster », jamais dans l'image générée.
- Par défaut l'outil simple et la définition standard, sauf demande explicite
  de l'utilisatrice.
- Ne considère jamais un visuel comme validé tant que l'utilisatrice ne l'a
  pas vu et approuvé elle-même.
- Cette skill ne génère et ne publie rien : l'utilisatrice ajoute l'image ou
  la vidéo dans l'app Instagram, avec la légende collée depuis le bloc livré.
