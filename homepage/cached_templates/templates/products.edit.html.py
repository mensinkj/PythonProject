# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423377128.261262
_enable_loop = True
_template_filename = '/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Projects/Sprint-1/homepage/templates/products.edit.html'
_template_uri = 'products.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'title', 'admin_bar']


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
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def admin_bar():
            return render_admin_bar(context._locals(__M_locals))
        product = context.get('product', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'admin_bar'):
            context['self'].admin_bar(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        product = context.get('product', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t<h3>Edit Item:</h3>\n\t\n\t<form method="POST">\n\t\t<table>\n\t\t\t')
        __M_writer(str( form ))
        __M_writer('\n\t\t</table>\n\t\t<button class="btn btn-success" type="submit">Save</button>\n\t\t<a class="btn btn-danger" href="/homepage/products.delete/')
        __M_writer(str( product.photographablething_ptr_id ))
        __M_writer('">Delete Item</a>\n\t\t<a class="btn btn-default" href="/homepage/products/">Cancel</a>\n\t</form>\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Edit Product')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_admin_bar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def admin_bar():
            return render_admin_bar(context)
        __M_writer = context.writer()
        __M_writer('\n<div id="admin_bar">\n\t<ul>\n\t\t<li><a href="/users">Users</a></li>\n\t\t<li><a href="/products">Products</a></li>\n\t\t<li><a href="/items">Items</a></li>\n\t\t<li><a href="/organizations">Organizations</a></li>\n\t\t<li><a href="/events">Events</a></li>\n\t\t<li><a href="/areas">Areas</a></li>\n\t</ul>\n</div> \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Projects/Sprint-1/homepage/templates/products.edit.html", "source_encoding": "ascii", "line_map": {"96": 5, "68": 18, "69": 24, "70": 24, "71": 27, "72": 27, "45": 3, "78": 3, "40": 1, "50": 16, "84": 3, "90": 5, "27": 0, "60": 18, "102": 96}, "uri": "products.edit.html"}
__M_END_METADATA
"""