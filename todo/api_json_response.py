from django.http import JsonResponse


class Success:
    @staticmethod
    def success():
        return JsonResponse({'Result': 'Success'})

    @staticmethod
    def note_added(note_id, note_date, note_active):
        note_data = {
            'id': note_id,
            'date': note_date,
            'active': note_active
        }
        print("halo")
        return JsonResponse({'Result': 'Success', 'Properties': note_data})

    @staticmethod
    def login(token):
        return JsonResponse({'Result': 'Success', 'Token': token})

    @staticmethod
    def request(notes):
        note_list = []
        for n in notes:
            note = {
                'title': n.title,
                'id': n.id,
                'content': n.content,
                'user': n.user,
                'importance': n.importance,
                'active': n.active,
                'date': n.date
            }
            note_list.append(note)
        return JsonResponse({'Result': 'Success', 'Notes': note_list})


class Error:
    class Appkey:
        @staticmethod
        def unknown():
            return JsonResponse({'Result': 'Error', 'Error': 'Nieznany appkey.'})

        @staticmethod
        def no_permission():
            return JsonResponse({'Result': 'Error', 'Error': 'Appkey nie posiada wymaganych uprawnien.'})

    class Data:
        @staticmethod
        def wrong():
            return JsonResponse({'Result': 'Error', 'Error': 'Nieprawidlowe dane.'})

        @staticmethod
        def wrong_user():
            return JsonResponse({'Result': 'Error', 'Error': 'Nieprawidlowe dane uzytkownika.'})

        @staticmethod
        def missing():
            return JsonResponse({'Result': 'Error', 'Error': 'Brakuje wymaganych atrybutow.'})

