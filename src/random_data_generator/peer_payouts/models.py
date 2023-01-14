from enum import Enum, EnumMeta
from uuid import UUID

import numpy as np
from pydantic import BaseModel


class RandomPayout(EnumMeta):
    @property
    def random(cls):
        return np.random.choice(list(cls.__members__.values()), p=[0.8, 0.2])


class PayoutStatus(Enum, metaclass=RandomPayout):
    success = "success"
    fail = "fail"


class Payout(BaseModel):
    id: UUID
    timestamp: float  # for Unix time
    amount: float
    status: PayoutStatus
    currency: str = "EUR"
    sender_nickname: str
    recipient_nickname: str | None = None
