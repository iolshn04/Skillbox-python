from typing import Any


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache_dict = {}
        self.usage_order = []

    @property
    def cache(self):
        oldest_key = self.usage_order[0]
        return self.cache_dict[oldest_key]

    @cache.setter
    def cache(self, new_elem: Any) -> None:
        key, value = new_elem
        if key in self.cache_dict:
            self.usage_order.remove(key)
        elif len(self.cache_dict) == self.capacity:
            oldest_key = self.usage_order.pop(0)
            del self.cache_dict[oldest_key]
        self.cache_dict[key] = value
        self.usage_order.append(key)

    def get(self, key: Any) -> None:
        if key in self.cache_dict:
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_dict[key]
        else:
            return None

    def print_cache(self):
        for key in self.cache_dict:
            print("{} : {}".format(
                key, self.cache_dict[key]
            ))


# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4

# зачтено
