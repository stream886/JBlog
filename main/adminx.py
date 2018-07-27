import xadmin
from xadmin import views
from xadmin.layout import Main, Side, Row, Fieldset

from xadmin.models import UserSettings
# from xadmin.models import Log
from django.contrib.auth.models import User, Group, Permission

from .models import Category, Tag, Post


# 基础设置
class BaseSetting(object):
    # enable_themes = True #主题选择
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "JBlog后台"
    site_footer = "CJP个人博客"
    menu_style = "accordion"  # 收缩下拉列表
    # 自定义菜单栏
    # def get_site_menu(self):
    #     return [
    #         {
    #             'title': r"主站",
    #             'menus': (
    #                 {
    #                     'title': r"博客首页",
    #                     'url': '/index',
    #                 },
    #             )
    #         }
    #     ]


# 主界面控制
class MainDashboard(object):
    widget_customiz = False
    widgets = [
        [
            {"type": "qbutton", "title": "Quick Start",
             "btns": [{"title": "index", "url": "/index"}]},
        ],
        [
            {"type": "html",
             "title": "公告测试",
             "content": '''
             <h3> Welcome</h3>
             '''},
            {"type": "qbutton", "title": "Quick Start",
             "btns": [{"title": "Awesome", "url": "http://www.fontawesome.com.cn/faicons/"}]},
        ],

    ]


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.website.IndexView, MainDashboard)

xadmin.site.unregister(UserSettings)
# xadmin.site.unregister(Log)
xadmin.site.unregister(User)
xadmin.site.unregister(Group)
xadmin.site.unregister(Permission)


class PostAdmin(object):
    # 图标
    model_icon = 'fa fa-file-text'
    # 分页数量
    list_per_page = 15
    # 显示字段
    list_display = ("title", "author", "category", "tags", "views", "created_time", "modified_time",)
    # 跳转字段
    list_display_links = ("title",)
    # 筛选字段
    list_filter = ("title", "author", "category", "tags", "views", "created_time", "modified_time",)
    # 搜索字段
    search_fields = ("title", "author", "category", "tags",)
    # 表单布局
    form_layout = (
        Main(
            Fieldset(r"基本信息",
                     Row("title", "author"),
                     "excerpt",
                     "body",
                     ),
        ),
        Side(
            Fieldset(r"其他属性",
                     "category", "tags"
                     ),
        )
    )


xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Category)
xadmin.site.register(Tag)
