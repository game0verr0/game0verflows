# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *


def home(request):
    return render(
        request,
        'home.html',
        context={'title': 'Accueil'},
    )


def failles_applicatives(request):
    category = Category.objects.get(name='Failles applicatives')
    posts = Post.objects.filter(category=category)
    return render(
        request,
        'category.html',
        context={
            'title': category.name,
            'category': category,
            'posts': posts}
    )


def failles_web(request):
    category = Category.objects.get(name='Failles web')
    posts = Post.objects.filter(category=category)
    return render(
        request,
        'category.html',
        context={
            'title': category.name,
            'category': category,
            'posts': posts}
    )


def scripts(request):
    category = Category.objects.get(name='Scripts')
    posts = Post.objects.filter(category=category)
    return render(
        request,
        'category.html',
        context={
            'title': category.name,
            'category': category,
            'posts': posts}
    )


def actualites(request):
    category = Category.objects.get(name='Actualités')
    posts = Post.objects.filter(category=category)
    return render(
        request,
        'category.html',
        context={
            'title': category.name,
            'category': category,
            'posts': posts}
    )


def post(request, id, name):
    post = Post.objects.get(pk=id)
    return render(
        request,
        'post.html',
        context={
            'title': post.title,
            'post': post},
    )


def error(request):
    return render(
        request,
        'error.html',
        context={'title': 'Erreur'},
    )
