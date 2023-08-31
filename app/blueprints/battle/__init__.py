#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
from flask import Blueprint

battle = Blueprint("battle", __name__, template_folder="battle_templates")

from . import routes
