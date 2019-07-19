#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:34:22 2019

@author: a49w
"""

from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name = 'listings'),
        path('<int:listing_id>', views.listing, name = 'listing'),
        path('search', views.search, name = 'search')
        
]