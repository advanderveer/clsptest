import pytest

from cdv.test import setup as setup_test
from clsptest.piggybank import (
    create_piggybank
)

class TestSomething:
    @pytest.fixture(scope="function")
    async def setup(self):
        network, alice, bob = await setup_test()
        await network.farm_block()
        yield network, alice, bob

    async def make_and_spend_piggybank(self, network, alice, bob):
        await network.farm_block(farmer=alice)

    @pytest.mark.asyncio
    async def test_valid_contribution(self, setup):
        network, alice, bob = setup
        try:
            await self.make_and_spend_piggybank(network, alice, bob)
        finally:
            await network.close()
