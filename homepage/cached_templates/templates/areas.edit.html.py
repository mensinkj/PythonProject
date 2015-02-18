# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423498697.022567
_enable_loop = True
_template_filename = '/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Projects/Sprint-1/homepage/templates/areas.edit.html'
_template_uri = 'areas.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        area = context.get('area', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Edit Area')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        area = context.get('area', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t<h3>Edit Area:</h3>\n\t\n\t<form method="POST">\n\t\t<table>\n\t\t\t')
        __M_writer(str( form ))
        __M_writer('\n\t\t</table>\n\t\t<button class="btn btn-success" type="submit">Save</button>\n\t\t<a class="btn btn-danger" href="/homepage/areas.delete/')
        __M_writer(str( area.photographablething_ptr_id ))
        __M_writer('">Delete Event</a>\n\t\t<a class="btn btn-default" href="/homepage/areas/">Cancel</a>\n\t</form>\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "areas.edit.html", "filename": "/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Projects/Sprint-1/homepage/templates/areas.edit.html", "line_map": {"65": 5, "27": 0, "38": 1, "73": 5, "74": 11, "75": 11, "76": 14, "77": 14, "43": 3, "83": 77, "53": 3, "59": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
