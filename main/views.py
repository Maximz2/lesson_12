import logging
from flask import Blueprint, render_template, request
from main.functions import PostHandler

from exceptions import DataLayerError

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="basic.log", level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    logging.info("Запрошена главная страница")
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    s = request.args.get("s", "")
    post_handler = PostHandler('posts.json')
    logging.info("Выполняется поиск")
    try:
        posts = post_handler.search_post_for_substring(s)
        return render_template('post_list.html', posts=posts, s=s)
    except DataLayerError:
        return "Поврежден файл с данными"
