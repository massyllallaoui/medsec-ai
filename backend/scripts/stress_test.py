import requests
import io
import time

# On cible l'API locale (port 8000 à l'intérieur du conteneur)
BASE_URL = "http://localhost:8000/api/v1"

def run_test():
    print("🚀 Démarrage du Stress-Test Asynchrone...")
    
    # 1. Authentification Automatique
    login_data = {"username": "radio@example.com", "password": "azerty123"}
    response = requests.post(f"{BASE_URL}/auth/login", data=login_data)
    
    if response.status_code != 200:
        print("❌ Échec de la connexion. Vérifie que la clinique radio@example.com existe.")
        return
        
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    print("✅ Authentification réussie. Token JWT obtenu.\n")
    
    # 2. Bombardement de l'API avec 5 fausses images
    print("🔥 Envoi de 5 images médicales en rafale...")
    start_time = time.time()
    
    for i in range(1, 6):
        # Création d'une fausse image en RAM (pour aller très vite)
        fake_image = io.BytesIO(b"Ceci est une fausse image IRM" * 1000)
        files = {"file": (f"scan_patient_{i}.jpg", fake_image, "image/jpeg")}
        
        # Envoi à l'API (Simule le bouton "Upload")
        res = requests.post(f"{BASE_URL}/scans/upload", headers=headers, files=files)
        data = res.json()
        print(f"📦 Upload {i}/5 expédié en {res.elapsed.total_seconds():.3f}s -> Statut: {data['status']}")

    total_time = time.time() - start_time
    print(f"\n⏱️ Temps total de réponse de l'API : {total_time:.3f} secondes.")
    print("😎 L'API est libre ! Elle n'a pas attendu les 50 secondes d'analyse IA.")

if __name__ == "__main__":
    run_test()
