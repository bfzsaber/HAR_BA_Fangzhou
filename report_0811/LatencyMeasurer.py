import time
import psutil
import torch

class LatencyMeasurer:
    def __init__(self, model):
        self.model = model
        self.model.eval()

    def measure_GPU_latency(self, inputs_shape, n=200):
        if not next(self.model.parameters()).is_cuda:
            raise ValueError("The model is not on the GPU. Please move it to the GPU using model.cuda().")
        return self._measure_latency(self.model, inputs_shape, n, gpu=True)

    def measure_GPU_finn_latency(self, method, inputs_shape, n=200):
        if not next(self.model.parameters()).is_cuda:
            raise ValueError("The model is not on the GPU. Please move it to the GPU using model.cuda().")
        return self._measure_latency(method, inputs_shape, n, gpu=True)

    def measure_latency_CPU(self, inputs_shape, n=100):
        return self._measure_latency(self.model, inputs_shape, n, gpu=False)

    def measure_CPU_latency_finn(self, method, inputs_shape, n=100):
        return self._measure_latency(method, inputs_shape, n, gpu=False)

    def _measure_latency(self, method, inputs_shape, n, gpu=False):
        total_latency = 0
        process = psutil.Process()

        warmup_inputs = torch.randn(inputs_shape).float()
        if gpu:
            warmup_inputs = warmup_inputs.cuda()

        # Warm up
        for _ in range(min(10, n)):
            with torch.no_grad():
                _ = method(warmup_inputs)
            if gpu:
                torch.cuda.synchronize()

        # Measure latency
        for _ in range(n):
            test_inputs = torch.randn(inputs_shape).float()
            if gpu:
                test_inputs = test_inputs.cuda()
            start = time.time()
            with torch.no_grad():
                _ = method(test_inputs)
            if gpu:
                torch.cuda.synchronize()
            end = time.time()
            total_latency += (end - start)

        average_latency = total_latency / n
        return average_latency
