# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-controller -*-
# Copyright (c) 2017 - dsanchez <dsanchez@localhost>

"""
.. controller:: Items
    :platform: Linux
    :synopsis: Items endpoints

.. controllerauthor:: dsanchez <dsanchez@localhost>
"""
from mamba.web.response import Ok, BadRequest
from mamba.application import route
from mamba.application import controller

from application.model.item import Item
from application.lib.items_manager import ItemsManager


class Items(controller.Controller):
    """
    Items endpoints
    """

    name = 'Items'
    __route__ = 'items'

    def __init__(self):
        """
        Put your initialization code here
        """
        super(Items, self).__init__()

    @route('/')
    def root(self, request, **kwargs):
        try:
            items = Item.lookup_list()
            return Ok([{'id': i.id, 'name': i.name} for i in items])
        except Exception as e:
            return BadRequest('Internal error: {}'.format(unicode(e)))

    @route('/deferred')
    def root_deferred(self, request, **kwargs):
        d = ItemsManager.lookup_items()
        d.addCallback(lambda items: Ok([{'id': i.id, 'name': i.name} for i in items]))
        d.addErrback(lambda e: BadRequest('Internal error: {}'.format(unicode(e))))
        return d

    @route('/', method='POST')
    def create(self, request, **kwargs):
        print dir(request)
        name = kwargs.get('name', None)

        if not name:
            return BadRequest('Name not filled')

        try:
            return Ok('{}'.format(Item.upsert(name=unicode(name))))
        except Exception as e:
            return BadRequest('Internal error: {}'.format(unicode(e)))
