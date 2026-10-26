# 9 skills Instagram en français pour Claude

**Neuf skills qui transforment Claude en équipe contenu pour ton Instagram.** Elles écrivent tes légendes avec le hook dans les 125 premiers caractères, planifient tes carrousels slide par slide, mesurent tes hashtags, organisent ta semaine, démontent les reels viraux, revoient ton profil et lisent ce qui marche dans ton niche. Chaque brouillon est nettoyé de ses tics d'IA et attend ta validation. Tu fournis l'image ou la vidéo, les skills écrivent les mots. Aucune ligne de code à écrire.

Une fois installées, tu demandes simplement à Claude :

- « Écris la légende de mon reel sur [thème] »
- « Planifie une semaine de posts Instagram pour mon [niche] »
- « Qu'est-ce qui marche dans mon niche en ce moment ? » (données réelles via Apify)
- « Réécris cette légende pour qu'elle ne sonne pas IA »

La bonne skill se déclenche toute seule. Tu relis, tu valides, tu publies.

## Installer

Choisis l'endroit où tu utilises Claude. Dans tous les cas, l'adresse est la même : `christelle-stack/instagram-skills-fr`

### App Claude (Mac et Windows)

1. Ouvre l'app Claude
2. Ouvre les **Réglages** (icône roue dentée)
3. Va dans **Skills**
4. Clique sur **Ajouter depuis GitHub**
5. Colle : `christelle-stack/instagram-skills-fr`
6. C'est tout. Ouvre une conversation et demande une légende.

### claude.ai dans le navigateur

1. Ouvre https://claude.ai/code
2. Va dans **Skills** dans la barre latérale
3. Clique sur **Ajouter depuis GitHub**
4. Colle : `christelle-stack/instagram-skills-fr`
5. C'est tout. Les skills s'activent dès que tu parles d'Instagram.

### Claude Code (terminal, VS Code, JetBrains)

```
/plugin marketplace add christelle-stack/instagram-skills-fr
/plugin install instagram-skills-fr@instagram-skills-fr
```

Ou clone le dépôt et ouvre-le comme dossier de travail :

```bash
git clone https://github.com/christelle-stack/instagram-skills-fr.git
cd instagram-skills-fr
```

### Autre agent (Codex, Cursor, tout agent qui lit des fichiers SKILL.md)

```bash
npx skills add christelle-stack/instagram-skills-fr
```

## Ce que tu peux demander

**Une légende :**
> « Écris-moi une légende Instagram sur comment je suis passée de 6 heures à 47 minutes de montage. Le hook en première ligne. »

**Un carrousel :**
> « Transforme mes notes en carrousel de 10 slides sur les erreurs de portfolio des graphistes débutantes. »

**Démonter un reel viral :**
> « Quel hook utilise ce reel ? https://www.instagram.com/reel/XXXX/ (je colle les 3 premières secondes) »

**Mesurer les hashtags :**
> « Donne-moi 5 hashtags pour ce post, calibrés pour que mon compte de 2 000 abonnées puisse ressortir. »

**Vérifier un brouillon avant de publier :**
> « Audite cette légende : tics d'IA et hook dans les 125 premiers caractères : [colle ton texte] »

**Planifier la semaine :**
> « Planifie une semaine de contenu Instagram. Je lance une formation pour les graphistes débutantes. »

Chaque skill te montre un brouillon et attend ton accord. Rien n'est publié sans toi : tu copies le texte validé et tu publies dans l'app Instagram avec ton média.

## Les 9 skills

| # | Skill | Ce qu'elle fait |
|---|---|---|
| 1 | `ig-caption-writer` | Légende avec le hook dans les 125 premiers caractères, corps lisible, un seul CTA choisi selon l'objectif |
| 2 | `ig-carousel-planner` | Carrousel de 2 à 10 slides : couverture qui ouvre la curiosité, valeur tôt, dernière slide qui fait enregistrer |
| 3 | `ig-hashtag-strategist` | 3 à 5 hashtags mesurés (niche, intermédiaire, large) pour qu'un petit compte puisse apparaître |
| 4 | `ig-humanizer` | Nettoie les tics d'IA (mots usés, triades, tirets longs, emojis en trop) et audite un post avant publication |
| 5 | `ig-content-planner` | Plan de la semaine : reels, carrousels, photos et stories jour par jour, avec hook, angle, heure et objectif |
| 6 | `ig-repurposer` | Transforme un post LinkedIn, un article, un script YouTube ou un thread en carrousel ou légende Instagram |
| 7 | `ig-hook-extractor` | Démonte le hook d'un reel ou carrousel viral : formule, pourquoi ça a marché, moule vide pour ton thème |
| 8 | `ig-audience-insights` | Lit les données publiques réelles d'un hashtag ou d'un profil via Apify, puis en tire les formats et hooks qui reviennent |
| 9 | `ig-profile-optimizer` | Note et réécrit le profil : photo, champ nom, bio de 150 caractères, lien, stories à la une, 9 premiers posts, épinglés |

Les règles communes (voix, formules de hook IG1 à IG10, stratégie hashtags, heuristiques de l'algorithme) sont dans `references/`.

## Données réelles avec Apify (optionnel)

Huit skills sur neuf marchent sans rien configurer. Seule `ig-audience-insights` (et le repli de `ig-hook-extractor` quand tu donnes un lien) va chercher des données publiques réelles via [Apify](https://apify.com) : les publications qui circulent sous un hashtag, les chiffres publics d'un profil.

- **Dans Claude Code** : copie `.env.example` en `.env` et renseigne `APIFY_TOKEN`, puis `pip install -r requirements.txt`.
- **Sur claude.ai ou dans l'app** : ajoute le connecteur MCP Apify (voir `references/mcp-read-layer.md`).
- **Sans Apify** : colle les posts et les chiffres à la main, la skill fait la même analyse.

Vérifie le plan et les coûts sur le site d'Apify avant de brancher. Un token est une clé : garde-le sur ton ordinateur, ne le colle jamais dans une conversation partagée.

## Avant de publier

- Les skills écrivent en français et te tutoient. Si Claude dévie, termine ton prompt par « En français, en me tutoyant. »
- Donne du contexte : ton niche, à qui tu parles, l'objectif du post (enregistrer, partager, commenter, s'abonner).
- Relis à voix haute. Si une phrase n'est pas de toi, change-la.
- 3 à 5 hashtags bien choisis valent mieux que 30 au hasard.
- Un viral se démonte pour en garder la structure, pas les mots.

## Structure du dépôt

```
instagram-skills-fr/
├── SKILL.md                 index du bundle et règles de voix
├── skills/                  les 9 skills, une par dossier
├── references/              formules de hook, hashtags, algorithme, profil de voix
├── lib/                     parseur d'URL Instagram et client Apify (Python)
├── .env.example             le seul réglage possible : APIFY_TOKEN
└── .claude-plugin/          manifestes pour l'installation
```

## Licence

MIT. Voir `LICENSE`.
