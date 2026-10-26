# Règles de nettoyage (Instagram, V3, 2026-09)

Les catalogues par niveau que l'humaniseur applique. Charge ce fichier quand tu
exécutes réellement un nettoyage. Deux niveaux : forensique (toujours actif)
et strict (actif par défaut), plus les nettoyages de format Instagram. V3 : le
vocabulaire est scoré par **densité par paragraphe**, pas supprimé mot à mot.
Le rythme forcé est un tic, pas un remède. Règle française : le tiret long et
le tiret moyen entre deux propositions sont **interdits**, zéro occurrence, et
le trait d'union des mots composés reste normal. Voir « Ce qui a changé en V3 »
dans SKILL.md pour les preuves.

## Sommaire

- Score de densité (comment chaque règle de vocabulaire s'applique)
- Niveau FORENSIQUE (toujours actif)
- Niveau STRICT (actif par défaut)
- Nettoyages de format Instagram (toujours appliqués)
- Passe 2 : Rythme (garde-fou anti-uniformité seulement)
- Passe 3 : Insertions interdites (marqueurs de candeur, atténuations)
- À préserver (la voix de l'utilisatrice, ne pas nettoyer)

---

## Score de densité (comment chaque règle de vocabulaire s'applique)

Le principe du cluster : les lectrices repèrent un texte IA à des grappes de
marqueurs, pas à un mot isolé. Un « notamment » dans un paragraphe, c'est du
français. « Notamment », « complet » et une nominalisation dans le même
paragraphe, c'est une signature.

```python
def score_paragraph(paragraph: str, markers: dict) -> dict:
    """Compte les marqueurs par paragraphe (ou par slide de carrousel). Renvoie les occurrences et l'action à prendre."""
    hits = []
    for name, pattern in markers.items():
        for m in re.finditer(pattern, paragraph, flags=re.I):
            hits.append((name, m.group(0)))
    n = len(hits)
    always = [h for h in hits if h[0] in ("reveal_bridge", "neg_parallel", "sincerity_marker")]
    if n >= 3:
        action = "REWRITE_PARAGRAPH"   # 3 marqueurs ou plus = signal. Réécrire le paragraphe, pas mot à mot.
    elif always:
        action = "REPLACE"             # un pont de révélation / parallélisme négatif / marqueur de candeur est toujours nettoyé,
                                       # même quand il partage le paragraphe avec un seul marqueur ordinaire (vérifié AVANT n == 2)
    elif n == 2:
        action = "FLAG_ONLY"           # 2 = limite. On le signale, on laisse les mots : l'audit tolère 0 à 2 par unité.
    else:
        action = "LEAVE"               # un seul mot courant n'est pas un verdict
    return {"hits": hits, "count": n, "action": action}
```

Règles d'application :
- Les marqueurs forensiques se scorent à part : une occurrence = suppression,
  sans seuil de densité.
- Les comptes au niveau de la légende entière comptent aussi pour deux
  schémas : les triades (3 ou plus par légende = on ramène à la première
  naturelle ; une ou deux triades naturelles passent, le même seuil que
  l'audit) et les fragments isolés (3 ou plus par légende = on refusionne,
  voir Passe 2).
- Ne remplace jamais un mot par un synonyme de la même liste. « Exploiter »
  vers « tirer parti de », ce n'est pas une correction.
- Quand tu réécris un paragraphe, réécris-le dans le registre de l'autrice
  (le casual en minuscules reste en minuscules, ses emojis restent), pas dans
  un registre « neutre ». La neutralité à température uniforme est elle-même
  une empreinte.

---

## Niveau FORENSIQUE (toujours actif)

Les vraies fuites de modèle qu'aucune humaine ne tape. Supprimer ou signaler à vue.

| Motif | Action |
|---|---|
| `oaicite`, `contentReference`, `turn0search0`, `attached_file`, `grok_card` | supprimer le marqueur |
| « À la date de ma dernière mise à jour », « Selon mes connaissances à date », « Je ne peux pas naviguer sur Internet » | supprimer la ligne d'avertissement |
| `[Ton prénom]`, `[Marque]`, `[insérer X ici]`, blancs de gabarit `AAAA-MM-JJ` | signaler, demander à l'utilisatrice de remplir |
| Tout tiret long (U+2014), tout tiret moyen (U+2013) entre deux propositions, tout double tiret (`--`) | remplacer par une virgule, deux-points, des parenthèses, un retour à la ligne ou une réécriture ; jamais un point |

### Règle du tiret long (zéro)

Les données 2026 disent que le caractère seul n'est plus un signal statistique
(GPT-5.4 en émet 1,43 pour 1 000 mots, sous la base humaine de 3,23). Ce
bundle tranche quand même pour une règle simple, parce qu'en français écrit
pour Instagram le tiret long entre deux propositions reste le réflexe le plus
visible des textes générés, et parce qu'une règle à seuil (« environ un pour
100 mots ») est impossible à tenir de tête. Donc : zéro tiret long, zéro
tiret moyen entre deux propositions, dans les textes produits comme dans les
textes corrigés. Ce qui reste forensique en plus, c'est la vieille habitude de
colle de GPT-4 : 3 tirets ou plus dans une légende courte, signature certaine.

```python
EM_DASH = "\u2014"   # tiret long
EN_DASH = "\u2013"   # tiret moyen

def dash_excess(text: str) -> int:
    """Renvoie le nombre de tirets à remplacer. Règle française : la limite est 0, chaque tiret long compte,
    et chaque tiret moyen placé entre deux propositions (entouré d'espaces) compte aussi.
    Un tiret moyen dans une plage de nombres (7-9, 2024-2025) ne compte pas. Une slide de carrousel
    est sa propre unité, même limite : 0."""
    em = text.count(EM_DASH)
    en_between_clauses = len(re.findall(r"\s" + EN_DASH + r"\s", text))
    double = text.count("--")
    return em + en_between_clauses + double

# Ordre de remplacement pour CHAQUE tiret (on garde le sens, pas le caractère) :
#   1. virgule           si le tiret rattache une proposition à la phrase principale
#   2. deux-points       si le tiret introduit une révélation, une liste ou une conséquence
#   3. parenthèses       si la paire de tirets encadre une incise
#   4. retour à la ligne natif Instagram : l'incise prend sa propre ligne
#   5. réécriture        si rien de ce qui précède ne sonne naturel
# JAMAIS un point. « X. Y. » issu d'un tiret coupé crée un empilement de fragments, un tic pire que le tiret.
```

---

## Niveau STRICT (actif par défaut)

Ce que citent les lectrices expertes quand elles repèrent un texte IA
(vocabulaire 53 %, structure des phrases 36 %). Toutes les listes de
vocabulaire et de grammaire passent par `score_paragraph()` ; les ponts de
révélation, le parallélisme négatif et les marqueurs de candeur sont nettoyés
sur une seule occurrence.

### Ponctuation

- Guillemets typographiques anglais (“ ”) vers des guillemets droits ou des
  guillemets français « » selon le registre de l'autrice.
- `--` vers une virgule ou un retour à la ligne (pas un point : un point ici
  empile des fragments).
- Tiret moyen (U+2013) entre deux propositions vers une virgule. Les plages
  de nombres (7-9) restent, écrites avec un trait d'union.
- Les tirets longs sont traités par `dash_excess()` ci-dessus : remplacés,
  jamais simplement effacés sans réécrire la jointure.

### Vocabulaire : marqueurs durables 2026 (scorés par densité)

La liste 2023-24 (« plonger dans », « tapisserie », « au cœur de », « voyage »)
s'efface parce que les humaines évitent désormais ces mots. Les marqueurs
durables sont des mots courants que les LLM sur-sélectionnent à 2 à 5 fois le
taux humain sur les modèles 2026. C'est du français ordinaire, donc un par
paragraphe, ça va. Trois dans un paragraphe, c'est une signature.

| Marqueur | Remplacement préféré quand le paragraphe dépasse le seuil |
|---|---|
| significatif, significativement | un chiffre (« 31 % d'enregistrements en plus », pas « une croissance significative » ; demander s'il n'y en a pas) |
| crucial, essentiel (« il est essentiel de », « il est crucial ») | supprimer, ou « le » |
| notamment, particulièrement | supprimer |
| complet, holistique, à 360° | dire ce que ça couvre |
| insight(s) | dire ce qui a été appris |
| robuste | solide (garder si terme technique) |
| exploiter, exploiter pleinement, tirer parti de | utiliser |
| favoriser, nourrir (figuré) | construire |
| paysage (figuré), écosystème | le secteur, le milieu |
| nuancé | précis |
| multifacette, à plusieurs niveaux | supprimer |
| optimiser, fluidifier, rationaliser | simplifier |
| sublimer, élever, magnifier | améliorer, et dire quoi |
| booster, propulser | faire grimper, avec un chiffre |
| libérer ton potentiel, révéler ton potentiel | supprimer |
| révolutionner, transformer (figuré) | dire ce qui change concrètement |
| incontournable, indispensable | supprimer |
| véritable, authentique (adjectif passe-partout) | supprimer |
| solution | nommer la chose |
| plonger dans, se plonger dans | entrer dans, regarder |
| permettre de | le verbe direct (« tu gagnes 2 heures », pas « ça te permet de gagner 2 heures ») |
| dans le cadre de | pour, pendant |
| magique, merveilleux | supprimer, dire le fait |
| accompagner (figuré, « t'accompagner vers ») | aider, montrer |
| impactant, impacter | marquer, changer |

Adverbes et connecteurs de remplissage (chacun compte pour un marqueur ;
supprimer au-delà du seuil) : fondamentalement, essentiellement, finalement,
pleinement, profondément, véritablement, clairement, certainement,
indéniablement, sans aucun doute, en effet, par ailleurs, force est de
constater.

### Marqueurs grammaticaux (scorés par densité ; la signature structurelle 2026)

```python
GRAMMAR_MARKERS = {
    # Phrases ouvertes sur un participe présent ou un gérondif : 5,3 fois le taux humain.
    # « En exploitant nos données, nous... » / « Partant de là, ... » / casual « en analysant mes stats, j'ai... »
    "ing_opener": r"(?m)^[\s>*\-]*(?:en |tout en )?[a-zA-ZÀ-ÿ]+ant\b[^.]{0,60},",
    # Nominalisations : un verbe transformé en nom qui cache qui agit. « la mise en place de », « l'optimisation de »
    "nominalisation": r"\b(?:la |l')(\w+(?:tion|sion|ment|ance|ence|isation)) (?:de|du|des|d')\b",
    # Noms abstraits empilés
    "abstract_stack": r"\b(alignement|transformation|optimisation|innovation|efficacité|scalabilité|synergie|performance)\b.{0,40}\b(alignement|transformation|optimisation|innovation|efficacité|scalabilité|synergie|performance)\b",
}
# Correction pour ing_opener : mettre qui agit en premier. « En exploitant nos données, on a réduit le churn » -> « on a réduit le churn avec nos données. »
# Correction pour nominalisation : utiliser le verbe. « la mise en place du nouveau process » -> « quand on a lancé le nouveau process »
```

### Couche d'idiomes de modèle 2026 (scorée par densité)

Des formules qui étaient de l'idiome de légende humaine en 2024 et qui sont de
l'idiome de modèle en 2026. Chacune compte pour un marqueur ; « laisse ça
infuser » et « c'est ça, la vraie histoire » sont nettoyées sur une seule
occurrence quand elles servent de clôture.

```python
IDIOM_LAYER_2026 = [
    r"\bdiscrètement\b|\ben silence\b",          # « j'ai discrètement lancé », « lancé en silence »
    r"(?m)^.{1,40}, ça compte\.$",               # « la régularité, ça compte. » comme ligne seule
    r"\bl'effet cumulé\b|\bça se cumule\b",
    r"\bun signal\b|\ble signal\b",
    r"\ble vrai travail\b|\bfaire le travail\b",
    r"\bconstruite? différemment\b|\bbuilt different\b",
    r"\bqui porte tout\b|\bqui tient tout\b",
    r"\bqui fait tout le boulot\b",
    r"\blaisse ça infuser\b|\bmédite là-dessus\b",
    r"\bc'est ça,? la vraie histoire\b",
    r"\bmain character energy\b",
    r"\bsoft launch\b(?! (du|de la|d'un|d'une) \w+)",  # comme humeur, pas comme lancement d'un produit
    r"\bça change tout\b",
    r"\bet c'est ok\b|\bet c'est okay\b",
]
```

### Ponts de révélation (une occurrence = remplacer)

```python
REVEAL_BRIDGES = [
    (r"(?im)^(le|la) (résultat|réponse|leçon|suite|vérité|hic|twist|piège)\s?\?\s*", ""),   # « Le résultat ? », « La suite ? »
    (r"(?im)^et devine quoi\s?\?\s*", ""),                                                     # « Et devine quoi ? »
    (r"(?i)\bce n'est pas (juste |seulement |qu'une question de )?\w[^,.]{0,40}, c'est \b", None),  # « Ce n'est pas X, c'est Y » (réécrire en deux déclaratives)
    (r"(?i)^arrête(z)? de \w[^,.]{0,40}[.,] (commence|commencez) (à|par) \b", None),           # « Arrête de X, commence à Y »
    (r"(?im)^(voilà|voici) (ce qui|ce que|comment|pourquoi|le truc)\b[^:.\n]{0,40}[:.]\s*", ""),  # « Voilà ce qui », « Voilà le truc : »
    (r"(?im)^(plot twist|spoiler|petit rappel|rappel)\s?[:?]\s*", ""),
    (r"(?im)^parlons (de|d')\b[^.\n]{0,40}[.:]\s*", ""),                                       # ouverture « Parlons de… »
]
# Correction : supprimer le pont et laisser la phrase suivante tenir seule. C'était elle, le propos.
# Tics nommés de 2026 sur toutes les listes de lectrices ; mesurés négatifs pour la portée sur LinkedIn (données éditeur).
```

### Parallélisme négatif (une occurrence = réécrire)

Retire les constructions « pas X, mais Y » / « ce n'est pas une question de X,
c'est une question de Y » et toutes leurs cousines (« La question n'est pas X,
c'est Y », « Ce n'est pas X. C'est Y. », « Pas X. Y. »). Réécris en deux
déclaratives, pas par substitution automatique, et signale-le à l'utilisatrice
parce que préserver le sens demande du jugement. Zéro légende humaine de notre
corpus en contient une.

### Règle de trois (stricte à partir d'une certaine densité ; une triade naturelle est permise)

Le tricolon tourne à 2 fois le taux des expertes humaines sur les modèles 2026.
23 % des légendes humaines de notre corpus en contiennent un, donc le tic, c'est
la triade empilée ou parfaitement parallèle, la triade creuse et la répétition,
pas la forme.

```python
NO_NO_JUST = r"\b(pas de \w+|ni \w+)[,.] (pas de \w+|ni \w+)[,.] ((?:juste|seulement|que|rien que) \w+)"   # « Pas de X. Pas de Y. Juste Z. » / « ni X, ni Y, juste Z »

def detect_triads(text: str) -> list:
    patterns = [
        r"(\w+), (\w+),? et (\w+)",                        # triplets de mots
        r"(\w+ \w+), (\w+ \w+),? et (\w+ \w+)",            # triplets de courts groupes
        r"(?m)^(\w+)\. (\w+)\. (\w+)\.$",                  # « Simple. Efficace. Facile. » (aussi une rafale en passe 2)
        NO_NO_JUST,                                        # construction mise en scène, jamais une triade naturelle (aussi un tic de passe 2)
    ]
    return [m for p in patterns for m in re.finditer(p, text, flags=re.I)]

HOLLOW_ADJECTIVES = {"dynamique", "vibrant", "innovant", "rapide", "simple", "efficace", "facile", "audacieux",
                     "clair", "concentré", "scalable", "puissant", "esthétique", "authentique", "unique", "inspirant",
                     "mieux", "moins cher", "plus vite"}
ABSTRACT_NOUNS = {"croissance", "impact", "valeur", "alignement", "innovation", "efficacité", "résultats", "succès",
                  "clarté", "liberté", "échelle", "élan", "régularité", "mindset", "stratégie", "vision", "énergie",
                  "confiance", "sérénité", "abondance"}

def hollow(t: "re.Match", text: str) -> bool:
    """Une triade est creuse quand ses éléments sont interchangeables : chaque élément est un adjectif abstrait ou
    un nom abstrait, et aucun ne porte de preuve (un nom propre, un chiffre, un € ou un %). Des nombres de mots égaux
    ne sont PAS un tic en soi : « les factures Stripe, les logs Vercel et les alertes Shopify » est une triade concrète
    naturelle. Une majuscule seule n'est jamais une preuve : une majuscule qui ouvre une phrase (« Simple, efficace et
    facile », « Simple. Efficace. Facile. ») est une majuscule de phrase, pas un nom. Un nom, c'est une majuscule qui
    n'ouvre PAS une phrase."""
    def opens_sentence(pos: int) -> bool:
        return re.search(r"(?:^|[.!?\n])\s*$", text[:pos]) is not None
    def has_receipt() -> bool:
        for g in range(1, t.lastindex + 1):
            pos = t.start(g)
            for w in t.group(g).split():
                if re.search(r"[0-9€$%]", w):
                    return True
                if w[:1].isupper() and not opens_sentence(pos):
                    return True
                pos += len(w) + 1
        return False
    items = t.groups()
    all_abstract = all(x.lower().strip() in HOLLOW_ADJECTIVES or x.lower().strip() in ABSTRACT_NOUNS
                       or x.lower().split()[-1] in ABSTRACT_NOUNS for x in items)
    return (not has_receipt()) and all_abstract

def triad_action(triads: list, text: str) -> list:
    """À appeler une fois par légende avec les triades de cette légende (issues de detect_triads(text)). Toute triade
    creuse est nettoyée à vue. Les triades naturelles (concrètes, non interchangeables) sont une question de densité,
    sur le MÊME seuil que l'audit : une ou deux passent ; à partir de 3 triades dans la légende, on ramène à la
    PREMIÈRE naturelle. Le mode réécriture n'est jamais plus sévère que le mode audit. Les threads ne sont pas
    mis en commun : le seuil est par légende."""
    actions = []
    over_density = len(triads) >= 3
    kept_one = False
    for t in triads:
        staged = t.re.pattern == NO_NO_JUST          # « pas de X, pas de Y, juste Z » est un tic mis en scène quelle que soit la ponctuation, toujours réécrit
        if hollow(t, text) or staged or (over_density and kept_one):
            actions.append((t, "REWRITE_AS_TWO_OR_FOUR"))   # 2 éléments, ou 4 dont un qui casse le motif
        else:
            actions.append((t, "LEAVE"))
            kept_one = True
    return actions
```

### Formules mortes (supprimer ou réécrire)

- « dans un monde où », « à l'ère de », « à l'heure du numérique », « à l'ère de l'IA »
- « au final », « en fin de compte », « au bout du compte »
- « game-changer », « révolutionner », « passer au niveau supérieur », « incontournable », « indispensable », « changement de paradigme »
- « l'univers de {chose} », « le monde de {chose} »
- « la vérité, c'est que » / « la réalité, c'est que » / « la dure réalité »
- « n'hésite pas à », « il est essentiel de », « il est crucial de », « force est de constater »

### Clôtures mortes (réécrire en un atterrissage ou une demande précise)

- « Et toi, qu'en penses-tu ? »
- « Ton avis ? »
- « Double tap si tu es d'accord. »
- « Tague 3 amies qui en ont besoin. »
- « Commente OUI en dessous. »
- « Laisse ça infuser. »
- « N'hésite pas à partager. »
- Une ligne finale d'un seul mot (« Voilà. »)

Une invitation à enregistrer ou à envoyer qui nomme une raison (« enregistre
ce post avant ta prochaine publication ») n'est pas une clôture morte ; c'est
le CTA qu'Instagram récompense.

### Pluies d'emojis

- 4 emojis ou plus dans une légende, ou un emoji sur chaque ligne : ramener à
  0 à 3 placés avec intention.
- La signature emoji IA 2024-25 (fusée, étincelles, feu, 100, mains levées à
  la suite) est nettoyée comme un ensemble sur une seule occurrence.
- Les 1 à 3 emojis voulus par l'autrice sont de la voix et restent (voir « À préserver »).

## Nettoyages de format Instagram (toujours appliqués)

- Un hook qui a besoin de la ligne 2 pour avoir un sens : réécrire pour que les
  125 premiers caractères tiennent seuls.
- 6 hashtags ou plus, ou n'importe lequel au milieu d'une phrase : ramener à un
  jeu calibré de 3 à 5 en fin de légende ou en premier commentaire (voir
  `../../../references/hashtag-strategy.md`).
- Un titre nu en slide 1 de carrousel : réécrire en promesse + boucle ouverte.
- Une légende de plus de 2 200 caractères : resserrer.
- Texte incrusté sur les slides : aucun tiret long ni tiret moyen ; une slide
  est courte, on coupe en deux lignes ou on met deux-points.

---

## Passe 2 : Rythme (garde-fou anti-uniformité seulement)

Remplace le « CASSER (forcer la burstiness) » de la V2. Les détecteurs ne
scorent pas la burstiness (GPTZero l'a abandonnée en 2023). Les légendes sont
de longueur moyenne, et sur les plateformes où nous avons des données
d'engagement la variance de longueur de phrase est soit neutre soit négative
(nulle sur LinkedIn ; l'uniforme gagne sur Threads), donc le rythme n'est pas
un levier de portée ici. Ce que les lectrices remarquent, c'est l'uniformité
mécanique (la structure = 36 % des jugements d'expertes) et, pire, la variance
mise en scène : l'alternance mécanique long/court est une empreinte
d'humaniseur apprenable. Donc : corriger le rythme seulement là où il sonne
plat, retirer la variance fabriquée partout, ne jamais ajouter de variance
comme tactique.

```python
STACCATO_TELLS = [
    r"(?m)^\w+\.$",                                                        # ligne d'un seul mot pour le drame : « Voilà. » « Exactement. » « Point. »
    r"(?m)^(\w+\. ){2,}\w+\.$",                                            # « Court. Percutant. Fini. » / « Simple. Efficace. Facile. »
    r"(?i)\b(pas de|ni) \w+\. (pas de|ni) \w+\. (juste|que|seulement|rien que) \w+",  # « Pas de X. Pas de Y. Juste Z. »
    r"(?i)\btou(s|tes) les \w+\. (aucun|aucune|rien) (des?|du|de la) \w+",  # « Tous les X. Aucun des Y. »
    r"(?im)^(le|la) (résultat|réponse|leçon|suite|vérité|hic|twist)\s?\?",  # révélation « Le résultat ? » (aussi un pont de révélation au niveau strict)
    r"(?im)^et devine quoi\s?\?",                                           # « Et devine quoi ? »
    r"(?i)\b(pourquoi|comment|et après|et ensuite)\s?\? (parce que|simple|facile)\b",  # pseudo-question socratique
    r"(?i)\b(c'est tout|c'est tout ce qu'il y a à dire|point final|point barre|c'est le post|voilà voilà)\.$",
]

def is_standalone_fragment(s: str) -> bool:
    """Un fragment est une ligne courte sans sujet + verbe conjugué : « Voilà. », « Exactement. », « Aucune excuse. »,
    « À chaque fois. » Une phrase courte complète (« Ça a marché. », « Les ventes ont monté. ») n'est pas un fragment
    et ne compte jamais dans la limite ; ce n'est pas la brièveté qui trahit, c'est le fragment-pour-le-drame."""
    return len(s.split()) < 4 and not has_subject_and_verb(s)

def restore_rhythm(text: str) -> str:
    """V3. Retire la variance mise en scène ; déplatit seulement ce qui sonne plat comme une machine. Ne fabrique jamais de variance."""
    paragraphs = split_paragraphs(text)
    fragments_seen = 0

    for i, p in enumerate(paragraphs):
        # 1. Tuer d'abord le rythme mis en scène. Fusionner les rafales en une phrase complète avec une vraie proposition.
        for pat in STACCATO_TELLS:
            if re.search(pat, p):
                p = merge_into_sentence(p, pat)     # « Pas de filtre. Pas de preset. Juste la lumière. » -> « pas de filtre ni de preset, juste la lumière de la fenêtre. »

        sents = split_sentences(p)
        lengths = [len(s.split()) for s in sents]

        # 2. Limiter les fragments isolés à 2 par LÉGENDE, pas par paragraphe. Seuls les vrais fragments comptent ;
        #    « Ça a marché. Les ventes ont monté. Les clientes sont revenues. » fait trois phrases courtes, pas trois fragments.
        for j, s in enumerate(sents):
            if is_standalone_fragment(s):
                fragments_seen += 1
                if fragments_seen > 2:
                    sents[j] = attach_to_neighbor(sents, j)   # rattacher à la phrase précédente avec une virgule ou deux-points

        # 3. Déplatir SEULEMENT un paragraphe plat comme une machine : 4 phrases ou plus, chacune à plus ou moins 3 mots
        #    de la moyenne, aucune subordonnée nulle part. Alors allonger LA phrase qui porte le plus de contenu en la
        #    joignant à sa voisine naturelle par une proposition qui travaille (parce que / qui / quand / après), pas une
        #    virgule de raccord. Une fois par paragraphe, et seulement si le résultat sonne comme l'autrice. Un paragraphe
        #    avec une phrase longue et une courte est déjà bien.
        if len(sents) >= 4 and all(abs(n - mean(lengths)) <= 3 for n in lengths) and not any(has_working_clause(s) for s in sents):
            k = max(range(len(sents)), key=lambda j: lengths[j])
            j = k + 1 if k + 1 < len(sents) else k - 1
            sents[k] = join_with_clause(sents[k], sents[j])
            del sents[j]                              # la voisine absorbée est retirée pour que rien n'apparaisse deux fois

        # 4. Jamais long/court/long/court. Si le paragraphe alterne maintenant (4 phrases ou plus qui basculent entre
        #    court < 8 mots et long >= 16 mots), replier la DEUXIÈME phrase courte dans la phrase qui la précède.
        #    La balançoire est l'empreinte de l'humaniseur.
        lengths = [len(s.split()) for s in sents]
        if len(lengths) >= 4 and all((lengths[k] < 8) != (lengths[k + 1] < 8) for k in range(len(lengths) - 1)) \
                and all(n < 8 or n >= 16 for n in lengths):
            k = [j for j, n in enumerate(lengths) if n < 8][1]
            sents[k - 1] = join_with_clause(sents[k - 1], sents[k])
            del sents[k]

        # 5. Légendes à une idée par ligne (chaque paragraphe = une phrase) et slides de carrousel : ne pas toucher au rythme.

        paragraphs[i] = rejoin_keeping_breaks(p, sents)   # ré-attacher les retours à la ligne simples du paragraphe ; la passe retouche des phrases, jamais des sauts de ligne

    return "\n\n".join(paragraphs)
```

Mise en page contre rythme : des lignes d'une seule phrase avec des lignes
vides entre elles, c'est la mise en page native d'une légende Instagram, et
cette passe n'y touche **pas**. « j'ai fait passer un compte de 0 à 10k en 4
mois. » sur sa propre ligne, c'est de la mise en page. « Voilà. » sur sa
propre ligne, c'est du fragment-pour-le-drame. La passe retouche des phrases,
jamais des retours à la ligne.

## Passe 3 : Insertions interdites (marqueurs de candeur, atténuations)

La passe 3 n'ajoute que de la concrétude (un chiffre à précision bizarre avec
son référent, une entité nommée, un fait daté énoncé à plat). Elle n'ajoute
jamais ce qui suit, et la passe 1 stricte le retire quand le brouillon
l'utilise déjà en ouverture ou en pivot :

```python
SINCERITY_MARKERS = [
    # Ancré au début de ligne OU à une frontière de phrase, pour attraper aussi un pivot sur la même ligne (« Le lancement a raté. Franchement, ça a fait mal. »).
    r"(?im)(?:^|(?<=[.!?]\s))(franchement|pour être (honnête|franche|cash|transparente)|soyons (honnêtes|francs|franches)|on ne va pas se mentir|je vais être (honnête|cash|directe|transparente|claire)|en toute (transparence|honnêteté)|la version honnête,? c'est|sans mentir|je peux être (honnête|vulnérable)|je vais dire ce que personne ne dit|avis impopulaire|storytime)[:,.]?\s*",
    r"(?im)(?:^|(?<=[.!?]\s))pov\s?:\s*(?!.*\b(tu|toi|ton|ta|tes|vous)\b)",   # « POV : » sur quelque chose qui n'est pas un point de vue
    r"(?i)\b(je me trompe peut-être,? mais|peut-être|il me semble que|à mon humble avis|je pense qu'on peut dire|je crois que c'est juste de dire)\b",  # atténuations insérées : à nettoyer seulement si ABSENTES des échantillons de voix de l'autrice
]
# Correction : supprimer le marqueur et garder la phrase qui suit. Si la phrase qui suit n'est pas un fait précis,
# c'est le marqueur qui faisait le travail de vulnérabilité. Demander le fait à l'autrice.
# Preuve : l'hésitation jouée est 2 fois plus fréquente dans les textes de LLM que chez les expertes humaines ; la
# « fausse vulnérabilité » est un tic nommé de 2026. La règle : n'en fabriquer jamais, et ne jamais envelopper un fait dedans.
```

## À préserver (la voix de l'utilisatrice, ne pas nettoyer)

- Le registre casual en minuscules si c'est comme ça que l'utilisatrice écrit ses légendes
- Les `..` comme pause douce et les retours à la ligne simples comme temps
- Un ou deux fragments de phrase utilisés exprès (« à chaque fois. ») : la
  limite est 2 par légende, pas 0
- Le trait d'union des mots composés (porte-clés, c'est-à-dire, peut-être) :
  ce n'est pas un tiret long, on n'y touche pas
- Une règle de trois naturelle avec des éléments concrets, non
  interchangeables (23 % des légendes humaines en ont une)
- Une phrase vraiment longue par paragraphe, même si un guide de style la couperait
- Les 1 à 3 emojis voulus par l'autrice
- Les contractions et l'oral écrit (« y a », « t'as », « j'sais pas ») si c'est sa voix
- Les chiffres précis avec référent et les entités nommées (en AJOUTER, jamais en retirer)
- Les détails sensoriels à la première personne
- Les réactions et les opinions de l'autrice, y compris une opinion brutale.
  Un ton plat sur toute une légende est une empreinte d'humaniseur
- Un marqueur de mot courant isolé dans un paragraphe (« notamment »,
  « robuste » comme terme technique). Un seul n'est pas un verdict
- Son histoire réelle. N'invente jamais un détail pour faire atterrir une légende
