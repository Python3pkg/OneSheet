__author__ = 'California Audio Visual Preservation Project'
from abc import ABCMeta
from onesheet.ClassFileMetadata import FileMetadata

class FileObject(FileMetadata, metaclass=ABCMeta):
    def __init__(self, filename):
        FileMetadata.__init__(self, filename)