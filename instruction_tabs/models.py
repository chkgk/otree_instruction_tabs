from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Christian König gen. Kersting'

doc = """
Demonstration of multi-screen instructions on a single oTree Page.
"""


class Constants(BaseConstants):
    name_in_url = 'instruction_tabs'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_1 = models.BooleanField(
        label="Did you read the instructions?",
        widget=widgets.RadioSelect,
        choices=[[True, 'Absolutely!'],
                 [False, 'Nope']],
    )

    question_2 = models.BooleanField(
        label="How about this?",
        widget=widgets.RadioSelect,
        choices=[[True, 'Absolutely!'],
                 [False, 'Nope']],
    )
