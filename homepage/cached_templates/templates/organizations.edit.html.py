# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423290554.672569
_enable_loop = True
_template_filename = '/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Projects/Sprint-1/homepage/templates/organizations.edit.html'
_template_uri = 'organizations.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['admin_bar', 'content', 'title']


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
        organization = context.get('organization', UNDEFINED)
        def admin_bar():
            return render_admin_bar(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        organization = context.get('organization', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t<h3>Edit Organization:</h3>\n\t<a class="btn btn-success" href="/homepage/organizations.create/">Add Organization</a>\n\t<form method="POST">\n\t\t<table>\n\t\t\t')
        __M_writer(str( form ))
        __M_writer('\n\t\t</table>\n\t\t<button class="btn btn-success" type="submit">Save</button>\n\t\t<a class="btn btn-danger" href="/homepage/organizations.delete/')
        __M_writer(str( organization.photographablething_ptr_id ))
        __M_writer('">Delete Organization</a>\n\t\t<a class="btn btn-default" href="/homepage/organizations/">Cancel</a>\n\t</form>\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Edit Organization')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "organizations.edit.html", "line_map": {"96": 3, "66": 5, "102": 96, "72": 18, "82": 24, "45": 3, "80": 18, "81": 24, "50": 16, "83": 27, "84": 27, "40": 1, "90": 3, "27": 0, "60": 5}, "source_encoding": "ascii", "filename": "/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Projects/Sprint-1/homepage/templates/organizations.edit.html"}
__M_END_METADATA
"""
