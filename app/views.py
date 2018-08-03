from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from flask_appbuilder import has_access

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


