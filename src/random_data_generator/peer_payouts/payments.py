import logging
import random
import time
from uuid import uuid4

import numpy as np
from faker import Faker
from faker.generator import Generator
from faker.providers import BaseProvider

from random_data_generator.peer_payouts.models import Payout, PayoutStatus

log = logging.getLogger(__name__)


class PayoutProvider(BaseProvider):
    def __init__(self, outlier_probability: float = 0.15):
        super().__init__(Generator)
        self.outlier_probability = outlier_probability
        self.faker = Faker()
        self.user_pool = [self.faker.user_name() for _ in range(2)]

    def _generate_outlier(self) -> bool:
        return np.random.choice(
            [True, False], 1, p=[self.outlier_probability, 1 - self.outlier_probability]
        )[0]

    def _pick_sender(self) -> str:
        random_sender = self.user_pool.pop(random.randrange(len(self.user_pool)))
        return random_sender

    def _create_payout_amount(self):
        payout_amount = round(random.normalvariate(20, 2), 2)
        if self._generate_outlier():
            log.info("Generating the outlier...")
            payout_amount = round(random.normalvariate(90, 2), 2)
        return payout_amount

    def create_payout(self) -> Payout:
        payload = Payout(
            **{
                "id": uuid4(),
                "timestamp": time.time(),  # now in milliseconds
                "amount": self._create_payout_amount(),
                "status": PayoutStatus.random,
                "sender_nickname": self._pick_sender(),
            }
            # recipients to be defined after the senders' definition
        )
        payload.recipient_nickname = self.user_pool.pop()
        return payload
