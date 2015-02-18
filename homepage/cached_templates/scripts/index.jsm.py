# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421286401.97074
_enable_loop = True
_template_filename = '/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Homework/test_dmp/homepage/scripts/index.jsm'
_template_uri = 'index.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer("$(function() {\n\t// update the time every n seconds\n\twindow.setInterval(function() {\n\t\t$('.browser-time').text(new Date());\n\t}, 1000);\n\n\t// update button\n    $('#server-time-button').click(function() {\n      $('.server-time').load('/homepage/index.gettime');\n    });\n});")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "27": 21, "21": 1}, "uri": "index.jsm", "source_encoding": "ascii", "filename": "/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Homework/test_dmp/homepage/scripts/index.jsm"}
__M_END_METADATA
"""
