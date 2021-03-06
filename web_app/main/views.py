from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from . import models

TITLE = "Blob Game"


class Home(TemplateView):

	title = None
	template_name = "home.html"

	def get_context_data(self, **kwargs):

		return {
			"title": TITLE,
		}

