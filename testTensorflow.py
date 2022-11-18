import tensorflow as tf
import torch

print("torch version",torch.__version__)
print("tensorflow version", tf.__version__)
print("tf gpu", tf.test.is_gpu_available())

torch.ones(1)+ torch.ones(1)