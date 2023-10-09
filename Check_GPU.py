def checkGPU_Torch():
    """Check if GPU is available and being recpognized For PyTorch"""

    import torch

    # Check if CUDA (GPU) is available
    if torch.cuda.is_available():
        # CUDA is available; you can use GPU acceleration
        device = torch.device("cuda")
        print(f"Using GPU: {torch.cuda.get_device_name(0)}")
    else:
        # CUDA is not available; fallback to CPU
        device = torch.device("cpu")
        print("CUDA is not available; using CPU")

def checkGPU_TensorFlow():
    """For TensorFlow"""

    import tensorflow as tf

    # Check if any GPU devices are available
    gpu_devices = tf.config.experimental.list_physical_devices('GPU')

    if len(gpu_devices) > 0:
        # GPUs are available
        print("Available GPU devices:")
        for gpu in gpu_devices:
            print(f"Device name: {gpu.name}")
    else:
        # No GPUs are available
        print("No GPU devices found. Using CPU for computation.")