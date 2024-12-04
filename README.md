# MIPT Hackathon Winter 2024

## Параметры проекта по классификации эмоций

### Основные характеристики
 Параметр | Значение |
|----------|-----------|
| **Задача** | Классификация эмоций в текстах |
| **Язык текстов** | Русский |
| **Тип задачи** | Multi-class + Multi-label |
| **Тип модели** | LM (до 1 млрд параметров) |
| **Оцениваемая метрика** | F1-score (weighted) |
| **Количество классов** | 7 (`anger`, `disgust`, `fear`, `joy`, `sadness`, `surprise`, `neutral`) |
| **Домен данных** | Транскрибированные тексты (ASR) |
| **Особенности домена** | Отсутствие пунктуации и капитализации, ошибки транскрибации |
| **Стек технологий** | `pytorch`, `transformers`, `huggingface` |
| **Данные для обучения** | [ссылка](https://disk.yandex.ru/d/awG8jCY01BGcAQ) |

### Требования к итоговой работе
1. Ноутбук с решением кейса с помощью технологического стека
2. Презентация + питч
3. Сабмит на Kaggle

### Ресурсы и материалы
1. [Paper "Emotion Classification in Short English Texts using Deep Learning Techniques"](https://arxiv.org/abs/2402.16034)
2. [Paper "DeepEmotex: Classifying Emotion in Text Messages using Deep Transfer Learning"](https://arxiv.org/abs/2206.06775)
3. [Семинар по классификации текстов с использованием предобученных моделей](https://www.youtube.com/watch?v=uRAsurPHycw)
