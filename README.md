# Electronic Component Classifier

A YOLO11 image classifier that identifies four electronic components from a photo:
resistor, transistor, LED, and electrolytic capacitor.

Trained on a MacBook Pro (M4 Pro) using Apple's MPS GPU backend.

## Results

Two models with the same architecture (YOLO11n-cls) were trained for 30 epochs and compared on a held-out test split (119 images):

| Model | Test accuracy |
|---|---|
| Trained from scratch | 79.8% |
| Pre-trained + fine-tuned | 90.8% |

Starting from pre-trained weights gave about 11 points higher accuracy.

## Known limitations

- The test split comes from the same photo collection as the training data, so real-world accuracy is lower than 90.8%.
- Photos of components that look different from the training photos (for example, blue resistors on a white background) can be misclassified.
- Improving this with more varied training photos is planned.

## Project structure

- scripts/split.py: splits the raw class folders into train, val, and test sets
- scripts/compare.py: evaluates both models on the test split
- models/component_classifier.pt: trained pre-trained + fine-tuned weights
- test_images/: sample images for trying predictions

## Dataset

The dataset (about 1,160 photos) is not included in this repository.
Layout expected by scripts/split.py: a data/ folder with one subfolder of images per class.

| Class | Images |
|---|---|
| LED | 480 |
| Electrolytic capacitor | 403 |
| Transistor | 153 |
| Resistor | 128 |

## Setup

    python3 -m venv venv
    source venv/bin/activate
    pip install ultralytics opencv-python matplotlib pandas

## Train

    python scripts/split.py
    yolo classify train data=dataset model=yolo11n-cls.pt epochs=30 imgsz=224 batch=32 device=mps name=pretrained

## Predict on a photo

    yolo classify predict model=models/component_classifier.pt source=your_photo.jpg device=mps
