import logging
import time
from typing import Callable

import click
from kafka import KafkaProducer

from random_data_generator.peer_payouts.payments import PayoutProvider

log = logging.getLogger(__name__)


def random_payout():
    return PayoutProvider().create_payout().json()


def produce_data(data_generator: Callable, bootstrap_servers: list[str], topic_name: str, timeout: int) -> None:
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        json_data = data_generator()
        producer.send(topic_name, bytes(f"{json_data}", "UTF-8"))
        log.info(f"Payment data is sent: {json_data}")
        time.sleep(1)
    log.info(f"The producer has produced for {timeout} seconds. Now shutting down.")
    producer.close()


@click.group(name="redpanda")
def rpk_cli():
    """Commands related to Redpanda"""
    pass


@rpk_cli.command(name="payouts")
@click.option(
    "--server",
    default="redpanda:9092",
    help="Bootstrap servers for redpanda",
)
@click.option(
    "--topic",
    default="mock-payments",
    help="The topic that you would like to send data to...",
)
@click.option(
    "--timeout",
    default=300,
    help="Timeout parameter for the mock data producer, as in seconds...",
)
def produce_payouts(server, topic, timeout):
    produce_data(data_generator=random_payout, bootstrap_servers=[server], topic_name=topic, timeout=timeout)
