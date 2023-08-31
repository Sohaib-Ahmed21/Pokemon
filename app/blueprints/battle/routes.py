#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

import requests
from flask import render_template

from . import battle

BASE_URL = "https://api.pokemontcg.io/v2/cards?q=name:gardevoir"


@battle.route("/battlefield")
def battlefield():
    response = requests.get(BASE_URL)
    data = response.json()
    cards = data["data"][:3]  # Get the first 3 cards

    return render_template("battlefield.html", cards=cards)
