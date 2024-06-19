import torch

from deephedge.instruments.underlying import Underlying

class BrownianStock(Underlying):

    def __init__(self):
        super().__init__()

    def simulate(self):
        S = torch.randn(1)

        self.register_buffer('spot', S)

