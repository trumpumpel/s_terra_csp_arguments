from conf_mgr_utiltity_class import ConfMgrUtility
import pytest


def test_conf_mgr_add():
    util = ConfMgrUtility("conf_mgr")
    util.run('add', 'key1', 'value1')
    assert util.config['key1'] == 'value1'


def test_conf_mgr_modify():
    util = ConfMgrUtility("conf_mgr")
    util.run('add', 'key1', 'value1')
    util.run('modify', 'key1', 'value2')
    assert util.config['key1'] == 'value2'


def test_conf_mgr_delete():
    util = ConfMgrUtility("conf_mgr")
    util.run('add', 'key1', 'value1')
    util.run('delete', 'key1')
    assert 'key1' not in util.config


def test_conf_mgr_show_all():
    util = ConfMgrUtility("conf_mgr")
    util.run('add', 'key1', 'value1')
    util.run('add', 'key2', 'value2')
    result = util.run('show', '--all')
    assert result == "{'key1': 'value1', 'key2': 'value2'}"
