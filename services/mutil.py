from typing import Optional
from werkzeug.exceptions import HTTPException
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response
from eventlet import wsgi
import eventlet
from pon.web.entrance import http
from loguru import logger
from pon.events.entrance import event_handler
from pon.events.hints import (
    Message,
    Property,
    Header,
)
from typing import Union
import time


class DNACreateService:
    name = 'dna_create_service'

    @event_handler(source_service='ye', event_name='take')
    def auth(
        self, data: str,
        message: Message,
        content_type: Optional[str] = Property(),
        content_encoding: Optional[str] = Property(),
        delivery_mode: int = Property(),
        track_uuid: Optional[str] = Header(),
        retry_count: Optional[int] = Header(),
        priority: Optional[int] = Property()
    ) -> int:
        logger.debug(f'src_dna: {data}')
        logger.debug(content_type)
        logger.debug(content_encoding)
        logger.debug(track_uuid)
        logger.debug(f'delivery_mode: {delivery_mode}, {type(delivery_mode)}')
        logger.debug(f'retry_count: {retry_count}, {type(retry_count)}')
        logger.debug(f'priority: {priority}')
        time.sleep(5)
        logger.debug(message.ack())

    # @http(methods=['GET'], url='/')
    # def upload(
    #     self,
    # ):
    #     return Response(
    #         'hello world!对吧'
    #     )
