# controller_server.py
# genx control server
# docs: http://flask.pocoo.org/
# quickstart: http://flask.pocoo.org/docs/quickstart/#quickstart
# to get files: os.root_path

# celery bootstrapping (for pro multitasking):
# to start the server: $ celery -A controller_server.celery worker


from celery import Celery

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# from flask_appconfig import AppConfig
from flask_wtf import Form, RecaptchaField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required


# straight from the wtforms docs:
class TelephoneForm(Form):
    country_code = IntegerField('Country Code', [validators.required()])
    area_code = IntegerField('Area Code/Exchange', [validators.required()])
    number = TextField('Number')


class ExampleForm(Form):
    field1 = TextField('First Field', description='This is field one.')
    field2 = TextField('Second Field', description='This is field two.',
                       validators=[Required()])
   fileName = FileField()


    hidden_field = HiddenField('You cannot see this', description='Nope')
    recaptcha = RecaptchaField('A sample recaptcha field')
    radio_field = RadioField('This is a radio field', choices=[
        ('head_radio', 'Head radio'),
        ('radio_76fm', "Radio '76 FM"),
        ('lips_106', 'Lips 106'),
        ('wctr', 'WCTR'),
    ])
    checkbox_field = BooleanField('This is a checkbox',
                                  description='Checkboxes can be tricky.')

    # subforms
    mobile_phone = FormField(TelephoneForm)

    # you can change the label as well
    office_phone = FormField(TelephoneForm, label='Your office phone')

    submit_button = SubmitField('Submit Form')

    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')


def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
    app.config.update(
	    CELERY_BROKER_URL='redis://localhost:6379',
	    CELERY_RESULT_BACKEND='redis://localhost:6379'
	)
    
    Bootstrap(app)
    celery = make_celery(app)

    # in a real app, these should be configured through Flask-Appconfig
    # app.config['SECRET_KEY'] = 'devkey'
    # app.config['RECAPTCHA_PUBLIC_KEY'] = \
    #     '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

    @app.route('/')
    def index():
        form = ExampleForm()
        form.validate_on_submit() #to get error messages to the browser
        return render_template('index.html', form=form)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
