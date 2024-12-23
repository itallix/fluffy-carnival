# MIPT Hackathon Winter 2024

## Команда проекта N39

 Участник | Роль | Функции |
|----------|------|---------|
| **Кубракова Екатерина** | `Team Lead`, `Data Scientist` | общая координация проекта, EDA, подготовка данных, тестирование базовых архитектур |
| **Дяминова Эльвира** | `Data Scientist`, `ML Engineer` | подбор гиперпараметров, обучение модели классификатора эмоций на базе T5, подготовка презентации |
| **Лилиом Елизавета** | `Data Scientist`, `NLP Engineer` | аугментация данных, тестирование разных подходов к расширению базового набора данных, балансировка классов, тестирование моделей Paraphrasing, оптимизация baseline решения |
| **Карнюшин Виталий** | `MLOps` | развертывание модели, подготовка инфраструктуры для инференса, сравнительный анализ инференс-серверов, оформление репозитория |

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
3. [Сабмит на Kaggle](https://www.kaggle.com/competitions/cryptonite-hack-sf)

### Ресурсы и материалы
1. [Paper "Emotion Classification in Short English Texts using Deep Learning Techniques"](https://arxiv.org/abs/2402.16034)
2. [Paper "DeepEmotex: Classifying Emotion in Text Messages using Deep Transfer Learning"](https://arxiv.org/abs/2206.06775)
3. [Семинар по классификации текстов с использованием предобученных моделей](https://www.youtube.com/watch?v=uRAsurPHycw)

## Исследования
Наши эксперименты находятся в папке [notebooks](https://github.com/itallix/fluffy-carnival/tree/main/notebooks)

### Подготовка данных
1. Exploratory Data Analysis (EDA). Лемматизация и токенизация данных, составление облака слов для оценки ключевых и наиболее частотных слов. Оценка распределения слов по классам.
2. Аугментация данных за счет двойного перевода «ru – en – ru». Использовались модели от Helsinki-NLP/opus-mt-...-...
   - fear & disgust: 43410 -> 44707
   - anger & fear & disgust & sadness & surprise: 43410 -> 50745
3. Поиск новых датасетов и их апробация на baseline модели. В итоге был взят [датасет с твитами](https://www.kaggle.com/datasets/pashupatigupta/emotion-detection-from-text) на английском языке. Для перевода использовалась модель от Helsinki-NLP. Это позволило увеличить тренировочный датасет до 58204.

### Модели
На данный момент исследованы эти модели от ai-forever. Результаты каждой из них будут представлены позже.
Модели от ai-forever | Num Parameters | Training Data Volume
|--------------------|----------------|---------------------|
| ruBert-base        |178 M           |30 GB                |
| ruBert-large       |427 M           |30 GB                |
| ruRoberta-large    |355 M           |250 GB               |
| ruT5-base          |222 M           |300 GB               |
| ruT5-large         |737 M           |300 GB|              |

## Финальное решение подробно описано в [final_solution](https://github.com/itallix/fluffy-carnival/blob/main/final_solution)
 Параметр | Значение |
|----------|-----------|
Модель| ai-forever/ruRoberta-large
Количество экпох | 4
Результат f1 на тесте | 0.59814
Датасет | Аугментация 5 классов «ru–en–ru» + доп. данные от твитов

Презентация - [team 39.pdf](https://github.com/itallix/fluffy-carnival/blob/main/final_solution/presentation/team%2039.pdf), также в папке [presentation](https://github.com/itallix/fluffy-carnival/tree/main/final_solution/presentation) есть версия pptx.


