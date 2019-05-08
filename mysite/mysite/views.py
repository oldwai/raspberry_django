# encoding: utf-8
"""
@version: python3.6
@Software: PyCharm
@File Name: views.py

@__author__: frank 
@contact: leihua_cao@sui.com
@site: NONE
@Time: 2019/5/8 20:29
"""
from django.shortcuts import render


def test(request):
    import socket

    print("您当前的主机名为" + socket.gethostname())
    hostip = socket.gethostbyname(socket.gethostname())
    print("您当前的IP地址为" + socket.gethostbyname(socket.gethostname()))
    return render(request, hostip)