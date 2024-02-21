# from flask import Blueprint
#
# bp = Blueprint("game", __name__)

from game_object import (
    PurchasedField,
    StartField, ChanceField, PrisonField, CasinoField, PoliceField, TaxField,
    MonopolyField, CarField, UnbelievableXXXField,
    Player)
from app.game.game import Game
