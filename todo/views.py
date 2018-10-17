from django.shortcuts import render
from .models import TodoUser, TodoApps, TodoNote
import random
from . import api_json_response as response


# Create your views here.


def documentation(request):
    return render(request, 'todo/documentation.html')


def api_request_notes(request, api_request, app_key):
    # sprawdź czy podana aplikacja istnieje w bazie aplikacji
    try:
        app = TodoApps.objects.get(appkey=app_key)
    except:
        return response.Error.Appkey.unknown()

    # sprawdź czy każdy parametr ma swoją wartość
    api_request_list = api_request.split(',')
    if len(api_request_list) % 2 != 0:
        return response.Error.Data.wrong()

    # przechowanie parametrów i wartości w słowniku
    request_dict = {}
    for i in range(0, len(api_request_list), 2):
        request_dict[api_request_list[i]] = api_request_list[i + 1]

    if not request_dict.get('type'):
        return response.Error.Data.missing()

    elif request_dict.get('type') == 'add':
        if not app.canMakeNotes:
            return response.Error.Appkey.no_permission()
        if request_dict.get('title') and request_dict.get('content') and request_dict.get('importance') and request_dict.get('token'):
            try:
                TodoUser.objects.get(user_token=request_dict.get('token'))
                new_note = TodoNote()
                new_note.title = request_dict.get('title')

                if request_dict.get('content') == 'null':
                    new_note.content = ""
                else:
                    new_note.content = request_dict.get('content')

                new_note.user = request_dict.get('token')

                if int(request_dict.get('importance')) < 0:
                    new_note.importance = 0
                elif int(request_dict.get('importance')) > 3:
                    new_note.importance = 0
                else:
                    new_note.importance = request_dict.get('importance')

                try:
                    new_note.save()
                except:
                    return response.Error.Data.wrong()
                return response.Success.success()
            except:
                return response.Error.Data.wrong()
        else:
            return response.Error.Data.wrong()

    elif request_dict.get('type') == 'delete':
        if not app.canDeleteNotes:
            return response.Error.Appkey.no_permission()
        if request_dict.get('id') and request_dict.get('token'):
            try:
                note = TodoNote.objects.get(id=request_dict.get('id'))
                if note.user == request_dict.get('token'):
                    note.delete()
                    return response.Success.success()
                else:
                    return response.Error.Data.wrong()
            except:
                return response.Error.Data.wrong()
        else:
            return response.Error.Data.missing()

    elif request_dict.get('type') == 'edit':
        if not app.canEditNotes:
            return response.Error.Appkey.no_permission()
        if request_dict.get('title') and request_dict.get('content') and request_dict.get(
            'importance') and request_dict.get('token') and request_dict.get('id'):
            try:
                note = TodoNote.objects.get(id=request_dict.get('id'))
                if note.user == request_dict.get('token'):
                    note.title = request_dict.get('title')

                    if request_dict.get('content') == 'null':
                        note.content = ""
                    else:
                        note.content = request_dict.get('content')

                    note.importance = request_dict.get('importance')

                    if int(request_dict.get('importance')) < 0:
                        note.importance = 0
                    elif int(request_dict.get('importance')) > 3:
                        note.importance = 0
                    else:
                        note.importance = request_dict.get('importance')
                    try:
                        note.save()
                        return response.Success.success()
                    except:
                        return response.Error.Data.wrong()
                else:
                    return response.Error.Data.wrong()
            except:
                return response.Error.Data.wrong()
        else:
            return response.Error.Data.missing()

    elif request_dict.get('type') == 'requestactive':
        if not app.canRequestActiveNotes:
            return response.Error.Appkey.no_permission()
        if request_dict.get('token'):
            try:
                notes = TodoNote.objects.all().filter(user=request_dict.get('token'), active=True)
                return response.Success.request(notes)
            except:
                return response.Error.Data.wrong()
        else:
            return response.Error.Data.missing()

    elif request_dict.get('type') == 'requestnonactive':
        if not app.canRequestNonActiveNotes:
            return response.Error.Appkey.no_permission()
        if request_dict.get('token'):
            try:
                notes = TodoNote.objects.all().filter(user=request_dict.get('token'), active=False)
                return response.Success.request(notes)
            except:
                return response.Error.Data.wrong()
        else:
            return response.Error.Data.missing()

    elif request_dict.get('type') == 'deactivate' or request_dict.get('type') == 'activate':
        if not app.canDeactivateNotes and request_dict.get('type') == 'deactivate':
            return response.Error.Appkey.no_permission()
        if not app.canActivateNotes and request_dict.get('type') == 'activate':
            return response.Error.Appkey.no_permission()
        if request_dict.get('token') and request_dict.get('id'):
            try:
                note = TodoNote.objects.get(id=request_dict.get('id'))
                if note.user == request_dict.get('token'):
                    if request_dict.get('type') == 'deactivate':
                        note.active = False
                    else:
                        note.active = True
                    note.save()
                    return response.Success.success()
                else:
                    return response.Error.Data.wrong()
            except:
                return response.Error.Data.wrong()
        else:
            return response.Error.Data.missing()

    else:
        return response.Error.Data.wrong()


def api_request_users(request, api_request, app_key):
    # sprawdź czy podana aplikacja istnieje w bazie aplikacji
    try:
        app = TodoApps.objects.get(appkey=app_key)
    except:
        return response.Error.Appkey.unknown()

    # sprawdź czy każdy parametr ma swoją wartość
    api_request_list = api_request.split(',')
    if len(api_request_list) % 2 != 0:
        return response.Error.Data.wrong()

    # przechowanie parametrów i wartości w słowniku
    request_dict = {}
    for i in range(0, len(api_request_list), 2):
        request_dict[api_request_list[i]] = api_request_list[i+1]

    if not request_dict.get('type'):
        return response.Error.Data.missing()

    elif request_dict.get('type') == 'add':
        if not app.canMakeUsers:
            return response.Error.Appkey.no_permission()
        if request_dict.get('name') and request_dict.get('password'):
            new_user = TodoUser()
            new_user.name = request_dict.get('name')
            new_user.password = request_dict.get('password')

            # generowanie unikatowego tokenu użytkownika
            token = new_user.name
            for i in range(50):
                token += str(random.randint(0, 9))
            new_user.user_token = token
            try:
                new_user.save()
            except:  # jeżeli podany użytkownik już istnieje
                return response.Error.Data.wrong()
            return response.Success.success()
        else:
            return response.Error.Data.wrong()

    elif request_dict.get('type') == 'delete':
        if not app.canDeleteUsers:
            return response.Error.Appkey.no_permission()
        if request_dict.get('name') and request_dict.get('password'):
            try:
                delete_user = TodoUser.objects.get(name=request_dict.get('name'))
                if delete_user.password == request_dict.get('password'):
                    delete_user.delete()
                    return response.Success.success()
                else:
                    return response.Error.Data.wrong_user()
            except:
                return response.Error.Data.wrong_user()
        else:
            return response.Error.Data.wrong()

    elif request_dict.get('type') == 'login':
        if not app.canLoginUsers:
            return response.Error.Appkey.no_permission()
        if request_dict.get('name') and request_dict.get('password'):
            try:
                user = TodoUser.objects.get(name=request_dict.get('name'))
                if user.password == request_dict.get('password'):
                    return response.Success.login(user.user_token)
                else:
                    return response.Error.Data.wrong_user()
            except:
                return response.Error.Data.wrong_user()
        else:
            return response.Error.Data.missing()
    else:
        return response.Error.Data.wrong()



