# -*- encoding: utf-8 -*-
# -*- mamba-file-type: mamba-controller -*-
# Copyright (c) 2017 - dsanchez <dsanchez@localhost>

"""
.. controller:: Hello
    :platform: Linux
    :synopsis: Say hello

.. controllerauthor:: dsanchez <dsanchez@localhost>
"""

from mamba.web.response import Ok
from mamba.application import route
from mamba.application import controller


class Hello(controller.Controller):
    """
    Say hello
    """

    name = 'Hello'
    __route__ = 'hello'

    def __init__(self):
        """
        Put your initialization code here
        """
        super(Hello, self).__init__()

    @route('/')
    def root(self, request, **kwargs):
        return Ok('I am the Hello, hello world!')

    @route('/<name>')
    def hello(self, request, name, **kwargs):
        return Ok('Hello {}!'.format(name))

