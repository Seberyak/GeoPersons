from django.shortcuts import render
from django.http import HttpResponse
from random import randrange
import os


Converted = {
    'ა': 'a',
    'ბ': 'b',
    'გ': 'g',
    'დ': 'd',
    'ე': 'e',
    'ვ': 'v',
    'ზ': 'z',
    'თ': 't',
    'ი': 'i',
    'კ': 'k',
    'ლ': 'l',
    'მ': 'm',
    'ნ': 'n',
    'ო': 'o',
    'პ': 'p',
    'ჟ': 'j',
    'რ': 'r',
    'ს': 's',
    'ტ': 't',
    'უ': 'u',
    'ფ': 'f',
    'ქ': 'q',
    'ღ': 'gh',
    'ყ': 'y',
    'შ': 'sh',
    'ჩ': 'ch',
    'ც': 'c',
    'ძ': 'dz',
    'წ': 'w',
    'ჭ': 'ch',
    'ხ': 'kh',
    'ჯ': 'j',
    'ჰ': 'h',
}


def convert(string):
    newstring = ''
    for i in string:
        if i in Converted.keys():
            newstring += Converted[i]
        else:
            newstring += i
    return newstring


def get_lname():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'static/Gvarebi.txt')
    l_names = open(file_path, 'r').readlines()
    l_name = l_names[randrange(len(l_names))][:-1]
    return l_name


def get_name():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'static/saxelebi.txt')
    names = open(file_path, 'r').readlines()
    name = names[randrange(len(names))][:-2]
    return name


def create_person(params):
    if 'results' not in params.keys():
        params['results'] = '1'
    info = list()

    for i in range(int(params['results'])):
        data = dict()
        data["first_name"] = [get_name()]
        data["first_name"].append(convert(data["first_name"][0]))

        data["last_name"] = [get_lname()]
        data["last_name"].append(convert(data["last_name"][0]))

        data['email'] = data["first_name"][1] + '.' + data["last_name"][1] + '@example.com'

        if 'age' in params.keys():
            try:
                data["age"] =int(params["age"])
            except:
                data["age"] = randrange(18, 100)
        else:
            data["age"] = randrange(18, 100)
        info.append(data)

    return info


def index(request):
    response_data = dict()
    response_data['results'] = list()
    if len(request.GET.keys()) == 0:
        response_data = create_person({})
    else:
        response_data = create_person(request.GET)
    return HttpResponse(str(response_data), content_type='application/json; charset=utf-8')
