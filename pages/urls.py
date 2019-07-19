#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 13:13:53 2019

@author: a49w
"""

from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name = 'index'),
        path('about', views.about, name = 'about')
        
]