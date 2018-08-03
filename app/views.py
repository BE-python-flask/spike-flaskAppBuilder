from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from flask_appbuilder import has_access

from .models import ContactGroup, Contact

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""
from flask_appbuilder import AppBuilder, expose, BaseView
 
class MyView(BaseView):
    # route_base = "/myview"
    default_view = 'hello'

    @expose('/hello/')
    def hello(self):
        return 'Hello World!'
 
    @expose('/message/<string:msg>')
    @has_access
    def message(self, msg):
        msg = 'Hello %s' % (msg)
        return msg

    @expose('/welcome/<string:msg>')
    @has_access
    def welcome(self, msg):
        msg = 'Hello %s' % (msg)
        return self.render_template('index.html',msg = msg)

# appbuilder.add_view_no_menu(MyView())
appbuilder.add_view(MyView, "Hello", category='My View')
appbuilder.add_link("Message", href='/myview/message/john', category='My View')
appbuilder.add_link("Welcome", href='/myview/welcome/student', category='My View')
"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()

class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)

    label_columns = {'contact_group': 'Contacts Group'}
    list_columns = ['name', 'personal_cellphone', 'birthday', 'contact_group']

    show_fieldsets = [
        (
            'Summary',
            {'fields':
                 ['name', 'address', 'contact_group']}
        ),
        (
            'Personal Info',
            {'fields':
                 ['birthday', 'personal_phone', 'personal_cellphone'],
             'expanded':False
             }
        )
    ]


class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]

db.create_all()

appbuilder.add_view(GroupModelView,
                    "List Groups",
                    icon = "fa-address-book-o",
                    category = "Contacts",
                    category_icon = "fa-envelope")
appbuilder.add_view(ContactModelView,
                    "List Contacts",
                    icon = "fa-address-card-o",
                    category = "Contacts")
