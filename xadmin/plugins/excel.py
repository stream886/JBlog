# coding:utf-8

import xadmin
from xadmin.views import BaseAdminPlugin,ListAdminView
from django.template import loader
from xadmin.plugins.utils import get_context_dict


# excel导入插件
class ListImportExcelPlugin(BaseAdminPlugin):
    import_excel = False
    templates_path = ""

    def init_request(self, *args, **kwargs):
        return bool(self.import_excel)

    def block_top_toolbar(self, context, nodes):
        context.update({
            "templates_path": self.templates_path
        })
        nodes.append(loader.render_to_string('xadmin/excel/model_list.top_toolbar.import.html',context=get_context_dict(context)))

xadmin.site.register_plugin(ListImportExcelPlugin,ListAdminView)