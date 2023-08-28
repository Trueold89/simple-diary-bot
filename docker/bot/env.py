# -*- coding: utf-8 -*-

import os

def env(env):
    defaults = {
        'TOKEN': 'insert_your_token_here',
        'USERS': "('insert_your_id_here', 'insert_your_id_here', etc.)",
        'LANG': 'ENG'
        }
    try:
        env = os.environ[env]
    except:
        env = defaults.get(env)
    return env
