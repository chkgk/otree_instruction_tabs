from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['question_1', 'question_2']

    def error_message(self, values):
        if not values['question_1']:
            return 'Please read the instructions again.'
        if not values['question_2']:
            return 'Please read the question again.'

class Results(Page):
    pass


page_sequence = [MyPage, Results]
