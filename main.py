import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialiser MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Ouvrir la webcam
cap = cv2.VideoCapture(0)

# Résolution de l'écran
screen_width, screen_height = pyautogui.size()
print(f"Résolution de l'écran : {screen_width}x{screen_height}")

# Liste pour lisser les mouvements
positions = []
smooth_factor = 5  # Nombre de positions à moyenner

def is_hand_closed(hand_landmarks):
    """
    Détecte si la main est fermée en vérifiant la distance entre le pouce et l'index.
    """
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    distance = ((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2)**0.5
    return distance < 0.03  # Ajuste ce seuil selon tes besoins

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Inverser l'image horizontalement (effet miroir)
    frame = cv2.flip(frame, 1)

    # Convertir l'image en RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    # Détecter la main
    results = hands.process(image)

    # Convertir l'image en BGR pour l'affichage
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Dessiner les points de repère de la main
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Obtenir les coordonnées du point central de la main (par exemple, la paume)
            palm_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
            palm_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y

            # Convertir les coordonnées normalisées en coordonnées de l'écran
            cursor_x = int(palm_x * screen_width)
            cursor_y = int(palm_y * screen_height)
            print(f"Position du curseur : ({cursor_x}, {cursor_y})")

            # Ajouter la position actuelle à la liste
            positions.append((cursor_x, cursor_y))

            # Garder seulement les dernières positions
            if len(positions) > smooth_factor:
                positions.pop(0)

            # Calculer la moyenne des positions pour lisser les mouvements
            smooth_x = int(np.mean([p[0] for p in positions]))
            smooth_y = int(np.mean([p[1] for p in positions]))

            # Déplacer le curseur de la souris
            pyautogui.moveTo(smooth_x, smooth_y)

            # Afficher une icône (cercle) à la position du pointeur
            cv2.circle(image, (cursor_x, cursor_y), 10, (0, 255, 0), -1)  # Cercle vert

            # Détecter si la main est fermée pour effectuer un clic droit
            if is_hand_closed(hand_landmarks):
                pyautogui.rightClick()
                cv2.circle(image, (cursor_x, cursor_y), 10, (0, 0, 255), -1)  # Cercle rouge pour indiquer un clic

    # Afficher l'image
    cv2.imshow('Hand Tracking', image)

    # Quitter avec la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()