# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423374368.233776
_enable_loop = True
_template_filename = '/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Projects/Sprint-1/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'admin_bar', 'sidebar', 'rightbar', 'title']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        def admin_bar():
            return render_admin_bar(context._locals(__M_locals))
        def rightbar():
            return render_rightbar(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        auth = context.get('auth', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def sidebar():
            return render_sidebar(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html lang="en">\n  <meta charset="UTF-8">\n  <head>\n    \n    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer(' - Colonial Heritage Foundation</title>\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n')
        __M_writer('\t<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">  \n\t\n')
        __M_writer('\t<link rel="icon" type="image/x-icon" href="/static/homepage/media/favicon.ico" />\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  \n  <body onload="getCurrentPath()">\n  \n    <div id="header">\n    \t<h1>Colonial Heritage Foundation</h1>\n    </div>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'admin_bar'):
            context['self'].admin_bar(**pageargs)
        

        __M_writer('\n  \t<div class="container">\n  \t\t<!-- use bootstrap grid -->\t\n\t\t<div class="row">\n\t\t\t<!-- side bar -->\n\t\t\t<div class="col-sm-2">\n\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sidebar'):
            context['self'].sidebar(**pageargs)
        

        __M_writer('\n\t\t\t</div>\n\t\t\t<!-- Main Content -->\n\t\t\t<div class="col-sm-8">\n\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\t\t\t</div>\n\t\t\t<!-- Right Login Sidebar -->\n\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'rightbar'):
            context['self'].rightbar(**pageargs)
        

        __M_writer('\n\t\t</div>\n\t</div>  \n\t\n\t<div id="footer">\n\t\t<p><span class="glyphicon glyphicon-copyright-mark"></span> Jameson Ricks 2015 - \n\t\t<span class="browser-time"><script>$(\'.browser-time\').text(new Date());</script></span><p>\n\t</div>\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n </body>\n  \n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t\t  Site content goes here in sub-templates.\n\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_admin_bar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def admin_bar():
            return render_admin_bar(context)
        auth = context.get('auth', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\t\t')

        if auth:
          context.write('<div id="admin_bar"><ul><li><a href="/users/">Users</a></li><li><a href="/products/">Products</a></li><li><a href="/items/">Items</a></li><li><a href="/organizations/">Organizations</a></li><li><a href="/events/">Events</a></li><li><a href="/areas/">Areas</a></li></ul></div> ')
        
        
        __M_writer('\n\t\t\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sidebar():
            return render_sidebar(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t\t<ul class="nav nav-pills nav-stacked top-padding">\n\t\t\t\t  <li id="home"><a href="/">Home</a></li>\n\t\t\t\t  <li id="about"><a href="/about">About</a></li>\n\t\t\t\t  <li id="contact"><a href="/contact">Contact</a></li>\n\t\t\t\t  <li id="terms"><a href="/terms">Terms<span class="badge pull-right">2</span></a></li>\n\t\t\t\t</ul>\n\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_rightbar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        auth = context.get('auth', UNDEFINED)
        def rightbar():
            return render_rightbar(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t\t<div class="col-sm-2">\n\t\t\t\t\t<div class="login_info">\n\t\t\t\t\t\t')

        if not auth:
                context.write('<p>Volunteers, <br>Login Here:</p><a type="button" class="btn btn-primary" href="/login">Login</a>')
        else:
                context.write('<p>Logged in as ' + user.first_name + '</p><a type="button" class="btn btn-primary" href="/logout/">Logout</a>')
        
        
        __M_writer('\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/jamesonricks/Dropbox/School/Winter 2015/IS 413 - Enterprise application development/Projects/Sprint-1/homepage/templates/base.htm", "uri": "base.htm", "line_map": {"64": 52, "115": 45, "69": 58, "135": 61, "136": 64, "74": 72, "75": 82, "76": 82, "77": 82, "143": 69, "16": 4, "18": 0, "83": 56, "149": 12, "89": 56, "103": 34, "95": 31, "160": 149, "37": 2, "38": 4, "39": 5, "104": 34, "43": 5, "109": 37, "48": 12, "49": 14, "50": 16, "51": 19, "52": 22, "53": 22, "54": 22, "121": 45, "59": 39, "102": 31, "127": 61}}
__M_END_METADATA
"""
