#!/usr/bin/python
# -*- coding: utf-8 -*-

from environment import *

class HelloWorldEnv(Environment):
    def __init__(self):
        Environment.__init__(self)

    def _execute_action(self, agent_name, action):
        print("Agent %s is doing %s" % (agent_name, action));
        self._add_percept(None)
        self._clear_perceptions()

        print(str(action))
        eval(str(action))

def aloha():
    print('Aloha HelloWorldEnv!')

def mahalo(argument):
    print('Mahaloing with %s' + argument)