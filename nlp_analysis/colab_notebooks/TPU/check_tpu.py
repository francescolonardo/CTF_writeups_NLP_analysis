import torch_xla
import torch_xla.core.xla_model as xm

# Prints XLA devices
print(xm.xla_device())
