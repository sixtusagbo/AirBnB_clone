#!/usr/bin/python3
"""
Initialize module models in this package
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
