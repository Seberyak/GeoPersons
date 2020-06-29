import datetime
from django.http import HttpResponse
from random import randrange
import os
import json

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


def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(seconds=randrange(0, int((end - start).total_seconds())))


def get_pass(user):
    password = ""
    symbs = '._-$@!#'
    while len(password) < randrange(8, 16):
        for k in user:
            if randrange(2):
                password += k[randrange(1, len(k))]
                break
            if randrange(2):
                password += str(randrange(10))
            if randrange(100) % 3 == 0:
                password += symbs[randrange(len(symbs))]

    r = randrange(len(password))
    password = password[:r] + chr(randrange(65, 90)) + password[r:]

    return str(password)


def create_person(params = dict() ):
    count = 1
    if 'results' in params.keys():
        try:
            count = int(params['results']) if int(params['results']) <= 5000 else count
        except:
            pass
    info = list()

    for i in range(count):
        data = dict()
        data["first_name"] = [get_name()]
        data["first_name"].append(convert(data["first_name"][0]))

        data["last_name"] = [get_lname()]
        data["last_name"].append(convert(data["last_name"][0]))

        data['email'] = data["first_name"][1] + '.' + data["last_name"][1] + '@example.com'

        year = randrange(datetime.datetime.now().year - 100, datetime.datetime.now().year - 18)
        if 'age' in params.keys():
            try:
                year = datetime.datetime.now().year - int(params['age'])
            except:
                pass

        date = str(random_date(datetime.datetime(year, 1, 1), datetime.datetime(year, 12, 31)))
        data['date_of_birth'] = date[:date.index(' ')]

        data['password'] = get_pass(data)

        info.append(data)

    return info


def index(request):
    response_data = dict()
    response_data['results'] = list()
    response_data = create_person(request.GET)

    json_str = json.dumps(response_data, ensure_ascii=False).encode('utf8')

    return HttpResponse(json_str, content_type='application/json')
