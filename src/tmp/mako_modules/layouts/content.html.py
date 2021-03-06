# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1350461785.671
_enable_loop = True
_template_filename = u'E:\\workspacePY\\let\\src/views/layouts/content.html'
_template_uri = u'/layouts/content.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = ['body']


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
    return runtime._inherit_from(context, u'/layouts/base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        is_logged_in = context.get('is_logged_in', UNDEFINED)
        def body_content():
            __M_caller = context.caller_stack._push_frame()
            try:
                next = context.get('next', UNDEFINED)
                __M_writer = context.writer()
                # SOURCE LINE 13
                __M_writer(u'\n\t\t\t\t\t')
                # SOURCE LINE 14
                __M_writer(unicode(next.body()))
                __M_writer(u'\n\t\t\t\t')
                return ''
            finally:
                context.caller_stack._pop_frame()
        current_user = context.get('current_user', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n\t')
        # SOURCE LINE 6
        runtime._include_file(context, u'/shared/flash_messages.html', _template_uri)
        __M_writer(u'\n\t<div id="wrap" role="main">\n\t\t')
        # SOURCE LINE 8
        runtime._include_file(context, u'/shared/header.html', _template_uri)
        __M_writer(u'\n\t\t<div class="clear"></div>\n\t\t<div id="main">\n\t\t\t<div id="content">\n\t\t\t\t<div id="content-inner">\n\t\t\t\t')
        # SOURCE LINE 15
        __M_writer(u'\n\t\t\t\t')
        # SOURCE LINE 16
        __M_writer(unicode(body_content()))
        __M_writer(u'\n\t\t\t\t</div>\n')
        # SOURCE LINE 18
        if is_logged_in :
            # SOURCE LINE 19
            __M_writer(u'\t\t\t\t<ul>\n')
            # SOURCE LINE 20
            if current_user['roletype']==2 :
                # SOURCE LINE 21
                __M_writer(u'\t\t\t\t\t<li class="main">\n\t\t\t\t\t\t\t<a href="#">\u8fd0\u8425\u5546</a>\n\t\t\t\t\t\t<ul>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="../manage">\u67e5\u8be2\u7528\u6237</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="../custorm_add">\u6dfb\u52a0\u7528\u6237</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="../pwdchange">\u5bc6\u7801\u91cd\u7f6e</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="../bwstat">\u7edf\u8ba1</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</li>\n')
                # SOURCE LINE 38
            elif  current_user['roletype']==3 :
                # SOURCE LINE 39
                __M_writer(u'\t\t\t\t\t<li class="main">\n\t\t\t\t\t\t<a href="#">\u7528\u6237</a>\n\t\t\t\t\t\t<ul>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="../product">\u4fe1\u606f\u67e5\u8be2</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="../pwdchange">\u5bc6\u7801\u91cd\u7f6e</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</li>\n')
                # SOURCE LINE 50
            else:
                # SOURCE LINE 51
                __M_writer(u'\t\t\t\t\t<li class="main">\n\t\t\t\t\t\t<a href="#">\u7cfb\u7edf\u7ba1\u7406</a>\n\t\t\t\t\t\t<ul>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="../get_admin">\u7ba1\u7406\u5458\u7ba1\u7406</a>\n\t\t\t\t\t\t\t</li>  \n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="../get_users">\u8fd0\u8425\u5546\u7ba1\u7406</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="../signup">\u6dfb\u52a0\u89d2\u8272</a>\n\t\t\t\t\t\t\t</li> \n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="../pwdchange">\u5bc6\u7801\u91cd\u7f6e</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</li>\n')
            # SOURCE LINE 69
            __M_writer(u'\t\t\t\t</ul>\n')
        # SOURCE LINE 71
        __M_writer(u'\t\t\t</div>\n\t\t</div>\n\t</div>\n\t\n\t\n\t\n\t')
        # SOURCE LINE 77
        runtime._include_file(context, u'/shared/footer.html', _template_uri)
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


