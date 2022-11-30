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
from mark import BASE_DIR
from pathlib import Path
import yaml
from typing import Dict

TESTING_BASE_DIR = Path(__file__).resolve().parent


class TestEnvParse(unittest.TestCase):
    def test_parse_yaml_with_env(self):
        """
        测试 es 是否联通
        python -m unittest testing.test_env.TestEnvParse.test_parse_yaml_with_env
        """
        from pon.events import EventletEventRunner

        config_filepath = TESTING_BASE_DIR/'config.yaml'

        with open(config_filepath, 'r', encoding='utf-8') as f:
            config: Dict[str, Dict] = yaml.safe_load(f)

        logger.debug(config)
