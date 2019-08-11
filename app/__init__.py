# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

#################
#### imports ####
#################

from flask import Flask

################
#### config ####
################

app = Flask(__name__, instance_relative_config=True)

####################
#### blueprints ####
####################

from app.mods.mod_main.views import main_blueprint

# register the blueprints
app.register_blueprint(main_blueprint)
