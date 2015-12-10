from __future__ import division
from random import randint
from progressbar import ProgressBar, Bar, ETA, ReverseBar
from time import sleep


def percent(percent, whole):
    return (percent * whole) / 100.0


def chance(percent):
    return randint(0, 100) in [x for x in xrange(percent)]


def ask(question, default=u'Yes'):
    yes = ["yes", "Y"]
    if default == 'Yes':
        yes.append("")
    return raw_input(question + ': ').title() in yes


def delay(seconds=1, widgets=None):
    bar = ProgressBar(widgets=widgets) if widgets else ProgressBar()
    for i in bar(xrange(100)):
        sleep(seconds)