# -*- coding: utf-8 -*-
'''
Pcs Command Wrapper
========================

The pcs command is wrapped for specific functions

:depends: pcs
'''
from __future__ import absolute_import

# Import python libs
import os

# Import salt libs
import salt.utils


def __virtual__():
    '''
    Only load if pcs is installed
    '''
    if salt.utils.which('pcs'):
        return 'pcs'
    return False


def auth(nodes, pcsuser='hacluster', pcspasswd='hacluster', extra_args = []):
    '''
    Authorize nodes

    CLI Example:

    .. code-block:: bash

        salt '*' pcs.auth nodes='[ node1.example.org node2.example.org ]' \\
                          pcsuser='hacluster' \\
                          pcspasswd='hacluster' \\
                          extra_args=[ '--force' ]
    '''
    cmd = [ 'pcs',  'cluster',  'auth'  ]

    if pcsuser:
      cmd +=  [ '-u', pcsuser ]

    if pcspasswd:
      cmd +=  [ '-p',  pcspasswd ]

    cmd += extra_args
    cmd += nodes

    return __salt__['cmd.run_all'](cmd, output_loglevel='trace', python_shell=False)

def is_auth(nodes):
    '''
    Check if nodes are already authorized

    CLI Example:

    .. code-block:: bash

        salt '*' pcs.is_auth nodes='[ node1.example.org node2.example.org ]' 
    '''
    cmd = [ 'pcs',  'cluster',  'auth'  ]
    cmd += nodes

    return __salt__['cmd.run_all'](cmd, stdin='\n\n', output_loglevel='trace', python_shell=False)

def cluster_setup(nodes, pcsclustername='pcscluster', extra_args = []):
    '''
    Setup pacemaker cluster via pcs

    CLI Example:

    .. code-block:: bash

        salt '*' pcs.cluster_setup nodes='[ node1.example.org node2.example.org ]' \\
                                   pcsclustername='pcscluster', \\
                                   extra_args=[ '' ]
    '''
    cmd = [ 'pcs',  'cluster',  'setup'  ]

    cmd += [ '--name', pcsclustername ]

    cmd += nodes
    cmd += extra_args

    return __salt__['cmd.run_all'](cmd, output_loglevel='trace', python_shell=False)

def config_show():
    '''
    Show config of cluster

    CLI Example:

    .. code-block:: bash

        salt '*' pcs.config_show 
    '''
    cmd = [ 'pcs',  'config',  'show'  ]

    return __salt__['cmd.run_all'](cmd, output_loglevel='trace', python_shell=False)
