from twisted.internet import defer

from application.model.item import Item


class ItemsManager(object):
    @staticmethod
    @defer.inlineCallbacks
    def lookup_items():
        d = yield Item.lookup_list()
        defer.returnValue(d)
