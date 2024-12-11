## Исследования
### Подходы
1. *Exploratory Data Analysis* - [Криптонит_EDA.ipynb](https://github.com/itallix/fluffy-carnival/blob/main/notebooks/%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%BD%D0%B8%D1%82_EDA.ipynb)

2. Тестирование *baseline* решения - [emotion_classification_baseline.ipynb](https://github.com/itallix/fluffy-carnival/blob/main/notebooks/emotion_classification_baseline.ipynb)

3. Тестирование T5 моделия на оригинальном датасете - [emotion_classification_t5.ipynb](https://github.com/itallix/fluffy-carnival/blob/main/notebooks/emotion_classification_t5.ipynb):

    Захотелось уйти от задачи классификации к задаче text-to-text. Метки one-hot были переведены в текст: [1, 0, 0, 0, 1, 0, 0] -> «гнев, грусть»


2. Аугментация 5 классов за счет двойного перевода *«ru – en – ru»* - [augmentation_5_classes.ipynb](https://github.com/itallix/fluffy-carnival/blob/main/notebooks/augmentation_5_classes.ipynb)
