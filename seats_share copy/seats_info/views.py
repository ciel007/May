from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import searchForm, updateForm
from .models import SeatInfo
from django.http import HttpResponse, JsonResponse
from django.views import View
import simplejson
import json


def get_area(request, floor_number):
	floor = int(floor_number)
	available_area = SeatInfo.objects.filer(floor=floor)
	available_area_dict = {}
	for area in available_area:
		available_area_dict[available_area.id] = available_area.area
	return HttpResponse(simplejson.dumps(available_area_dict))


class MainPageView(View):
	@method_decorator(login_required)
	def get(self, request):
		print(request)
		searchform = searchForm()
		updateform = updateForm()
		#print(searchform.fields)
		return render(request, 'seats_info/main_function_page.html', {'searchform': searchform, 'updateform': updateform})

	@method_decorator(login_required)
	def post(self, request):
		if 'pageSize' in request.POST:
			request.POST = request.POST.copy()
			print(request.POST)
			request.POST.pop('pageSize')
			request.POST.pop('pageNumber')
			print(type(request.POST['floor']))
			search_form = searchForm(request.POST)
			if search_form.is_valid():
				inquired_floor = search_form.cleaned_data.get('floor')
				print("here-----------------")
				print(inquired_floor)
				inquired_area = search_form.cleaned_data.get('area')
				seat_entries = SeatInfo.objects.filter(floor=inquired_floor, area=inquired_area).values('floor', 'area', 'table', 'seats')
				print(seat_entries)
				result_list = list(seat_entries)
				return HttpResponse(json.dumps(result_list))

				#return JsonResponse(seat_entries, safe=False)
				#return render(request, 'seats_info/main_function_page.html', {'available_seats':seat_entries})
			else:
				return HttpResponse("something wrong with search_form")

		elif 'update_button' in request.POST:
			print(request.POST)
			request.POST = request.POST.copy()
			request.POST.pop('update_button')
			# floor_value = int(request.POST.get('floor'))
			# seats_value = int(request.POST.get('seats'))
			# request.POST.update({'floor': floor_value})
			# request.POST.update({'seats': seats_value})
			print(request.POST)
			update_form = updateForm(request.POST)
			if update_form.is_valid():
				updated_floor = request.POST.get('floor')
				updated_area = request.POST.get('area')
				updated_table = request.POST.get('table')
				updated_seats = request.POST.get('seats')
				updated_entry = SeatInfo.objects.filter(floor=updated_floor, area=updated_area, table=updated_table).update(seats=updated_seats)
				searchform = searchForm()
				updateform = updateForm()
				return render(request, 'seats_info/main_function_page.html', {'searchform': searchform, 'updateform': updateform})

			else:
				return HttpResponse("form is not valid")

		else:
			return HttpResponse("something wrong with request.POST")





			# request.user.email
			# return render("profile", )