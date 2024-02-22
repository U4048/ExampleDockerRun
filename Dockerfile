# Выбор базового образа с Python
FROM python:3.8-slim
# Установка рабочей директории
WORKDIR /app
# Копирование файлов проекта
COPY . /app
# Запуск приложения
CMD [ "python", "GetTime/Gettime.py" ]