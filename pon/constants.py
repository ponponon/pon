AMQP_URI_CONFIG_KEY = 'AMQP_URI'
WEB_SERVER_CONFIG_KEY = 'WEB_SERVER_ADDRESS'
RPC_EXCHANGE_CONFIG_KEY = 'rpc_exchange'
SERIALIZER_CONFIG_KEY = 'serializer'
SERIALIZERS_CONFIG_KEY = 'SERIALIZERS'
ACCEPT_CONFIG_KEY = 'ACCEPT'
HEARTBEAT_CONFIG_KEY = 'HEARTBEAT'
AMQP_SSL_CONFIG_KEY = 'AMQP_SSL'
TRANSPORT_OPTIONS_CONFIG_KEY = 'TRANSPORT_OPTIONS'
LOGIN_METHOD_CONFIG_KEY = 'LOGIN_METHOD'

MAX_WORKERS_CONFIG_KEY = 'max_workers'
PARENT_CALLS_CONFIG_KEY = 'parent_calls_tracked'

DEFAULT_MAX_WORKERS = 10
DEFAULT_PARENT_CALLS_TRACKED = 10
DEFAULT_SERIALIZER = 'json'
DEFAULT_RETRY_POLICY = {'max_retries': 3}
DEFAULT_HEARTBEAT = 60
DEFAULT_TRANSPORT_OPTIONS = {
    'max_retries': 3,
    'interval_start': 2,
    'interval_step': 1,
    'interval_max': 5
}

CALL_ID_STACK_CONTEXT_KEY = 'call_id_stack'
AUTH_TOKEN_CONTEXT_KEY = 'auth_token'
LANGUAGE_CONTEXT_KEY = 'language'
USER_ID_CONTEXT_KEY = 'user_id'
USER_AGENT_CONTEXT_KEY = 'user_agent'

DEFAULT_FRAMEWORK = 'pon'
DEFAULT_FRAMEWORK_GITHUB = 'https://github.com/ponponon/pon'
DEFAULT_PROJECT_NAME = ''

# delivery_mode
HEADER_PREFIX = "pon"
NON_PERSISTENT = 1
PERSISTENT = 2

RABBIT_USER = 'guest'
RABBIT_PASSWORD = 'guest'
RABBIT_HOST = 'localhost'
RABBIT_PORT = 5672
RABBIT_VHOST = '/'
