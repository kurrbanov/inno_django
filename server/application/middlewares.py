from django.http import HttpResponse


class FirstMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        response = self._get_response(request)
        return response

    def process_exception(self, request, exception):
        print(f"Было получено исключение: {exception}")
        return HttpResponse('У ТЕБЯ ОШИБКИ!!!')
