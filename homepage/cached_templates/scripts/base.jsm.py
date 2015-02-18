# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421290074.098685
_enable_loop = True
_template_filename = '/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Homework/test_dmp/homepage/scripts/base.jsm'
_template_uri = 'base.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        currentPage = context.get('currentPage', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("$(function() {\n\t// update the time every n seconds\n\twindow.setInterval(function() {\n\t\t$('.browser-time').text(new Date());\n\t}, 1000);\n\n\t// update button\n    $('#server-time-button').click(function() {\n      $('.server-time').load('/homepage/index.gettime');\n    });\n});\n\n//set active page by id\nfunction getCurrentPath() \n{ \n\t$(")
        __M_writer(str( currentPage ))
        __M_writer(").addClass('active');\n}")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Homework/test_dmp/homepage/scripts/base.jsm", "line_map": {"16": 0, "24": 16, "30": 24, "22": 1, "23": 16}, "uri": "base.jsm", "source_encoding": "ascii"}
__M_END_METADATA
"""
