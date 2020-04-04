from django.http.response import JsonResponse
from .models import Color as ColorModel

from django.views.generic import View
from django.core.paginator import Paginator
from django.core import serializers
from django.db.utils import IntegrityError

import sys

class Colores(View):
    """View class handling API calls for color listing"""

    def get(self,request):
        """GET request processing"""

        # Fetching all colors records
        color_list = ColorModel.objects.all().order_by('color_id')

        # defaulting number of items per page to 10 if not provided in request or invalid
        try:
            number_colors_per_page = int(request.GET.get('colors_per_page'))
        except:
            number_colors_per_page = 10

        paginator = Paginator(color_list, number_colors_per_page)

        # defaulting page to display to 1 if invalid
        try:
            page = int(request.GET.get('page'))
        except:
            page = 1
        if page < 1 : page = 1
        # defaulting page to display to last page number if provided page to display is greater than
        # max page number
        if page > paginator.num_pages : page = paginator.num_pages

        # defaulting page to display to last page number if page to display is irrelevant
        try:
            page_obj = paginator.get_page(page)
        except:
            page = paginator.num_pages
            page_obj = paginator.get_page(page)

        page_colors = [
            {
                'color_id':c.get('color_id'),
                'name':c.get('name'),
                'hex_code':c.get('hex_code')
            } for c in list(page_obj.object_list.values())
        ]

        d = {'page': page, 'number_pages': paginator.num_pages,
             'number_colors_per_page': number_colors_per_page, 'colors':page_colors}

        return JsonResponse(d, safe=False)

    def post(self, request):
        """POST request processing"""

        if not request.content_type == 'application/x-www-form-urlencoded':
            return JsonResponse({'error':'only application/x-www-form-urlencoded Content-Type header is accepted'}, status=415)

        # checking parameters
        name = request.POST.get('name')
        if name is None or name == '':
            return JsonResponse({'error':'name parameter missing or invalid'}, status=422)
        year = request.POST.get('year')
        if year is None or not ColorModel.check_year(year):
            return JsonResponse({'error':'year parameter missing or invalid'}, status=422)
        hex_code = request.POST.get('hex_code')
        if hex_code is None or not ColorModel.check_hex_code(hex_code):
            return JsonResponse({'error':'hex_code parameter missing or invalid'}, status=422)
        pantone = request.POST.get('pantone')
        if pantone is None or not ColorModel.check_pantone(pantone):
            return JsonResponse({'error':'pantone parameter missing or invalid'}, status=422)

        # retrieving last color id
        last_id = ColorModel.get_last_id()
        if last_id is None : last_id = 0
        new_id  = last_id + 1

        # inserting new color
        try:
            new_color = ColorModel(color_id = new_id, name = name, year = year, hex_code = hex_code, pantone = pantone)
            new_color.save()
        except IntegrityError:
            return JsonResponse({'error':'at least one of the provided parameters already exist'}, status=422)
        except:
            mes = "Unexpected error: {0}".format(sys.exc_info()[0])
            return JsonResponse({'error':mes}, status=422)

        # we return inserted color id
        return JsonResponse({'color_id' : new_id})

class Color(View):
    """View class handling API calls for color details"""

    def get(self, *args, **kwargs):
        """GET request processing"""

        try:
            color_obj = ColorModel.objects.get(color_id=kwargs['color_id'])
        except ColorModel.DoesNotExist:
            return JsonResponse({},status=404)

        color_serialized_object = serializers.serialize('python', [color_obj,])

        return JsonResponse(color_serialized_object[0].get('fields'), safe=False)
