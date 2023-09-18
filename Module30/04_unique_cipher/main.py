def count_unique_characters(sms):
    lowercase_message = sms.lower()
    unique_chars = len(set(filter(lambda x: lowercase_message.count(x) <= 1, lowercase_message)))
    return unique_chars


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке -", unique_count)

# зачтено
