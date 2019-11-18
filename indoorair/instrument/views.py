from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render # STEP 1 - Import
from django.shortcuts import redirect
from foundations.models import Instrument


def i_list_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "instrument/list.html", {})

def i_create_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "instrument/create.html", {})


def get_instruments_api(request):
    return JsonResponse({
         'version': '1.0',
    })

def post_instruments_create_api(request):
    name = request.POST.get("name")
    print(name)
    try:
        instrument = Instrument.objects.create(
            name=name,
            user=request.user
        )
        print("INSTRUMENT ID", instrument.id)
        return JsonResponse({
         'was_created': True,
        })
    except Exception as e:
        return JsonResponse({
         'was_created': False,
         'reason': str(e),
        })


def i_retrieve_page(request, id):
    return render(request, "instrument/retrieve.html", {
        "instrument_id": int(id),
    })

def i_retrieve_api(request, id):
    try:
        instrument = Instrument.objects.get(id=int(id))
        return JsonResponse({
            'was_found': True,
            'id': instrument.id,
            'name': instrument.name,
        })
    except Exception as e:
        return JsonResponse({
         'was_found': False,
        })

def i_update_page(request, id):
    return render(request, "instrument/update.html", {
        "instrument_id": int(id),
    })

def i_update_api(request, id):
    try:
        name = request.POST.get("name")
        instrument = Instrument.objects.get(id=int(id))
        instrument.name = name
        instrument.save()
        return JsonResponse({
            'was_found': True,
            'id': instrument.id,
            'name': instrument.name,
        })
    except Exception as e:
        print(e)
        return JsonResponse({
         'was_found': False,
        })
