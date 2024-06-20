from abc import ABC, abstractmethod

from deephedge.instruments.basestock import BaseStock

import torch

class Derivative(ABC):

    underlying: BaseStock

    def simulate(self):
        self.underlying.simulate()


class EuropeanCall(Derivative):

    def __init__(self, underlying: BaseStock, strike: float):
        self.underlying = underlying
        self.strike = strike

    def payoff(self):
        return torch.max(self.underlying.spot - self.strike, torch.tensor(0.0))




