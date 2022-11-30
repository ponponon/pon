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
from pon.events.hints import Message
from pon.constants import NON_PERSISTENT, PERSISTENT
from utils.time_helpers import get_utc_now_timestamp

_data = """
{
  "clip_result": {
    "id": null,
    "company_id": 1677,
    "track_source_id": 3945,
    "track_source_type": "search",
    "clip_title": "甜心范-教你穿衣打扮,教人穿衣搭配的网站",
    "clip_url": "http://www.tianxinfan.com/",
    "clip_url_hash": "3a0362b5d3d61d536c939a01b915f8d6",
    "author": null,
    "clip_source": "360引擎",
    "publish_date": null,
    "is_parsed": true,
    "parsed_by": "redirect_service",
    "parser": "redirect",
    "priority": 1,
    "skip_filter": true,
    "save_image": true,
    "extra": {}
  },
  "source_results": [
    {
      "id": null,
      "source_url": "http://www.tianxinfan.com/",
      "source_url_hash": "3a0362b5d3d61d536c939a01b915f8d6",
      "source_type": "text",
      "source_media_path": "oss_text_dir/3a/d6/3a0362b5d3d61d536c939a01b915f8d6.txt",
      "content": "雅娴 2018-11-05小编说 如果有留意自己的皮肤状态，会发现到了25岁，细纹一夜之间爬上了你的脸。就连笑起来都变的不自信了，不用你也不用怕，小琪琪还是贴心的给你们找了好物，快来看看吧。 不过我最近听说了珀莱雅经过多 …",
      "is_persisted": false
    }
    ]
}
""".strip()

data = json.loads(_data)


class TestMessagePush(unittest.TestCase):
    def test_message_push_standalone(self):
        """

        python -m unittest testing.test_rabbitmq_event.TestMessagePush.test_message_push_standalone
        """
        from pon.standalone.events import event_dispatcher

        config = {
            'amqp_uri': f'amqp://{settings.RABBITMQ_CONFIG.username}:'
            f'{settings.RABBITMQ_CONFIG.password}@{settings.RABBITMQ_CONFIG.host}:'
            f'{settings.RABBITMQ_CONFIG.port}/{settings.RABBITMQ_CONFIG.vhost}',
        }

        logger.debug(config)

        dispatch_event = event_dispatcher(
            config['amqp_uri'], delivery_mode=PERSISTENT)

        for i in range(1000000):
            dispatch_event(
                'ye',
                'take',
                data,
                priority=9
            )
