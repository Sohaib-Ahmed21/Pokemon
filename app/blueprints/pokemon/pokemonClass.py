#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

from pokemontcgsdk import RestClient, Card

from config import Config


class Pokemonclass:
    RestClient.configure(Config.pokemontcgsdk_api_key)

    @classmethod
    def get_card_by_name(cls, name):
        cards = Card.where(name=name).all()

        if len(cards) > 0:
            return cards[0].__dict__
        return None
