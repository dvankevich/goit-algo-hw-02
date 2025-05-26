from queue import Queue
import uuid
import time
import random

#Створити чергу заявок
q = Queue()
'''
Функція generate_request():
    Створити нову заявку
    Додати заявку до черги

Функція process_request():
    Якщо черга не пуста:
        Видалити заявку з черги
        Обробити заявку
    Інакше:
        Вивести повідомлення, що черга пуста

Головний цикл програми:
    Поки користувач не вийде з програми:
        Виконати generate_request() для створення нових заявок
        Виконати process_request() для обробки заявок
'''

def generate_request():
    print("-- generate request")
    q.put(uuid.uuid1())

def process_request():
    print("Processing request",q.get())
    time.sleep(random.randint(1, 3))  # Імітація часу обробки від 1 до 3 секунд

def main():
    # Головний цикл програми:
    while True:
        q_num = random.randint(1, 10) # Кількість заявок
        print("Кількість заявок для генерації",q_num)

        for i in range(q_num):
            print("# ", i+1, end=' ')
            generate_request()
            

        time.sleep(1) # пауза між генерацією заявок і обробкою

        # Обробка заявок
        while not q.empty(): # допоки черга не пуста
            process_request() # обробляємо заявку





if __name__ == "__main__":
        # Спочатку тести
    generate_request()
    assert q.qsize() == 1, "Помилка: Розмір черги не дорівнює 1"
    generate_request()
    assert q.qsize() == 2, "Помилка: Розмір черги не дорівнює 2"
    process_request()
    assert q.qsize() == 1, "Помилка: Розмір черги не дорівнює 1"
    process_request()
    assert q.empty(), "Помилка: Черга має бути пустою"

    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограма завершена.")
