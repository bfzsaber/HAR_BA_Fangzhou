import pynvml
import torch

def measure_gpu_power(model, inputs_shape, num_runs=200):
    test_inputs = torch.randn(inputs_shape).float().cuda()
        
    # Initialize NVML
    pynvml.nvmlInit()

    # Get handle for the first GPU
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)

    # Variables to store total power and number of measurements
    total_power = 0.0
    num_measurements = 0

    # Start measuring power just before the prediction
    for _ in range(num_runs):
        power_before = pynvml.nvmlDeviceGetPowerUsage(handle) / 1000.0
        # Run the model prediction
        output = model(test_inputs)
        power_after = pynvml.nvmlDeviceGetPowerUsage(handle) / 1000.0

        total_power += (power_before + power_after) / 2.0
        num_measurements += 1

    # Shutdown NVML
    pynvml.nvmlShutdown()

    # Calculate average power consumption during prediction
    average_power = total_power / num_measurements

    return average_power


def measure_gpu_finn_power(model, method, inputs_shape, num_runs=200):
    test_inputs = torch.randn(inputs_shape).float().cuda()
        
    # Initialize NVML
    pynvml.nvmlInit()

    # Get handle for the first GPU
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)

    # Variables to store total power and number of measurements
    total_power = 0.0
    num_measurements = 0

    # Start measuring power just before the prediction
    for _ in range(num_runs):
        power_before = pynvml.nvmlDeviceGetPowerUsage(handle) / 1000.0
        # Run the model prediction
        output = method(test_inputs)
        power_after = pynvml.nvmlDeviceGetPowerUsage(handle) / 1000.0

        total_power += (power_before + power_after) / 2.0
        num_measurements += 1

    # Shutdown NVML
    pynvml.nvmlShutdown()

    # Calculate average power consumption during prediction
    average_power = total_power / num_measurements

    return average_power