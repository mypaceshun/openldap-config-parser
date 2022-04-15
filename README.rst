openldap-config-parser
======================

.. image:: https://img.shields.io/pypi/pyversions/openldap-config-parser
   :alt: PyPI - Python Version
.. image:: https://badge.fury.io/py/openldap-config-parser.svg
   :target: https://pypi.org/project/openldap-config-parser/
.. image:: https://github.com/mypaceshun/openldap-config-parser/workflows/Test/badge.svg?branch=main&event=push
   :target: https://github.com/mypaceshun/openldap-config-parser/actions/workflows/main.yml
.. image:: https://codecov.io/gh/mypaceshun/openldap-config-parser/branch/main/graph/badge.svg?token=YT631KX1TK
   :target: https://codecov.io/gh/mypaceshun/openldap-config-parser

Repository
----------

https://github.com/mypaceshun/openldap-config-parser

Documentation
-------------

https://mypaceshun.github.io/openldap-config-parser

Install
-------

::

  python3 -m pip install openldap-config-parser

Command Usage
-------------

::

  $ slapd-parser --help
  Usage: slapd-parser [OPTIONS] TARGET

    TARGET      parse target file

  Options:
    --version   Show the version and exit.
    -h, --help  Show this message and exit.

  $ slapd-parser test.slapd.conf
  [16:45:11] run script                                                                                                           command.py:24
             SlapdConfig(global_conig={'include': [['/opt/osstech/etc/openldap/schema/core.schema'],                              command.py:26
             ['/opt/osstech/etc/openldap/schema/cosine.schema'], ['/opt/osstech/etc/openldap/schema/nis.schema'],                              
             ['/opt/osstech/etc/openldap/schema/inetorgperson.schema'], ['/opt/osstech/etc/openldap/schema/misc.schema'],                      
             ['/opt/osstech/etc/openldap/schema/ppolicy.schema']], 'moduleload': [['ppolicy']], 'password-hash': [['{CRYPT}']],                
             'password-crypt-salt-format': [['"$5$%.16s"']], 'attributeoptions': [['lang-', 'phonetic']], 'sortvals':                          
             [['memberUid', 'member', 'host']], 'access': [['to', 'dn.exact=""', 'attrs=supportedSASLMechanisms', 'by', '*',                   
             'none'], ['to', 'dn.subtree=""', 'by', '*', 'read']]}, databases=[Database(type='bdb', config={'suffix':                          
             [['"dc=example,dc=com"']], 'rootdn': [['"cn=master,dc=example,dc=com"']], 'monitoring': [['on']], 'dbconfig':                     
             [['set_data_dir', '.'], ['set_lg_dir', '.']], 'index': [['objectClass', 'eq'], ['modifyTimestamp', 'eq'], ['cn',                  
             'eq,sub']], 'limits': [['dn="uid=user,dc=example,dc=com"', 'time=unlimited', 'size=unlimited']], 'access': [['to',                
             '*', 'by', 'dn="uid=user,dc=example,dc=com"', 'manage', 'by', '*', 'break'], ['to', 'attrs=userPassword', 'by',                   
             'self', '=wx', 'by', 'anonymous', 'auth', 'by', '*', 'none'], ['to', '*', 'by', '*', 'none']], 'overlay':                         
             [['syncprov']], 'syncprov-checkpoint': [['128', '5']], 'syncprov-sessionlog': [['128']], 'serverID': [['1']],                     
             'syncrepl': [['rid=1', 'provider="ldap://ldap.example.com/"', 'type=refreshAndPersist',                                           
             'binddn="cn=slave,dc=example,dc=com"', 'credentials="xxxxx"']], 'mirrormode': [['on']]}), Database(type='monitor',                
             config={'access': [['to', '*', 'by', 'dn="uid=user,dc=example,dc=com"', 'read', 'by', '*', 'none']]})])

Library Usage
-------------

::

  from openldap_config_parser.parser import parse
  from openldap_config_parser.config import SlapdConfig

  result = parse("slapd.conf")
  assert isinstance(result, SlapdConfig)
