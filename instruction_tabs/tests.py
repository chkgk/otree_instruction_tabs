from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield pages.MyPage, {'question_1': True, 'question_2': True}
        yield pages.Results
