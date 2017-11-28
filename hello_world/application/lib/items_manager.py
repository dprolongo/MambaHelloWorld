from twisted.internet import defer

from application.model.item import Item


class ItemsManager(object):
    @staticmethod
    @defer.inlineCallbacks
    def upsert_item_with_name(name):
        d = yield Item.upsert(name)
        defer.returnValue(d)

    @staticmethod
    @defer.inlineCallbacks
    def lookup_items(*args, **kwargs):
        d = yield Item.lookup_list(*args, **kwargs)
        defer.returnValue(d)
