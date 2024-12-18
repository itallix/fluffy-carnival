## Финальное решение
Презентация - [team 39.pdf](https://github.com/itallix/fluffy-carnival/blob/main/final_solution/presentation/team%2039.pdf), также в папке [presentation](https://github.com/itallix/fluffy-carnival/tree/main/final_solution/presentation) есть версия pptx.


### Аугментация данных:
Весь процесс аугментации - [augmentation_5_classes.ipynb](https://github.com/itallix/fluffy-carnival/blob/main/final_solution/augmentation_5_classes.ipynb)
1. Аугментация данных за счет двойного перевода «ru – en – ru» Использовались модели от Helsinki-NLP. Таким образом были аугментированы 5 классов: anger, fear, disgust, sadness, surprise. Получилось увеличть тренирововчные данные с 43410 до 50745.
2. Добавление данных с [твитами](https://www.kaggle.com/datasets/pashupatigupta/emotion-detection-from-text) на английском языке:

   - sadness: 5165
   - surprise: 2187
   - anger: 110
   
   Для перевода использовалась модель от Helsinki-NLP. Это позволило увеличить тренировочный датасет до 58204.

### Обучение модели:
Весь процесс обучения - [emotion_classification_berts.ipynb](https://github.com/itallix/fluffy-carnival/blob/main/final_solution/emotion_classification_berts.ipynb)
 Параметр | Значение |
|----------|-----------|
Модель| ai-forever/ruRoberta-large
Количество экпох | 4
tokenizer: max_length | 32
tokenizer: batch_size | 64
Результат f1 на тесте | 0.59814
