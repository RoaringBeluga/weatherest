import requests


class Api:
    def __init__(self, base_url: str, **kwargs):
        """
        Create the API object.

        :param base_url: str Base URL for the API
        :param kwargs: dict list of arguments
        """
        self._base_url = base_url
        self._request_string = None
        self._params = dict()
        self._post_data = dict()
        self._headers = dict()
        if 'params' in kwargs:
            for key in kwargs['params']:
                self._params[key] = ""

    def add_param(self, param_name, param_value):
        if param_name not in self._params:
            return self
        if param_value is None:
            return self
        self._params[param_name] = param_value
        if self._request_string is None:
            self._request_string = f'?{param_name}={param_value}'
        else:
            self._request_string += f'&{param_name}={param_value}'
        return self

    def add_post_data(self, key_name, data_value):
        self._post_data[key_name] = data_value
        return self

    def set_post_data(self, data: dict):
        """
        Set data for POST request from the dictionary supplied.

        :param data: dict   Data to be set
        """
        self._post_data = data
        return self

    def add_header(self, header, value):
        self._headers[header] = value
        return self

    def query(self, endpoint):
        """
        Send GET request to the endpoint.

        :param endpoint: str
        """
        headers = self._headers if self._headers else {}
        response = requests.get(self._base_url + endpoint, params=self._params, headers=headers)
        return response

    def post_json(self, endpoint):
        headers = self._headers if self._headers else {}
        response = requests.post(self._base_url + endpoint, json=self._post_data, headers=headers)
        return response

    def post(self, endpoint):
        headers = self._headers if self._headers else {}
        response = requests.post(self._base_url + endpoint, data=self._post_data, headers=headers)
        return response

    def delete(self, endpoint):
        headers = self._headers if self._headers else {}
        response = requests.delete(self._base_url + endpoint, headers=headers)
        return response

    def put(self, endpoint):
        headers = self._headers if self._headers else {}
        response = requests.put(self._base_url + endpoint, data=self._post_data, headers=headers)
        return response

    def __str__(self):
        result = "{" + " _base_url: '{}', _request_url: '{}', _params: {} ".format(self._base_url, self._request_string, self._params) + "}"
        return result
