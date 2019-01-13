from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import View

def function_view(request):
    return HttpResponse('response from function view')


def mainview(request):
    return HttpResponse('I love WEB')



class ExampleClassBased(View):
    def get(self, request):
        return render(request, 'example.html', {'list': ['1', '2', '3', 'nikita']})

class OrdersView(View):
    def get(self, request):
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id': '1'},
                {'title': 'Второй заказ', 'id': '2'},
                {'title': 'Третий заказ', 'id': '3'}
            ]
        }
        return render(request, 'orders.html', data)

class OrderView(View):
    def get(self, request, id):
        data = {
            'order': {
                'id': id
            }
        }
        return render(request, 'order.html', data)
