# Hand Tracking Mouse Control

## Description
Ce projet utilise OpenCV, MediaPipe et PyAutoGUI pour contrôler le curseur de la souris en temps réel à l'aide des mouvements de la main capturés par une webcam. Les fonctionnalités incluent :

- Déplacement du curseur en suivant la position de la paume.
- Détection de main fermée pour effectuer un clic droit.
- Lissage des mouvements pour une interaction plus fluide.

## Fonctionnalités
- Suivi précis des mouvements de la main grâce à MediaPipe.
- Intégration avec PyAutoGUI pour contrôler la souris.
- Affichage en temps réel de l'image avec des annotations visuelles (points et connexions des mains).

## Prérequis
- Python 3.7 ou plus récent.
- Une webcam fonctionnelle.
- Les bibliothèques suivantes installées :
  - `opencv-python`
  - `mediapipe`
  - `pyautogui`
  - `numpy`

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/Louisdavid32/Hand_Tracking_Mouse_Control.git
   cd hand-tracking-mouse-control
   ```
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez le script Python :
   ```bash
   python main.py
   ```
2. Positionnez votre main devant la webcam pour déplacer le curseur.
3. Fermez la main pour effectuer un clic droit.
4. Appuyez sur la touche `q` pour quitter.

## Configuration
- Vous pouvez ajuster le paramètre `smooth_factor` dans le script pour modifier le niveau de lissage des mouvements.
- Changez le seuil dans la fonction `is_hand_closed` pour ajuster la détection de la main fermée.

## Aperçu

![Exemple de fonctionnement](https://via.placeholder.com/800x400.png)

## Contributions
Les contributions sont les bienvenues ! Veuillez soumettre vos propositions via une pull request.

## Licence
Ce projet est sous licence MIT.
