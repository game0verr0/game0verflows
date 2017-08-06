# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def home(request):
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'home.html',
        context={'title': 'Accueil - game0verflows'},
    )
