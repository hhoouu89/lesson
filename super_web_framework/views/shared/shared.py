from patterns.сreational_patterns import Engine, Logger
from patterns.behavioral_patterns import EmailNotifier, SmsNotifier, \
    TemplateView, ListView, CreateView, BaseSerializer


site = Engine()
logger = Logger('main')
routes = {}
email_notifier = EmailNotifier()
sms_notifier = SmsNotifier()
