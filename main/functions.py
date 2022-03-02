from exceptions import DataLayerError
import json


class PostHandler:

    def __init__(self, path):

        self.path = path

    def load_post_from_json(self):
        """
        Загружает данные из JSON файла
        :return:
        """
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                posts = json.load(file)
            return posts
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataLayerError("Что-то не так с файлом")

    def search_post_for_substring(self, substring):
        """
        Поиск по постам
        :param substring: Строка для поиска
        :return: Список найденных постов
        """
        substring_lower = substring.lower()
        posts_found = []

        posts = self.load_post_from_json()
        for post in posts:
            if substring_lower in post['content'].lower():
                posts_found.append(post)
        return posts_found

    def add_post(self, post):
        """
        Добавление нового поста
        :param post:
        :return:
        """
        posts = self.load_post_from_json()
        posts.append(post)
        self.save_post_to_json(posts)

    def save_post_to_json(self, posts):
        """
        Запись нового поста
        :param posts:
        :return:
        """
        try:
            with open(self.path, "w", encoding="utf-8",) as file:
                json.dump(posts, file, ensure_ascii=False)
        except FileNotFoundError:
            raise DataLayerError
