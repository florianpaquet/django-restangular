# -*- coding:utf-8 -*-
from rest_framework.routers import SimpleRouter, Route


class CustomRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing suffixes.
    """
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={
                'get': 'list',
                'post': 'create'
            },
            name='{basename}-list',
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            name='{basename}-detail',
            initkwargs={'suffix': 'Instance'}
        ),
    ]
