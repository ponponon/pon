from typing import Optional
from loguru import logger
from pon.events.entrance import event_handler


class DNACreateService:
    name = 'dna_create_service'

    @event_handler(source_service='ye', event_name='take')
    def auth(self, src_dna: str, content_type: Optional[str] = None) -> int:
        logger.debug(f'src_dna: {src_dna}')

    @event_handler(source_service='ye', event_name='to_decode')
    def decode(self, src_dna: str) -> int:
        logger.debug(f'src_dna: {src_dna}')


class SampleSearchService:
    name = 'sample_search_service'

    @event_handler(source_service='ye', event_name='take')
    def search(self, url: str) -> str:
        logger.debug(f'url: {url}')
