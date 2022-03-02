from exceptions import PictureWrongTypeError


def save_uploaded_picture(picture):
    """
    Запись загруженной картинки в каталог "/uploads"
    :param picture:
    :return:
    """

    file_name = picture.filename

    file_type = file_name.split('.')[-1]

    if file_type not in ['jpg', 'jpeg', 'png', 'svg']:
        raise PictureWrongTypeError

    picture.save(f"./uploads/images/{file_name}")

    return f"./uploads/images/{file_name}"
