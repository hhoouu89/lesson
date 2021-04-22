import quopri
from super_web_framework.views.shared.page_not_found_404 import PageNotFound404


class SuperWebFramework:
    """Base of the framework"""
    page_not_found_view: PageNotFound404 = PageNotFound404()

    def __init__(self, url_routes, front_layer_actions):
        self.url_routes = url_routes
        self.front_layer_actions = front_layer_actions

    @staticmethod
    def __get_url_end(environment: dict) -> str:
        """
        Возвращает то, что идёт после первого слеша в юрл адресе.
        :param environment:
        :return: Возвращает то, что идёт после первого слеша в юрл адресе.
        """
        url_end = environment['PATH_INFO']  # адрес, по которому выполнен переход
        if not url_end.endswith('/'):
            url_end = f'{url_end}/'
        return url_end

    def __get_view(self, url_end: str):
        """
        Получить вью
        :param url_end: Ничто иное как то, что идёт после первого слеша в юрл адресе.
        :return: Возвращает view.
        """
        view = self.page_not_found_view
        if url_end in self.url_routes:
            view = self.url_routes[url_end]
        return view

    def create_request(self) -> dict:
        request = dict()
        for front_layer_action in self.front_layer_actions:
            front_layer_action(request)
        return request

    def __call__(self, environment: dict, start_response):
        url_end = SuperWebFramework.__get_url_end(environment)
        view = self.__get_view(url_end)
        request = self.create_request()
        result_code, html_content = view(request)
        start_response(result_code, [('Content-Type', 'text/html')])
        return [html_content.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = dict()
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
