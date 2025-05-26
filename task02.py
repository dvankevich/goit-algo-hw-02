'''
https://uk.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BB%D1%96%D0%BD%D0%B4%D1%80%D0%BE%D0%BC

'''
from collections import deque

def is_palindrome(s):
    # Очищуємо рядок: видаляємо пробіли і переводимо в нижній регістр
    cleaned_s = ''.join(s.lower().replace(" ", ""))
    # прибираємо знаки пунктуації
    cleaned_s = cleaned_s.translate( str.maketrans('', '', '-.,!"'))
    
    # Створюємо двосторонню чергу
    dq = deque(cleaned_s)
    
    while len(dq) > 1:
        # Порівнюємо символи з обох кінців черги
        if dq.popleft() != dq.pop():
            return False
            
    return True

# Тести
def test_is_palindrome():
    assert is_palindrome("Hello") == False, "Тест не пройдено"
    assert is_palindrome("12321") == True, "Тест  не пройдено"
    assert is_palindrome("1 2 3 2 1") == True, "Тест  не пройдено"
    assert is_palindrome(" 12 32 1") == True, "Тест  не пройдено"
    assert is_palindrome("123456") == False, "Тест  не пройдено"
    assert is_palindrome("") == True, "Тест не пройдено"  # Пустий рядок є паліндромом
    assert is_palindrome("абба") == True, "Тест не пройдено"
    assert is_palindrome("АБба") == True, "Тест не пройдено"
    assert is_palindrome("1,2!3-2 1") == True, "Тест  не пройдено"

# Запуск тестів
if __name__ == "__main__":
    test_is_palindrome()
    print("Усі тести пройдено успішно!")
   
    lines = [
        "Дід і дід",
        "Е, ти дурен, ерудите!",
        "І розморозь зором зорі",
        "О, гомін німого",
        "простий рядок"
    ]

    for line in lines:
        print("Рядок: ",line,  end=' ')
        if is_palindrome(line):
            print("- є паліндромом")
        else:
            print("- не паліндром")