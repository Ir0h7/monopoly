from app.game import (
    StartField, ChanceField, PrisonField, CasinoField, PoliceField, TaxField,
    MonopolyField, CarField, UnbelievableXXXField, Player)

field_types = {
    'Start': StartField,
    'Chance': ChanceField,
    'Prison': PrisonField,
    'Casino': CasinoField,
    'Police': PoliceField,
    'Luxury': TaxField,
    'Declaration': TaxField,
    'Monopoly': MonopolyField,
    'Car': CarField,
    'XXX': UnbelievableXXXField
}

labels = {
    'Start': tuple(['{} Получает {}, потому что остановился на стартовом поле']),
    'Chance': tuple(['{} хз']),
    'Prison': tuple(['{} Посещает тюрьму с визитом']),
    'Casino': tuple(['{} Получает шанс испытать свою удачу в казино']),
    'Police': tuple(['{} Отпправляется в тюрьму']),
    'Luxury': tuple(['{} Должен заплатить налог на роскошь в размере {}']),
    'Declaration': tuple(['{} Задолжал налоговой {}']),
    'Monopoly': ('{} оказывается на поле {} и может купить его за {} или выставить на аукцион',
                 '{} Посещает своё поле',
                 '{} Посещает заложенное поле игрока {}',
                 '{} Посещает поле игрока {} и должен заплатить ему {}'),
    'Car': ('{} оказывается на поле {} и может купить его за {} или выставить на аукцион',
            '{} Посещает своё поле',
            '{} Посещает заложенное поле игрока {}',
            '{} Посещает поле игрока {} и должен заплатить ему {}'),
    'XXX': ('{} оказывается на поле {} и может купить его за {} или выставить на аукцион',
            '{} Посещает своё поле',
            '{} Посещает заложенное поле игрока {}',
            '{} Посещает поле игрока {} и должен заплатить ему {}')
}

fields = (
    ('Monopoly', None, 'Adidas', 1000, 600, 500, (60, 300, 900, 2700, 4000, 5500), 500, 0),
    ('Monopoly', None, 'Puma', 1000, 600, 500, (60, 300, 900, 2700, 4000, 5500), 500, 0),
    ('Monopoly', None, 'Lacoste', 1200, 720, 600, (80, 400, 1000, 3000, 4500, 6000), 500, 0),
    ('Monopoly', None, 'Вконтакте', 1400, 840, 700, (100, 500, 1500, 3500, 6250, 7500), 750, 1),
    ('Monopoly', None, 'Facebook', 1400, 840, 700, (100, 500, 1500, 3500, 6250, 7500), 750, 1),
    ('Monopoly', None, 'Twitter', 1600, 960, 800, (120, 600, 1800, 5000, 7000, 9000), 750, 1)
)

move_types = {
    'roll': Player.move,
    'purchase': Player.purchase_field,
    'pledge': Player.pledge_field,
    'redemption': Player.redemption_field,
    'rent': 0,
    'tax': 0
}