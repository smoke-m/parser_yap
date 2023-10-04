import logging

# Импорт базового класса ошибок библиотеки request.
from requests import RequestException

from exceptions import ParserFindTagException


# Перехват ошибки RequestException.
def get_response(session, url):
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


# Перехват ошибки поиска тегов.
def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


# Функция будет искать теги с атрибутами, которые переданы при её вызове,
# либо вообще с любыми атрибутами, на что указывает пустой
# словарь — attrs=(attrs or {}). Если тег не найдётся, программа завершит
# работу, а в логи и терминал выведется сообщение об ошибке.
