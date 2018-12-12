#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../src/')

import os
import tempfile

import pytest
import porradepapp


@pytest.fixture
def client():
    db_fd, porradepapp.app.config['DATABASE'] = tempfile.mkstemp()
    porradepapp.app.config['TESTING'] = True
    client = porradepapp.app.test_client()

    yield client

    os.close(db_fd)
    os.unlink(porradepapp.app.config['DATABASE'])


def test_status(client):
    rv = client.get('/')
    rv2 = client.get('/status')
    json_data = rv.get_json()
    json_data2 = rv2.get_json()
    assert json_data['status']=="OK"
    assert json_data['status']=="OK"

def test_jornada(client):
    rv = client.get('/jornada/1')
    rv2 = client.put('/jornada/1', json={'partido': 'Almeria - Granada',})
    rv3 = client.delete('/jornada/1')
    json_data = rv.get_json()
    json_data2 = rv2.get_json()
    json_data3 = rv3.get_json()
    assert json_data['partidos']!=False
    assert json_data2['partidos']==True
    assert json_data3['partidos']==True

def test_partido(client):
    rv = client.get('/partido/1/jornada/1')
    json_data = rv.get_json()
    assert json_data['partido'] != None

def test_apuesta(client):
    rv = client.get('/apuesta/luis14')
    json_data = rv.get_json()
    assert json_data['apuestas'] != False
