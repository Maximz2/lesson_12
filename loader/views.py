from flask import Blueprint, render_template, request
import logging

from loader.functions import save_uploaded_picture
from exceptions import PictureWrongTypeError, DataLayerError
from main.functions import PostHandler

loader_blueprint = Blueprint('load_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def create_new_post_page():
    """
    Страница для добавления нового поста
    :return:
    """
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def create_new_post_from_user_data_page():
    """
    Запись нового поста
    :return:
    """

    picture = request.files.get('picture')
    content = request.form.get('content')
    post_handler = PostHandler('posts.json')

    if not picture or not content:
        logging.info("Данные не загружены")
        return "Данные не загружены"

    try:
        picture_path = save_uploaded_picture(picture)
    except PictureWrongTypeError:
        logging.info("Неверный тип файла")
        return "Неверный тип файла"
    except FileNotFoundError:
        return "Не удалось сохранить файл, путь не найден"

    picture_url = "/" + picture_path

    post_object = {"pic": picture_url, "content": content}

    try:
        post_handler.add_post(post_object)
    except DataLayerError:
        return "Не удалось добавить пост, ошибка записи в список постоа"

    return render_template('post_uploaded.html', picture_url=picture_url, content=content)
