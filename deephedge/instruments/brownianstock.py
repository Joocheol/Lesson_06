import torch

from deephedge.instruments.basestock import BaseStock

class BrownianStock(BaseStock):

    def __init__(self):
        super().__init__()

    def simulate(self):
        S = torch.randn(1)

        self.register_buffer('spot', S)

