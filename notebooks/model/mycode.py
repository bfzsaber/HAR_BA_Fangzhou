import torch
from LatencyMeasurer import LatencyMeasurer
import PowerMeasurer
from TinyHAR_Model import TinyHAR_Model

def main(input_shape):
    # Define the path to the pre-trained model and input shape
    loadPath = "/home/bian/finn/notebooks/HAR/Run_logs/logs/DSADS1/cv_5/final_best_vali.pth"


    # TO DO:
    num_classes = 19
    num_channels =45
    windowsize = 125
    input_shape =(1, 1, windowsize, num_channels)
    print(input_shape)

    model = TinyHAR_Model(input_shape = input_shape,
                      number_class = num_classes,
                      filter_num = 20,
                      cross_channel_interaction_type = "attn",
                      cross_channel_aggregation_type = "FC",
                      temporal_info_interaction_type = "conv",
                      temporal_info_aggregation_type = "tnaive")


    # Load the model
    model.load_state_dict(torch.load(loadPath), strict=False)
    model.eval()

    # Get the truncated output from forward_truncated1
    truncated_input = model.forward_truncated1(torch.rand(input_shape))

    # Measure latency on CPU
    model = model.cpu()
    measurer = LatencyMeasurer(model)
    cpu_latency = measurer.measure_latency_CPU(input_shape)
    cpu_finn_latency = measurer.measure_CPU_latency_finn(model.forward_truncated2, truncated_input.shape)
    print(f"cpu latency for quantized TinyHAR: {cpu_latency}s,\nfinn part latency: {cpu_finn_latency}s")

    # Measure latency on GPU
    model = model.cuda()
    measurer = LatencyMeasurer(model)
    gpu_latency = measurer.measure_GPU_latency(input_shape)
    gpu_finn_latency = measurer.measure_GPU_finn_latency(model.forward_truncated2, truncated_input.shape)
    print(f"gpu latency for quantized TinyHAR: {gpu_latency}s,\nfinn part latency: {gpu_finn_latency}s")

    # Measure power consumption on GPU
    gpu_power = PowerMeasurer.measure_gpu_power(model, input_shape)
    gpu_power_finn = PowerMeasurer.measure_gpu_finn_power(model, model.forward_truncated2, truncated_input.shape)
    print(f"gpu power consumption for quantized TinyHAR: {gpu_power}W,\nfinn part latency: {gpu_power_finn}W")

if __name__ == "__main__":
    input_shape = (1, 1, 125, 45)
    main(input_shape)