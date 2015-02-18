# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423374232.537733
_enable_loop = True
_template_filename = '/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Projects/Sprint-1/homepage/templates/items.html'
_template_uri = 'items.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'title']


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
        items = context.get('items', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t<h3>Items</h3>\n\t<a class="btn btn-success" href="/homepage/items.create/">Add Item</a>\n\t<table class="table table-striped table-bordered">\n\t\t<tr>\n\t\t\t<th>Name</th>\n\t\t\t<th>Description</th>\n\t\t\t<th>Value</th>\n\t\t\t<th>Rental Price</th>\n\t\t\t<th>Actions</th>\n\t\t</tr>\n')
        for item in items:
            __M_writer('\t\t\t<tr>\n\t\t\t\t<td><p>')
            __M_writer(str( item.name ))
            __M_writer('</p></td>\n\t\t\t\t<td><p>')
            __M_writer(str( item.description ))
            __M_writer('</p></td>\n\t\t\t\t<td><p>')
            __M_writer(str( item.value ))
            __M_writer('</p></td>\n\t\t\t\t<td><p>')
            __M_writer(str( item.standard_rental_price ))
            __M_writer('</p></td>\n\t\t\t\t<td><p><a href="/homepage/items.edit/')
            __M_writer(str( item.photographablething_ptr_id ))
            __M_writer('/">Edit</a></p></td>\n\t\t\t</tr>\n')
        __M_writer('\t</table>\n\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Items')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Projects/Sprint-1/homepage/templates/items.html", "uri": "items.html", "line_map": {"64": 20, "65": 20, "66": 21, "59": 5, "68": 22, "37": 1, "70": 23, "71": 23, "72": 26, "42": 3, "78": 3, "67": 21, "52": 5, "69": 22, "84": 3, "90": 84, "27": 0, "60": 17, "61": 18, "62": 19, "63": 19}}
__M_END_METADATA
"""
