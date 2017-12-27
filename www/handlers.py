#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from coroweb import get, post
from models import User

@get('/')
def index(request):
    users = yield from User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }


