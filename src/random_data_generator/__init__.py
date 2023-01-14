import logging

LOGGING_FORMAT_STRING = (
    "%(asctime)s %(levelname)-1s [%(name)s] [%(filename)s:%(lineno)d] %(message)s"
)

# Root level basic logging integrations
logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT_STRING)

# specific logging integrations
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(LOGGING_FORMAT_STRING))
producer_logger = logging.getLogger(__name__)
producer_logger.addHandler(console_handler)
inner_logger = logging.getLogger("random_data_generator.peer_payouts.payments")
inner_logger.propagate = False
inner_logger.addHandler(console_handler)
