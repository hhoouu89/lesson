from datetime import date


def front_layer_1(request):
    request['date'] = date.today()


def front_layer_2(request):
    request['key'] = 'key'


fronts = [front_layer_1, front_layer_2]
