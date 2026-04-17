"""
Модуль client - клиент для работы с внешними API.
Использует библиотеку requests.
"""
import requests
from datetime import datetime

class APIClient:
    """
    Клиент для работы с внешними REST API.
    """
    def __init__(self, base_url=None, timeout=10):
        """
        Инициализация API клиента.
        Args:
            base_url (str): Базовый URL API
            timeout (int): Таймаут запроса в секундах
        """
        self.base_url = base_url or "https://jsonplaceholder.typicode.com"
        self.timeout = timeout
        self.request_count = 0
        self.last_response = None

    def get_posts(self, limit=10):
        """
        Получает список постов.
        Args:
            limit (int): Максимальное количество постов
        Returns:
            list: Список постов или None при ошибке
        """
        url = f"{self.base_url}/posts"
        try:
            print(f"📡 Запрос GET: {url}")
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            self.request_count += 1
            self.last_response = response
            data = response.json()
            print(f"✅ Получено {len(data)} постов")
            # Ограничиваем количество
            return data[:limit]
        except requests.exceptions.Timeout:
            print("❌ Ошибка: превышено время ожидания ответа")
            return None
        except requests.exceptions.ConnectionError:
            print("❌ Ошибка: проблема с подключением к интернету")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"❌ HTTP ошибка: {e}")
            return None
        except Exception as e:
            print(f"❌ Неожиданная ошибка: {e}")
            return None

    def get_users(self):
        """
        Получает список пользователей.
        Returns:
            list: Список пользователей
        """
        url = f"{self.base_url}/users"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            self.request_count += 1
            return response.json()
        except Exception as e:
            print(f"❌ Ошибка при получении пользователей: {e}")
            return None

    def get_user_posts(self, user_id):
        """
        Получает посты конкретного пользователя.
        Args:
            user_id (int): ID пользователя
        Returns:
            list: Посты пользователя
        """
        url = f"{self.base_url}/users/{user_id}/posts"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            self.request_count += 1
            return response.json()
        except Exception as e:
            print(f"❌ Ошибка при получении постов пользователя: {e}")
            return None

    def get_random_quote(self):
        """
        Получает случайную цитату.
        Returns:
            dict: Цитата или None
        """
        # Используем другой API для цитат
        url = "https://api.quotable.io/random"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            self.request_count += 1
            data = response.json()
            return {
                'text': data.get('content', ''),
                'author': data.get('author', 'Unknown'),
                'tags': data.get('tags', [])
            }
        except Exception as e:
            print(f"❌ Ошибка при получении цитаты: {e}")
            return None

    def get_statistics(self):
        """Возвращает статистику запросов."""
        return {
            'total_requests': self.request_count,
            'last_response_code': self.last_response.status_code if self.last_response else None,
            'base_url': self.base_url,
            'timeout': self.timeout
        }

# Тестирование модуля
if __name__ == "__main__":
    client = APIClient()
    
    # Получаем посты
    posts = client.get_posts(5)
    if posts:
        print(f"\nПоследние посты:")
        for post in posts[:3]:
            print(f" - {post['title'][:50]}...")
    
    # Получаем цитату
    quote = client.get_random_quote()
    if quote:
        print(f"\nЦитата дня:")
        print(f" \"{quote['text']}\"")
        print(f" — {quote['author']}")
    
    print(f"\nСтатистика: {client.get_statistics()}")