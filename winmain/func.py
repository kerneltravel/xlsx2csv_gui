# -*- coding: utf-8 -*-

def isanum(str):
    try:
        float(str);
        return True;
    except ValueError:
        return False;
