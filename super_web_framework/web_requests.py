class GetRequests:
    @staticmethod
    def parse_input_data(data: str) -> dict:
        result = dict()
        if data:
            params = data.split('&')
            for item in params:
                key, value = item.split('=')
                result[key] = value
        return result

    @staticmethod
    def get_request_params(environment: dict) -> dict:
        query_string = environment['QUERY_STRING']
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


class PostRequests:
    @staticmethod
    def parse_input_data(data: str) -> dict:
        result = dict()
        if data:
            params = data.split('&')
            for item in params:
                key, value = item.split('=')
                result[key] = value
        return result

    @staticmethod
    def get_wsgi_input_data(environment: dict) -> bytes:
        content_length_data = environment.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = environment['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = dict()
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environment: dict) -> dict:
        data = self.get_wsgi_input_data(environment)
        return self.parse_wsgi_input_data(data)
