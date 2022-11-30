# coding=utf-8
import csv
import json
import os
import time
import unittest
from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from uuid import uuid4
# from elasticsearch import Elasticsearch
from loguru import logger
import settings
from mark import BASE_DIR


class TestBulkIngestES(unittest.TestCase):
    def test_es_ping(self):
        """
        测试 es 是否联通
        python -m unittest testing.test_es_ddl.TestBulkIngestES.test_es_ping
        """
        from database.es.models import create_index, delete_index, es
        print(es.ping())
        # delete_index()

    def test_0_craete_index(self):
        """
        批量创建 dna 文件
        python -m unittest es_tests.TestES.test_0_craete_index
        """
        from database.es.models import create_index, delete_index
        create_index()

