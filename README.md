# langue : français / french

# 🔄 Discord Server Backup Tool

Un script Python pour copier intégralement la structure d'un serveur Discord vers un autre serveur (rôles, canaux, catégories, permissions).

## ✨ Fonctionnalités

✅ **Copie complète de :**
- 👑 Tous les rôles (couleurs, permissions, hiérarchie)
- 📁 Toutes les catégories
- 💬 Tous les canaux textuels (topic, slowmode, NSFW)
- 🔊 Tous les canaux vocaux (bitrate, limite utilisateurs)
- 🔒 Toutes les permissions par rôle sur chaque canal
- 📍 La structure et hiérarchie complète

❌ **Ne copie PAS :**
- Les messages
- Les membres
- Les bots
- Les emojis personnalisés
- Les stickers

## 📋 Prérequis

- Python 3.7 ou supérieur
- Bibliothèque `requests`
- Votre token utilisateur Discord

## 🚀 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/VOTRE_USERNAME/discord-backup-tool.git
cd discord-backup-tool
```

### 2. Installer les dépendances

**Sur Windows :**
```bash
pip install requests
```

**Sur Mac/Linux :**
```bash
pip3 install requests
```

## ⚙️ Configuration

### 1. Obtenir votre token utilisateur Discord

1. Ouvrez Discord dans votre **navigateur web** (pas l'application)
2. Appuyez sur `F12` pour ouvrir les outils développeur
3. Allez dans l'onglet **Console**
4. Collez ce code et appuyez sur Entrée :

```javascript
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```

5. Copiez le token qui s'affiche (commence par `MTEy...`)

### 2. Obtenir les IDs des serveurs

1. Activez le **Mode Développeur** dans Discord :
   - Paramètres utilisateur → Avancé → Mode développeur ✅
2. **Clic droit** sur le serveur → **Copier l'identifiant du serveur**
3. Faites ça pour les 2 serveurs (source et cible)

### 3. Configurer le script

Ouvrez `backup_discord.py` et modifiez les lignes suivantes :

```python
# Configuration
USER_TOKEN = "VOTRE_TOKEN_ICI"
SOURCE_GUILD_ID = "ID_SERVEUR_A_COPIER"
TARGET_GUILD_ID = "ID_SERVEUR_DESTINATION"
```

## 🎯 Utilisation

### Lancer le script

**Sur Windows :**
```bash
py backup_discord.py
```

**Sur Mac/Linux :**
```bash
python3 backup_discord.py
```

### Ce qui va se passer :

1. ✅ Vérification des serveurs
2. 🗑️ Suppression des canaux existants du serveur cible
3. 👑 Création des rôles
4. 📁 Création des catégories
5. 💬 Création des canaux textuels
6. 🔊 Création des canaux vocaux
7. ✨ Résumé final

## 📊 Exemple de sortie

```
🚀 Démarrage du script de backup Discord...
============================================================

🔍 Vérification des serveurs...
✅ Serveur source: Mon Serveur Original
✅ Serveur cible: Mon Nouveau Serveur

👑 Récupération des rôles du serveur source...
   📊 Total rôles trouvés: 8
   📊 Rôles à copier (sans @everyone et bots): 5

👑 Création des rôles...
   [1/5] Traitement du rôle: Admin
   ✅ Rôle créé: Admin → ID: 123456789

...

✨ Copie terminée avec succès!
📊 Résumé:
   - Rôles: 5
   - Catégories: 3
   - Canaux textuels: 12
   - Canaux vocaux: 4
```

## ⚠️ Avertissements Importants

### Sécurité
- **NE PARTAGEZ JAMAIS** votre token Discord publiquement
- **NE COMMITEZ JAMAIS** votre token sur GitHub
- Ajoutez `backup_discord.py` dans `.gitignore` si vous modifiez les IDs

### Conditions d'utilisation Discord
- L'utilisation de self-bots (automatisation avec votre compte utilisateur) est **contre les conditions d'utilisation de Discord**
- Utilisez ce script **à vos propres risques**
- Discord pourrait suspendre votre compte s'il détecte une automatisation

### Permissions
- Vous devez avoir les **permissions administrateur** sur les deux serveurs
- Le script supprimera **tous les canaux existants** du serveur cible avant de copier

## 🛠️ Dépannage

### Erreur : `pip n'est pas reconnu`
- Installez Python depuis https://www.python.org/downloads/
- Cochez bien "Add Python to PATH" lors de l'installation

### Erreur : `Python est introuvable`
- Sur Windows, utilisez `py` au lieu de `python`
- Sur Mac/Linux, utilisez `python3` au lieu de `python`

### Erreur 401 (Unauthorized)
- Votre token est invalide ou expiré
- Récupérez un nouveau token Discord

### Erreur 403 (Forbidden)
- Vous n'avez pas les permissions nécessaires sur un des serveurs
- Vérifiez que vous êtes administrateur des deux serveurs

### Rate Limited (429)
- Discord limite le nombre de requêtes
- Le script attend automatiquement 0.8s entre chaque action
- Si ça persiste, augmentez le délai dans `rate_limit_sleep()`

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- 🐛 Signaler des bugs
- 💡 Proposer des nouvelles fonctionnalités
- 🔧 Soumettre des pull requests

## ⚖️ Disclaimer

Ce projet est fourni "tel quel", sans garantie d'aucune sorte. L'utilisation de ce script est à vos propres risques. Les auteurs ne sont pas responsables de tout bannissement ou suspension de compte Discord résultant de l'utilisation de cet outil.

---

Made with ❤️ by [TilyesTAG]

# Langue : Anglais / English 

# 🔄 Discord Server Backup Tool

A Python script to copy the entire structure of a Discord server to another server (roles, channels, categories, permissions).

## ✨ Features

✅ **Full copy of:**
- 👑 All roles (colors, permissions, hierarchy)
- 📁 All categories
- 💬 All text channels (topic, slowmode, NSFW)
- 🔊 All voice channels (bitrate, user limit)
- 🔒 All permissions per role on each channel
- 📍 Full structure and hierarchy

❌ **Does NOT copy:**
- Messages
- Members
- Bots
- Custom emojis
- Stickers

## 📋 Requirements

- Python 3.7 or higher
- `requests` library
- Your Discord user token

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/discord-backup-tool.git
cd discord-backup-tool
```

### 2. Install Dependencies

**On Windows:**
```bash
pip install requests
```

**On Mac/Linux:**
```bash
pip3 install requests
```

## ⚙️ Setup

### 1. Get your Discord user token

1. Open Discord in your **web browser** (not the app)
2. Press `F12` to open the developer tools
3. Go to the **Console** tab
4. Paste this code and press Enter:

```javascript
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```

5. Copy the displayed token (starts with `MTEy...`)

### 2. Get the server IDs

1. Enable **Developer Mode** in Discord:
- User Settings → Advanced → Developer Mode ✅
2. **Right-click** on the server → **Copy Server ID**
3. Do this for both servers (source and target)

### 3. Configure the script

Open `backup_discord.py` and modify the following lines:

```python
# Configuration
USER_TOKEN = "YOUR_TOKEN_HERE"
SOURCE_GUILD_ID = "SERVER_ID_TO_COPY"
TARGET_GUILD_ID = "DESTINATION_SERVER_ID"
```

## 🎯 Usage

### Run the script

**On Windows:**
```bash
py backup_discord.py
```

**On Mac/Linux:**
```bash
python3 backup_discord.py
```

### What will happen:

1. ✅ Checking the servers
2. 🗑️ Deleting existing channels from the target server
3. 👑 Creating roles
4. 📁 Creating categories
5. 💬 Creating text channels
6. 🔊 Creating voice channels
7. ✨ Final summary

## 📊 Example output

```
🚀 Starting Discord backup script...
=================================================================

🔍 Checking servers...
✅ Source server: My Original Server
✅ Target server: My New Server

👑 Retrieving roles from source server...
📊 Total roles found: 8
📊 Roles to copy (without @everyone and bots): 5

👑 Creating roles...
[1/5] Processing role: Admin
✅ Role created: Admin → ID: 123456789

...

✨ Copy completed successfully!
📊 Summary:
- Roles: 5
- Categories: 3
- Text Channels: 12
- Voice Channels: 4
```

## ⚠️ Important Warnings

### Security
- **NEVER** share your Discord token publicly
- **NEVER** commit your token to GitHub
- Add `backup_discord.py` to `.gitignore` if you change IDs

### Discord Terms of Service
- Using self-bots (automation with your user account) is **against Discord's Terms of Service**
- Use this script **at your own risk**
- Discord may suspend your account if it detects automation

### Permissions
- You must have **admin permissions** on both servers
- The script will delete **all existing channels** from the target server before copy

## 🛠️ Troubleshooting

### Error: `pip is not recognized`
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### Error: `Python cannot be found`
- On Windows, use `py` instead of `python`
- On Mac/Linux, use `python3` instead of `python`

### Error 401 (Unauthorized)
- Your token is invalid or expired
- Retrieve a new Discord token

### Error 403 (Forbidden)
- You don't have the necessary permissions on one of the servers
- Make sure you are an administrator on both servers

### Rate Limited (429)
- Discord limits the number of requests
- The script automatically waits 0.8 seconds between each Action
- If it persists, increase the timeout in `rate_limit_sleep()`.

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🤝 Contribution

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

## ⚖️ Disclaimer

This project is provided "as is," without warranty of any kind. Use of this script is at your own risk. The authors are not responsible for any bans or suspensions of Discord accounts.

---

Made with ❤️ by [TilyesTAG]
