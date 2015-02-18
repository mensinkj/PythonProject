# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421293239.993866
_enable_loop = True
_template_filename = '/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Homework/test_dmp/homepage/templates/contact.html'
_template_uri = 'contact.html'
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
        def title():
            return render_title(context._locals(__M_locals))
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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t<h3>Contact Us</h3>\n\t<form>\n\t\tName:<br />\n\t\t<input type="text" name="name"/><br /><br />\n\t\tEmail:<br />\n\t\t<input type="text" name="email"/><br /><br />\n\t\tMessage:<br />\n\t\t<textarea name="message" rows="10" cols="40"></textarea><br /><br />\n\t\t<input class="btn btn-success" type="submit" value="Submit"/>\n\t</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Contact')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"75": 69, "51": 5, "36": 1, "69": 3, "57": 5, "41": 3, "27": 0, "63": 3}, "filename": "/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Homework/test_dmp/homepage/templates/contact.html", "uri": "contact.html"}
__M_END_METADATA
"""
