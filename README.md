# 🔐 PyPass-Validator

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Sécurité-Mot_de_passe-green?style=for-the-badge)

Outil de sécurité en Python conçu pour évaluer la force des mots de passe via le calcul de l'**Entropie de Shannon** et l'analyse des jeux de caractères.

## 📋 Fonctionnalités
- **Calcul d'Entropie** : Mesure la densité d'information du mot de passe en bits.
- **Détection de Caractères** : Identifie les minuscules, majuscules, chiffres et caractères spéciaux.
- **Évaluation de Sécurité** : Fournit un niveau de risque basé sur les seuils standards de résistance aux attaques par force brute.

## 🔬 Fonctionnement technique
L'outil utilise la formule mathématique :  
`Entropie = L * log2(R)`  
Où **L** est la longueur du mot de passe et **R** la taille du pool de caractères utilisés (ex: 26 pour les minuscules, 95 pour l'ASCII complet).

---

## 🛠️ Utilisation

Pour tester la sécurité de vos mots de passe, suivez ces étapes :

### 1. Cloner le projet
   ```bash
   git clone [https://github.com/yanisdardaz/PyPass-Validator.git](https://github.com/yanisdardaz/PyPass-Validator.git)
   ```
 ### 2. Enter the directory:
   ```bash
    cd PyPass-Validator
   ```
### 3. Run le scipt:
   ```bash
    python3 password_checker.py
   ```
