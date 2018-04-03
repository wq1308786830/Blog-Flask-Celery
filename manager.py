#!/usr/bin/env python
# -*- coding: utf-8 -*-

from application import create_app

__author__ = 'Russell'

if __name__ == '__main__':
    app = create_app()
    app.run(host="127.0.0.1", port=7000)
