# 🚗 ADAS License Plate Recognition 🔍

Este repositorio contiene la implementación de un sistema de reconocimiento de placas vehiculares (License Plate Recognition - LPR) como parte de un proyecto mayor de **Asistencia Avanzada al Conductor (ADAS)** para vehículos de bajo costo en México. Se encuentra diseñado para ejecutarse en un entorno embebido utilizando **Raspberry Pi 5**, **Hailo-8L**, y modelos optimizados de **Computer Vision**.

---

## 📌 Objetivos

- Detectar vehículos y sus placas con **YOLOv8n**.
- Realizar OCR sobre las placas usando **EasyOCR**.
- Optimizar para ejecución embebida mediante **ONNX** y futuro soporte para **Hailo**.

---

## 🧠 Tecnologías y herramientas

| Componente          | Descripción                                    |
|---------------------|------------------------------------------------|
| 🧠 Deep Learning     | YOLOv8n (detección) + EasyOCR (OCR)            |
| ⚙️ Formato modelo     | PyTorch (.pt), ONNX (.onnx)                    |
| 🧪 Frameworks        | Ultralytics, OpenCV, Python 3.8                |
| 💡 Optimización      | Exportación a ONNX para ejecución eficiente    |
| 🐍 Entorno virtual   | `venv_lp` con dependencias aisladas            |

---

## 📂 Estructura del proyecto
ocr_license_plate/
├── ocr_test.py # Script de OCR de prueba
├── prub.jpg # Imagen de prueba
├── ocr_resultado.png # Resultado visual del OCR
├── yolov8n.pt # Modelo base YOLOv8n
├── runs/ # Salidas del entrenamiento
│ └── detect/
│ └── placas_yolov8n2/
│ ├── best.pt
│ ├── best.onnx
│ ├── results.png
│ └── ...
└── venv_lp/ # (NO subir al repo si es posible)
