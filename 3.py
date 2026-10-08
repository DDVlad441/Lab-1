import hashlib


def hash_password(password):
    """Повертає md5-хеш пароля у вигляді рядка."""
    return hashlib.md5(password.encode()).hexdigest()

users = {
    "ivan123": {
        "password": hash_password("qwerty1"),
        "full_name": "Іваненко Іван Іванович"
    },
    "olena_p": {
        "password": hash_password("pass2024"),
        "full_name": "Петренко Олена Василівна"
    },
    "max_k": {
        "password": hash_password("secret77"),
        "full_name": "Коваленко Максим Олегович"
    },
}


def check_user(login, password):
    """Перевіряє логін і пароль користувача."""
    if login not in users:
        return False
    return users[login]["password"] == hash_password(password)


def main():
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    if check_user(login, password):
        print(f"Автентифікація успішна. Вітаємо, {users[login]['full_name']}!")
    else:
        print("Невірний логін або пароль.")


if __name__ == "__main__":
    main()