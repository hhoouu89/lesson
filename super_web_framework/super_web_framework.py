import quopri
from super_web_framework.views.shared.page_not_found_404 import PageNotFound404
from super_web_framework.web_requests import GetRequests, PostRequests


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

    def create_request(self, environment: dict) -> dict:
        request = dict()
        method = request['method'] = environment['REQUEST_METHOD']
        if method == 'POST':
            data = PostRequests().get_request_params(environment)
            request['data'] = data
            request['post_request_data'] = data
            print(f'Пришёл post-запрос: {SuperWebFramework.decode_value(data)}')
        elif method == 'GET':
            request_params = GetRequests().get_request_params(environment)
            request['request_params'] = request_params
            request['get_request_data'] = request_params
            print(f'Пришли GET-параметры: {request_params}')
        for front_layer_action in self.front_layer_actions:
            front_layer_action(request)
        return request

    def __call__(self, environment: dict, start_response):
        url_end = SuperWebFramework.__get_url_end(environment)
        view = self.__get_view(url_end)
        request = self.create_request(environment)
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


class DebugApplication(SuperWebFramework):
    def __init__(self, routes_obj, fronts_obj):
        self.application = SuperWebFramework(routes_obj, fronts_obj)
        super().__init__(routes_obj, fronts_obj)

    def __call__(self, env, start_response):
        print('DEBUG MODE')
        print(env)
        return self.application(env, start_response)


class FakeApplication(SuperWebFramework):
    def __init__(self, routes_obj, fronts_obj):
        self.application = SuperWebFramework(routes_obj, fronts_obj)
        super().__init__(routes_obj, fronts_obj)

    def __call__(self, env, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello from Fake']
