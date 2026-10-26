---
name: instagram-marketing
description: "Planifier, rédiger et auditer du contenu pour Instagram. Utilise ce bundle quand l'utilisatrice dit « écris la légende de mon reel » (hook dans les 125 premiers caractères), « planifie mon carrousel » slide par slide, « décortique le hook de ce reel viral », « trouve-moi des hashtags » calibrés façon 2026, « enlève les tics d'IA de ma légende », « planifie ma semaine de contenu », ou « qu'est-ce qui marche dans ma niche ». Instagram exige un média sur chaque post : les skills écrivent le texte, l'utilisatrice ajoute l'image ou la vidéo et publie elle-même dans l'app Instagram."
---

# Skills marketing Instagram

Un bundle de 9 skills ciblées pour la création de contenu Instagram en 2026.
Chaque skill a un seul rôle, suit le schéma brouillon, puis validation, puis
livraison du texte, et laisse l'utilisatrice publier elle-même dans l'app
Instagram avec son média.

## Quand utiliser ce bundle

- **Écrire une légende** (hook dans les 125 premiers caractères, corps, CTA) -> utilise `ig-caption-writer`
- **Planifier un carrousel** slide par slide (de la slide d'accroche à la slide de récompense) -> utilise `ig-carousel-planner`
- **Décortiquer le hook** d'un reel ou d'un carrousel viral -> utilise `ig-hook-extractor`
- **Calibrer les hashtags** (la réalité des 3 à 5 tags niche, intermédiaires et larges, pas 30) -> utilise `ig-hashtag-strategist`
- **Retirer les tics d'IA d'une légende, ou l'auditer avant de poster** -> utilise `ig-humanizer` (réécriture plus `--mode audit`, qui intègre le sous-outil d'audit de post)
- **Planifier une semaine** de reels, de carrousels et de stories -> utilise `ig-content-planner`
- **Adapter du contenu venu d'ailleurs** (un post LinkedIn, un article de blog, un script YouTube ou un fil X) en carrousel ou en légende native Instagram -> utilise `ig-repurposer`
- **Auditer et réécrire le profil** (photo, champ NOM, bio, lien, stories à la une, les 9 premières cases de la grille, posts épinglés) -> utilise `ig-profile-optimizer`
- **Lire ta niche et tes stats de profil à partir de vraies données** (scanner un hashtag pour voir ce qui marche, tirer les stats d'abonnés et de posts pour toi ou une concurrente) -> utilise `ig-audience-insights`

## Schéma de base

Chaque skill qui produit quelque chose suit quatre étapes :

1. **Analyser l'entrée.** Si l'utilisatrice donne une URL Instagram, la skill
   utilise `lib/url_parser.py` pour en extraire le nom d'utilisateur et le
   shortcode.
2. **Rédiger et montrer le brouillon.** La skill applique les recherches 2026
   (formules de hooks Instagram, calibrage des hashtags, timing, règles de
   voix, heuristiques de classement) et montre le brouillon à l'utilisatrice.
3. **Attendre la validation.** Rien n'est final tant que l'utilisatrice n'a pas
   dit oui, dans ses propres mots, dans cette conversation.
4. **Livrer le texte final avec le rappel du média.** Le texte validé arrive
   dans un bloc à copier-coller, suivi d'un rappel : ajoute l'image ou la vidéo
   dans l'app Instagram, car Instagram refuse les posts sans média.

## Le média est obligatoire (à lire en premier)

Instagram refuse les posts sans image ni vidéo. Les skills d'écriture
produisent la légende, le hook, les hashtags et le plan des slides ou des plans
de tournage. C'est l'UTILISATRICE qui fournit l'image ou la vidéo, au moment où
elle publie dans l'app. Le chemin de livraison est toujours le même :

```
1. le texte validé, dans un bloc à copier-coller
2. le rappel : ajoute ton image ou ta vidéo dans l'app Instagram
3. pour un carrousel : 2 à 10 slides, dans l'ordre, toutes images ou toutes vidéos
```

## Prérequis

Aucune installation nécessaire. Les skills écrivent, tu publies.

Apify est optionnel, et seulement pour `ig-audience-insights` et
`ig-hook-extractor`, qui lisent de vraies données Instagram : soit un token
`APIFY_TOKEN` dans l'environnement, soit le connecteur MCP Apify (voir
`references/mcp-read-layer.md`). Sans Apify, tu colles à la main les posts et
les chiffres que tu vois dans l'app, et la skill fait exactement la même
analyse dessus.

## Règles de voix (intégrées à chaque skill)

1. Zéro tiret long (em dash) et zéro tiret moyen (en dash) entre deux propositions. On remplace par une virgule, deux-points, des parenthèses ou un retour à la ligne, jamais par un point. Pas de double tiret (`--`) non plus.
2. Utilise `..` ou un retour à la ligne comme pause douce quand le rythme le demande.
3. Majuscule à tous les noms de personnes, d'entreprises et de produits.
4. Une phrase peut commencer en minuscule (voix native des légendes) ; les noms gardent leur majuscule.
5. Évite le vocabulaire IA : « booster », « sublimer », « révolutionner »,
   « incontournable », « plonger dans », « n'hésite pas à », « il est essentiel de »,
   « dans un monde où », « véritable », « solution ».
6. Un chiffre précis bat un adjectif. « 47 minutes » bat « rapide ».
7. Une idée par légende. Les 125 premiers caractères portent le hook (le pli « plus »).
8. Les hashtags, c'est du calibrage, pas du volume : 3 à 5 tags calibrés, pas 30.

(Référence canonique : `references/voice-rules.md`. Voir aussi
`references/hook-formulas.md`, `references/algorithm-heuristics.md` et
`references/hashtag-strategy.md`.)

## Comment les URL Instagram sont lues

| Forme de l'URL | Résultat |
|---|---|
| `https://www.instagram.com/p/SHORTCODE/` | shortcode, type `post` |
| `https://www.instagram.com/reel/SHORTCODE/` | shortcode, type `reel` |
| `https://www.instagram.com/USERNAME/` | nom d'utilisateur, type `profile` |
| `https://www.instagram.com/stories/USER/ID/` | nom d'utilisateur + id, type `story` |

`lib.url_parser.parse_instagram_url(url)` renvoie `{username, shortcode,
url_type, canonical_url}`. Un carrousel partage le chemin `/p/` avec une image
seule ; le carrousel se détecte au média, pas à l'URL.

## Pièges connus

- **Le média est obligatoire.** Pas d'image ou de vidéo, pas de post. La skill
  livre le texte et te rappelle d'ajouter le média.
- **Pas de médias mixtes dans un carrousel.** Toutes images ou toutes vidéos,
  jamais les deux.
- **Les 125 premiers caractères, rien d'autre.** Tout ce qui suit est caché
  derrière « plus ».
- **Un carrousel fait 2 à 10 éléments** dans les plans de ces skills (l'app
  native en accepte jusqu'à 20).

## Ressources

- `lib/url_parser.py` : lecture d'une URL Instagram vers nom d'utilisateur et shortcode
- `lib/apify_client.py` : client Python de la couche de lecture Apify (optionnel)
