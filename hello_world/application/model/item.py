# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-model -*-
# Copyright (c) 2017 - dsanchez <dsanchez@localhost>

"""
.. model:: Item
    :plarform: Linux
    :synopsis: None

.. modelauthor:: dsanchez <dsanchez@localhost>
"""

# it's better if you remove this star import and import just what you
# really need from mamba.enterprise
from mamba.enterprise import Int, Unicode
from mamba.application import model


class Item(model.Model):
    """
    None
    """

    __storm_table__ = 'item_table'
    
    id = Int(primary=True, unsigned=True)
    name = Unicode(allow_none=False)

    @classmethod
    def upsert(cls, name):
        item = Item.find(
            Item.name == name,
            async=False
        ).one()
        if not item:
            item = Item()
            item.name = name
            item.create(async=False)
        return True

    @classmethod
    def lookup_list(cls):
        store = cls.database.store()
        return store.find(Item)
