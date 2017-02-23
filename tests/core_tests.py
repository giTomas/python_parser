#!/usr/bin/python

from nose.tools import *
from lexicon.core import scan

def test_direction():
    assert_equal(scan('north'), [('direction', 'north')])
    result = scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(scan('go'), [('verb', 'go')])
    result = scan('Go stop eat')
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'stop'),
                          ('verb', 'eat')])

def test_stops():
    assert_equal(scan('the'), [('stop_word', 'the')])
    result = scan('in of fRom at')
    assert_equal(result, [('stop_word','in'),
                          ('stop_word', 'of'),
                          ('stop_word', 'from'),
                          ('stop_word', 'at')])

def test_nouns():
    assert_equal(scan('doOr'), [('noun', 'door')])
    result = scan('bear princess cabinet')
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess'),
                          ('noun', 'cabinet')])

def test_numbers():
    assert_equal(scan('10'), [('number', 10)])
    result = scan('255 30 990')
    assert_equal(result, [('number', 255),
                          ('number', 30),
                          ('number', 990)])

def test_errors():
    assert_equal(scan('55elat'), [('error', '55elat')])
    result = scan('Of drol cabinet 55lolo')
    assert_equal(result, [('stop_word', 'of'),
                          ('error', 'drol'),
                          ('noun', 'cabinet'),
                          ('error', '55lolo')])
