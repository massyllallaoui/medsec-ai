# 🏥 MedSec AI - Portail B2B d'Imagerie Médicale

MedSec AI est une plateforme d'architecture distribuée conçue pour l'analyse sécurisée de radiographies par intelligence artificielle. 

🔗 **[Voir l'interface de démonstration Vercel](https://medsec-ai.vercel.app/)** *(Note: L'interface web est live, le moteur d'inférence asynchrone est actuellement configuré pour un déploiement local).*

## ⚙️ Architecture Technique (Stack Complète)

Ce projet est structuré autour d'un pipeline asynchrone pour encaisser des calculs tensoriels lourds sans bloquer l'API web :

*   **Frontend (UI/UX) :** Next.js 14, React, Tailwind CSS V4 (Interface "Clinique Premium").
*   **Backend (API Web) :** FastAPI (Python) sécurisé par JWT et Bcrypt (Isolation Multi-Tenant).
*   **Base de données :** PostgreSQL (Historique des diagnostics et des scans).
*   **Message Broker :** Redis (Gestion de la file d'attente des images).
*   **Worker Asynchrone :** Celery (Traitement en tâche de fond isolée).
*   **Moteur d'Intelligence Artificielle :** PyTorch & torchvision (Inférence via ResNet-50 avec Lazy Loading pour optimisation RAM), OpenCV/PIL.

## 🚀 Fonctionnalités Clés
- **Sécurité :** Chiffrement des mots de passe, Tokens JWT, et stockage des fichiers médicaux avec UUID.
- **Asynchronisme :** Le client upload son image et reçoit un `scan_id` instantanément. L'IA analyse l'image en arrière-plan et met à jour la base de données.
- **Lazy Loading ML :** Chargement optimisé des poids du modèle PyTorch en mémoire pour éviter les blocages (Deadlocks) lors des forks de processus Celery.
(base) massyl@MacBook-Pro-de-Massyl frontend % 
(base) massyl@MacBook-Pro-de-Massyl frontend % cat << 'EOF' > README.md     
# 🏥 MedSec AI - Portail B2B d'Imagerie Médicale

MedSec AI est une plateforme d'architecture distribuée conçue pour l'analyse sécurisée de radiographies par intelligence artificielle. 

🔗 **[Voir l'interface de démonstration Vercel](https://medsec-ai.vercel.app/)** *(Note: L'interface web est live, le moteur d'inférence asynchrone est actuellement configuré pour un déploiement local).*

## ⚙️ Architecture Technique (Stack Complète)

Ce projet est structuré autour d'un pipeline asynchrone pour encaisser des calculs tensoriels lourds sans bloquer l'API web :

*   **Frontend (UI/UX) :** Next.js 14, React, Tailwind CSS V4 (Interface "Clinique Premium").
*   **Backend (API Web) :** FastAPI (Python) sécurisé par JWT et Bcrypt (Isolation Multi-Tenant).
*   **Base de données :** PostgreSQL (Historique des diagnostics et des scans).
*   **Message Broker :** Redis (Gestion de la file d'attente des images).
*   **Worker Asynchrone :** Celery (Traitement en tâche de fond isolée).
*   **Moteur d'Intelligence Artificielle :** PyTorch & torchvision (Inférence via ResNet-50 avec Lazy Loading pour optimisation RAM), OpenCV/PIL.

## 🚀 Fonctionnalités Clés
- **Sécurité :** Chiffrement des mots de passe, Tokens JWT, et stockage des fichiers médicaux avec UUID.
- **Asynchronisme :** Le client upload son image et reçoit un `scan_id` instantanément. L'IA analyse l'image en arrière-plan et met à jour la base de données.
- **Lazy Loading ML :** Chargement optimisé des poids du modèle PyTorch en mémoire pour éviter les blocages (Deadlocks) lors des forks de processus Celery.
