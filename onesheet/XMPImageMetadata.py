#!/usr/bin/python
# -*- coding: UTF-8 -*-
from onesheet import CRSMetadata, XMPMetadata, PhotoshopMetadata, AUXMetadata
from abc import ABCMeta

class XMPImageMetadata(XMPMetadata, PhotoshopMetadata, CRSMetadata, AUXMetadata, metaclass=ABCMeta):
    pass
