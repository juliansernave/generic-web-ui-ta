# src/core/builder.py
from __future__ import annotations

from dataclasses import dataclass

from faker import Faker

fake = Faker()


@dataclass
class CheckoutInfo:
    first_name: str
    last_name: str
    postal_code: str


def build_checkout_info() -> CheckoutInfo:
    # Keep it simple & stable for demo purposes
    return CheckoutInfo(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        postal_code=fake.postcode(),
    )
