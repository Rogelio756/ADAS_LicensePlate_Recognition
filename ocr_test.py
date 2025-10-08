import cv2
import easyocr
import matplotlib.pyplot as plt

# RUTA COMPLETA A LA IMAGEN
image_path = "/home/rogelio/venv_lp/prub.jpg"

# Inicializar el lector OCR con español e inglés
reader = easyocr.Reader(['es', 'en'])

# Leer imagen directamente desde ruta con OpenCV
image = cv2.imread(image_path)

# Ejecutar OCR pasando la ruta directamente (más seguro)
results = reader.readtext(image_path)

# Dibujar resultados en la imagen y mostrar en consola
for (bbox, text, prob) in results:
    print(f"Texto: {text} | Confianza: {prob:.2f}")
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(image, text, (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

# Convertir imagen para matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 6))
plt.imshow(image_rgb)
plt.axis("off")
plt.title("Resultado OCR")
plt.savefig("ocr_resultado.png")  # guarda imagen con resultados
# plt.show()  # si tienes entorno gráfico

