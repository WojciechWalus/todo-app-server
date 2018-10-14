from django.http import JsonResponse


def success():
    return JsonResponse({'Result': 'Success'})


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
            return JsonResponse({'Result': 'Error', 'Error': 'Nieprawidlowe dane użytkownika.'})

        @staticmethod
        def missing():
            return JsonResponse({'Result': 'Error', 'Error': 'Brakuje wymaganych atrybutow.'})

