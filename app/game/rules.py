from fields import (
    StartField, ChanceField, PrisonField, CasinoField, PoliceField, TaxField,
    MonopolyField, CarField, UnbelievableXXXField)

field_types = {
    'Start': StartField,
    'Chance': ChanceField,
    'Prison': PrisonField,
    'Casino': CasinoField,
    'Police': PoliceField,
    'Tax': TaxField,
    'Monopoly': MonopolyField,
    'Car': CarField,
    'XXX': UnbelievableXXXField
}

fields = (
    ('Monopoly', None, 'Adidas', 1000, 600, 500, (60, 300, 900, 2700, 4000, 5500), 500, 0),
    ('Monopoly', None, 'Puma', 1000, 600, 500, (60, 300, 900, 2700, 4000, 5500), 500, 0),
    ('Monopoly', None, 'Lacoste', 1200, 720, 600, (80, 400, 1000, 3000, 4500, 6000), 500, 0),
    ('Monopoly', None, 'Вконтакте', 1400, 840, 700, (100, 500, 1500, 3500, 6250, 7500), 750, 1),
    ('Monopoly', None, 'Facebook', 1400, 840, 700, (100, 500, 1500, 3500, 6250, 7500), 750, 1),
    ('Monopoly', None, 'Twitter', 1600, 960, 800, (120, 600, 1800, 5000, 7000, 9000), 750, 1)
)
