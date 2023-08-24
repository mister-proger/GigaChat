import re

from django.http import JsonResponse

from . import DBOperator


def validate_input(input_string):
    phone_pattern = r'^\+[0-9]+$'
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(phone_pattern, input_string):
        return 'phone'
    elif re.match(email_pattern, input_string):
        return 'email'
    else:
        return 'name'


def register(request):
    if request.GET.get('login', None) is None \
            or request.GET.get('password', None) is None \
            or request.GET.get('contact', None) is None:
        return JsonResponse({
            'status': 'refused',
            'reason': 'BadRequest',
            'description': 'LackOfArguments'
        }, status=400)

    contact_type = validate_input(request.GET['contact'])

    if contact_type is 'name':
        return JsonResponse({
            'status': 'refused',
            'reason': 'BadRequest',
            'description': 'NotValidContact'
        }, status=400)

    if DBOperator.operator.check(contact_type, request.GET['contact']):
        return JsonResponse({
            'status': 'refused',
            'reason': 'BadRequest',
            'description': 'ContactAlreadyRegistered'
        }, status=400)

    id = DBOperator.operator.register(
        request.GET['login'],
        request.GET['password'],
        **{contact_type: request.GET['contact']}
    )

    token = DBOperator.operator.create_token(request.META.get('HTTP_USER_AGENT'), id)

    return JsonResponse({
        'status': 'Done',
        'auth-data': {
            'id': id,
            'token': token
        },
        'user-data': {
            'name': request.GET['login'],
            'id': id
        }
    })


def auth(request):
    if request.GET.get('login', None) is None \
            or request.GET.get('password') is None:
        return JsonResponse({
            'status': 'refused',
            'reason': 'BadRequest',
            'description': 'LackOfArguments'
        }, status=400)

    id = DBOperator.operator.check(validate_input(request.GET['login']), request.GET['login'])

    if id is None:
        return JsonResponse({
            'status': 'refused',
            'reason': 'BadRequest',
            'description': 'UserNotFound'
        }, status=400)

    token = DBOperator.operator.create_token(request.META.get('HTTP_USER_AGENT'), id)

    return JsonResponse({
        'status': 'Done',
        'auth-data': {
            'id': id,
            'token': token
        }
    })
