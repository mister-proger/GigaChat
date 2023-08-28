import re

from django.http import JsonResponse

from . import helper


def determining_login_type(input_string):
    phone_pattern = r'^\+[0-9]+$'
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(phone_pattern, input_string):
        return 'phone'
    elif re.match(email_pattern, input_string):
        return 'email'
    else:
        return 'username'


def register(request):
    if request.GET.get('username', None) is None \
            or request.GET.get('password', None) is None \
            or request.GET.get('contact', None) is None:
        return JsonResponse({
            'status': 'refused',
            'reason': 'BadRequest',
            'description': 'LackOfArguments'
        }, status=400)

    if not helper.validator.validate_name(request.GET['username']):
        return JsonResponse({
            'status': 'refused',
            'reason': 'BadRequest',
            'description': 'BadName'
        }, status=400)

    if not helper.validator.validate_password(request.GET['password']):
        return JsonResponse({
            'status': 'refused',
            'reason': 'BadRequest',
            'description': 'BadPassword'
        }, status=400)

    if helper.validator.CheckAvailability.username(request.GET['username']):
        return JsonResponse({
            'status': 'refused',
            'reason': 'BadRequest',
            'description': 'UsernameAlreadyRegistered'
        }, status=400)

    contact_type = determining_login_type(request.GET['contact'])

    match contact_type:
        case 'email':
            if helper.validator.CheckAvailability.email(request.GET['contact']):
                return JsonResponse({
                    'status': 'refused',
                    'reason': 'BadRequest',
                    'description': 'ContactAlreadyRegistered'
                }, status=400)
        case 'phone':
            if helper.validator.CheckAvailability.phone(request.GET['contact']):
                return JsonResponse({
                    'status': 'refused',
                    'reason': 'BadRequest',
                    'description': 'ContactAlreadyRegistered'
                }, status=400)
        case _:
            return JsonResponse({
                'status': 'refused',
                'reason': 'BadRequest',
                'description': 'NotValidContact'
            }, status=400)

    id = helper.operator.register(
        request.GET['username'],
        request.GET['password'],
        **{contact_type: request.GET['contact']}
    )

    token = helper.operator.create_token(request.META.get('HTTP_USER_AGENT'), id)

    return JsonResponse({
        'status': 'Done',
        'auth-data': {
            'id': id,
            'token': token
        },
        'user-data': {
            'name': request.GET['username'],
            'id': id
        }
    })


def auth(request):
    if request.GET.get('username', None) is None \
            or request.GET.get('password') is None:
        return JsonResponse({
            'status': 'refused',
            'reason': 'BadRequest',
            'description': 'LackOfArguments'
        }, status=400)

    id = helper.DBOperator.get_id(request.GET['username'])

    if id is None:
        return JsonResponse({
            'status': 'refused',
            'reason': 'BadRequest',
            'description': 'UserNotFound'
        }, status=400)

    if not helper.DBOperator.auth(determining_login_type(request.GET['username']), request.GET['username'], request.GET['password']):
        return JsonResponse({
            'status': 'refused',
            'reason': 'BadRequest',
            'description': 'UserNotFound'
        }, status=400)

    return JsonResponse({
        'status': 'Done',
        'auth-data': {
            'id': id,
            'token': helper.operator.create_token(request.META.get('HTTP_USER_AGENT'), id)
        }
    })
