import requests
import time
import json

# Configuration
USER_TOKEN = "" #Votre Token / Your Token
SOURCE_GUILD_ID = ""  # ID du serveur à copier / Server ID to copy
TARGET_GUILD_ID = ""  # ID du serveur destination / Destination server ID

BASE_URL = "https://discord.com/api/v10"
HEADERS = {
    "Authorization": USER_TOKEN,
    "Content-Type": "application/json"
}

def rate_limit_sleep():
    """Pause pour éviter le rate limit"""
    time.sleep(0.8)

def get_guild_channels(guild_id):
    """Récupère tous les canaux d'un serveur"""
    response = requests.get(f"{BASE_URL}/guilds/{guild_id}/channels", headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Erreur lors de la récupération des canaux: {response.status_code}")
        print(response.text)
        return []

def get_guild_info(guild_id):
    """Récupère les informations d'un serveur"""
    response = requests.get(f"{BASE_URL}/guilds/{guild_id}", headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Erreur lors de la récupération du serveur: {response.status_code}")
        return None

def get_guild_roles(guild_id):
    """Récupère tous les rôles d'un serveur"""
    response = requests.get(f"{BASE_URL}/guilds/{guild_id}/roles", headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Erreur lors de la récupération des rôles: {response.status_code}")
        return []

def create_role(guild_id, name, permissions, color, hoist, mentionable):
    """Crée un rôle"""
    data = {
        "name": name,
        "permissions": str(permissions),
        "color": color,
        "hoist": hoist,
        "mentionable": mentionable
    }
    print(f"   🔄 Création du rôle: {name}")
    response = requests.post(f"{BASE_URL}/guilds/{guild_id}/roles", headers=HEADERS, json=data)
    if response.status_code == 200:
        print(f"   ✅ Rôle créé avec succès!")
        return response.json()
    else:
        print(f"   ❌ Erreur {response.status_code}: {response.text}")
        return None

def modify_role_position(guild_id, role_id, position):
    """Modifie la position d'un rôle"""
    data = [{"id": role_id, "position": position}]
    response = requests.patch(f"{BASE_URL}/guilds/{guild_id}/roles", headers=HEADERS, json=data)
    return response.status_code == 200

def delete_channel(channel_id):
    """Supprime un canal"""
    response = requests.delete(f"{BASE_URL}/channels/{channel_id}", headers=HEADERS)
    return response.status_code == 200 or response.status_code == 204

def create_category(guild_id, name, position, permission_overwrites):
    """Crée une catégorie"""
    data = {
        "name": name,
        "type": 4,  # Type catégorie
        "position": position,
        "permission_overwrites": permission_overwrites
    }
    response = requests.post(f"{BASE_URL}/guilds/{guild_id}/channels", headers=HEADERS, json=data)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"❌ Erreur création catégorie {name}: {response.status_code} - {response.text}")
        return None

def create_text_channel(guild_id, name, category_id, position, topic, slowmode, nsfw, permission_overwrites):
    """Crée un canal textuel"""
    data = {
        "name": name,
        "type": 0,  # Type text
        "position": position,
        "topic": topic,
        "rate_limit_per_user": slowmode,
        "nsfw": nsfw,
        "permission_overwrites": permission_overwrites
    }
    if category_id:
        data["parent_id"] = category_id
    
    response = requests.post(f"{BASE_URL}/guilds/{guild_id}/channels", headers=HEADERS, json=data)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"❌ Erreur création canal {name}: {response.status_code} - {response.text}")
        return None

def create_voice_channel(guild_id, name, category_id, position, bitrate, user_limit, permission_overwrites):
    """Crée un canal vocal"""
    data = {
        "name": name,
        "type": 2,  # Type voice
        "position": position,
        "bitrate": bitrate,
        "user_limit": user_limit,
        "permission_overwrites": permission_overwrites
    }
    if category_id:
        data["parent_id"] = category_id
    
    response = requests.post(f"{BASE_URL}/guilds/{guild_id}/channels", headers=HEADERS, json=data)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"❌ Erreur création canal vocal {name}: {response.status_code} - {response.text}")
        return None

def filter_overwrites(overwrites, target_guild_id, role_mapping):
    """Filtre les permission overwrites pour mapper les rôles"""
    filtered = []
    for overwrite in overwrites:
        # Type 0 = role, Type 1 = member
        if overwrite["type"] == 0:
            # Si c'est @everyone, utiliser l'ID du serveur cible
            if overwrite["id"] == SOURCE_GUILD_ID:
                filtered.append({
                    "id": target_guild_id,
                    "type": 0,
                    "allow": overwrite.get("allow", "0"),
                    "deny": overwrite.get("deny", "0")
                })
            # Si c'est un autre rôle, utiliser le mapping
            elif overwrite["id"] in role_mapping:
                filtered.append({
                    "id": role_mapping[overwrite["id"]],
                    "type": 0,
                    "allow": overwrite.get("allow", "0"),
                    "deny": overwrite.get("deny", "0")
                })
    return filtered

def backup_server():
    """Fonction principale de backup"""
    print("🚀 Démarrage du script de backup Discord...")
    print("=" * 60)
    
    # Vérification des serveurs
    print("\n🔍 Vérification des serveurs...")
    source_guild = get_guild_info(SOURCE_GUILD_ID)
    target_guild = get_guild_info(TARGET_GUILD_ID)
    
    if not source_guild:
        print("❌ Impossible d'accéder au serveur source!")
        return
    
    if not target_guild:
        print("❌ Impossible d'accéder au serveur cible!")
        return
    
    print(f"✅ Serveur source: {source_guild['name']}")
    print(f"✅ Serveur cible: {target_guild['name']}")
    
    # Récupération des canaux source
    print("\n📥 Récupération des canaux du serveur source...")
    source_channels = get_guild_channels(SOURCE_GUILD_ID)
    
    categories = [c for c in source_channels if c["type"] == 4]
    text_channels = [c for c in source_channels if c["type"] == 0]
    voice_channels = [c for c in source_channels if c["type"] == 2]
    
    print(f"   📊 Trouvé: {len(categories)} catégories, {len(text_channels)} canaux texte, {len(voice_channels)} canaux vocaux")
    
    # Récupération des rôles source
    print("\n👑 Récupération des rôles du serveur source...")
    source_roles = get_guild_roles(SOURCE_GUILD_ID)
    print(f"   📊 Total rôles trouvés: {len(source_roles)}")
    
    # Afficher tous les rôles pour debug
    for role in source_roles:
        print(f"      - {role['name']} (ID: {role['id']}, Bot: {role.get('tags', {}).get('bot_id', 'Non')})")
    
    # Filtrer @everyone et les rôles bot
    source_roles = [r for r in source_roles if r["name"] != "@everyone" and not r.get("tags", {}).get("bot_id")]
    source_roles.sort(key=lambda x: x.get("position", 0))
    print(f"   📊 Rôles à copier (sans @everyone et bots): {len(source_roles)}")
    
    # Suppression des canaux existants
    print("\n🗑️  Suppression des canaux du serveur cible...")
    target_channels = get_guild_channels(TARGET_GUILD_ID)
    for channel in target_channels:
        print(f"   Suppression: {channel['name']}")
        delete_channel(channel["id"])
        rate_limit_sleep()
    
    # Mapping des IDs
    role_mapping = {}
    role_mapping[SOURCE_GUILD_ID] = TARGET_GUILD_ID  # Mapping @everyone
    
    # Copie des rôles
    print("\n👑 Création des rôles...")
    created_roles = []
    
    for i, role in enumerate(source_roles):
        print(f"\n   [{i+1}/{len(source_roles)}] Traitement du rôle: {role['name']}")
        try:
            new_role = create_role(
                TARGET_GUILD_ID,
                role["name"],
                int(role.get("permissions", "0")),
                role.get("color", 0),
                role.get("hoist", False),
                role.get("mentionable", False)
            )
            if new_role:
                role_mapping[role["id"]] = new_role["id"]
                created_roles.append((new_role["id"], role.get("position", 1)))
                print(f"   ✅ Rôle créé: {role['name']} → ID: {new_role['id']}")
            else:
                print(f"   ❌ Échec de création du rôle: {role['name']}")
        except Exception as e:
            print(f"   ❌ Erreur pour {role['name']}: {e}")
        rate_limit_sleep()
    
    # Ajuster les positions des rôles
    print("\n📍 Ajustement des positions des rôles...")
    if created_roles:
        for role_id, position in created_roles:
            try:
                modify_role_position(TARGET_GUILD_ID, role_id, position)
            except Exception as e:
                print(f"   ⚠️  Erreur position pour rôle {role_id}: {e}")
            rate_limit_sleep()
    else:
        print("   ⚠️  Aucun rôle à positionner")
    
    # Mapping des IDs
    category_mapping = {}
    
    # Copie des catégories
    print("\n📁 Création des catégories...")
    categories.sort(key=lambda x: x.get("position", 0))
    
    for category in categories:
        overwrites = filter_overwrites(category.get("permission_overwrites", []), TARGET_GUILD_ID, role_mapping)
        new_category = create_category(
            TARGET_GUILD_ID,
            category["name"],
            category.get("position", 0),
            overwrites
        )
        if new_category:
            category_mapping[category["id"]] = new_category["id"]
            print(f"   ✅ {category['name']}")
        rate_limit_sleep()
    
    # Copie des canaux textuels
    print("\n💬 Création des canaux textuels...")
    text_channels.sort(key=lambda x: x.get("position", 0))
    
    for channel in text_channels:
        overwrites = filter_overwrites(channel.get("permission_overwrites", []), TARGET_GUILD_ID, role_mapping)
        parent_id = category_mapping.get(channel.get("parent_id")) if channel.get("parent_id") else None
        
        new_channel = create_text_channel(
            TARGET_GUILD_ID,
            channel["name"],
            parent_id,
            channel.get("position", 0),
            channel.get("topic", ""),
            channel.get("rate_limit_per_user", 0),
            channel.get("nsfw", False),
            overwrites
        )
        if new_channel:
            print(f"   ✅ #{channel['name']}")
        rate_limit_sleep()
    
    # Copie des canaux vocaux
    print("\n🔊 Création des canaux vocaux...")
    voice_channels.sort(key=lambda x: x.get("position", 0))
    
    for channel in voice_channels:
        overwrites = filter_overwrites(channel.get("permission_overwrites", []), TARGET_GUILD_ID, role_mapping)
        parent_id = category_mapping.get(channel.get("parent_id")) if channel.get("parent_id") else None
        
        new_channel = create_voice_channel(
            TARGET_GUILD_ID,
            channel["name"],
            parent_id,
            channel.get("position", 0),
            channel.get("bitrate", 64000),
            channel.get("user_limit", 0),
            overwrites
        )
        if new_channel:
            print(f"   ✅ 🔊 {channel['name']}")
        rate_limit_sleep()
    
    print("\n" + "=" * 60)
    print("✨ Copie terminée avec succès!")
    print(f"📊 Résumé:")
    print(f"   - Rôles: {len(source_roles)}")
    print(f"   - Catégories: {len(categories)}")
    print(f"   - Canaux textuels: {len(text_channels)}")
    print(f"   - Canaux vocaux: {len(voice_channels)}")

if __name__ == "__main__":
    backup_server()