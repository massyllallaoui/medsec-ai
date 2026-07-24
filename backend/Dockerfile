FROM python:3.11-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier uniquement les requirements d'abord (optimisation du cache Docker)
COPY requirements.txt .

# Installer les dépendances sans garder le cache pour alléger l'image
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code de l'application
COPY . .

# Exposer le port de l'API
EXPOSE 8000

# Commande de lancement (avec rechargement auto pour le développement)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
