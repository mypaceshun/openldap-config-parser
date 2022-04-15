from openldap_config_parser.config import SlapdConfig


def test_config():
    s = SlapdConfig()
    s.add_database("bdb")
    s.add_directive({"directive": "key1", "args": ["value"]})
    s.add_directive({"directive": "key2", "args": ["value", "value2"]}, 0)
    assert isinstance(s.get_database(), dict)
    assert s.get_database_no("bdb") == 0
    assert s.get_value("key1", -1)[0] == ["value"]
    assert s.get_value("key1", 0)[0] == ["value"]
    assert s.get_value("key2", 0)[0] == ["value", "value2"]
