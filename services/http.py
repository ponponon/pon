from loguru import logger
from pon.events.entrance import event_handler
from pon.web.entrance import http
import eventlet
from eventlet import wsgi
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException

class FileService:
    name = 'file_service'

    @http(methods=['GET'], url='/')
    def upload(
        self,
    ):
        return Response(
            'hello world!对吧'
        )

    @http(methods=['GET'], url='/hi')
    def read(
        self,
    ):
        return Response(
            'hello world!'
        )


class MonitorService:
    name = 'monitor_service'

    @http(methods=['GET'], url='/monitor')
    def upload(
        self,
    ):
        return Response(
            '监控你'
        )
