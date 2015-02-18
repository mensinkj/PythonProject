# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423374233.069019
_enable_loop = True
_template_filename = '/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Projects/Sprint-1/homepage/templates/organizations.html'
_template_uri = 'organizations.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        organizations = context.get('organizations', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        organizations = context.get('organizations', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t<h3>Organizations</h3>\n\t\t<a class="btn btn-success" href="/homepage/organizations.create/">Add Organization</a>\n\t<table class="table table-striped table-bordered">\n\t\t<tr>\n\t\t\t<th>Name</th>\n\t\t\t<th>Type</th>\n\t\t\t<th>Actions</th>\n\t\t</tr>\n')
        for organization in organizations:
            __M_writer('\t\t\t<tr>\n\t\t\t\t<td><p>')
            __M_writer(str( organization.given_name ))
            __M_writer('</p></td>\n\t\t\t\t<td><p>')
            __M_writer(str( organization.organization_type ))
            __M_writer('</p></td>\n\t\t\t\t<td><p><a href="/homepage/organizations.edit/')
            __M_writer(str( organization.photographablething_ptr_id ))
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
        __M_writer('Organizations')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Projects/Sprint-1/homepage/templates/organizations.html", "uri": "organizations.html", "line_map": {"64": 19, "65": 19, "66": 20, "59": 6, "68": 23, "37": 1, "42": 3, "80": 3, "67": 20, "52": 6, "86": 80, "74": 3, "27": 0, "60": 16, "61": 17, "62": 18, "63": 18}}
__M_END_METADATA
"""
