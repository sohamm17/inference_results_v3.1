# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_IGPU(MultiStreamGPUBaseConfig):
    system = KnownSystem.igx_orin_igpu

    workspace_size = 30000000000
    multi_stream_expected_latency_ns = 130000000
    gpu_copy_streams = 2
    gpu_batch_size = 2

    # Use early stopping estimate due to long runtime.
    min_duration = 3600000
    min_query_count = 20000
    
    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):

@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_IGPU_Triton(IGX_ORIN_IGPU):
    use_triton = True

    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):

@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_DGPU(MultiStreamGPUBaseConfig):
    system = KnownSystem.IGX_Orin_dGPU

    workspace_size = 30000000000
    multi_stream_expected_latency_ns = 130000000
    gpu_copy_streams = 2
    gpu_batch_size = 2

    # Use early stopping estimate due to long runtime.
    min_duration = 3600000
    min_query_count = 20000
    
@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_DGPU_Triton(IGX_ORIN_DGPU):
    use_triton = True



# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_IGPU(MultiStreamGPUBaseConfig):
    system = KnownSystem.igx_orin_igpu

    workspace_size = 30000000000
    multi_stream_expected_latency_ns = 130000000
    gpu_copy_streams = 2
    gpu_batch_size = 2

    # Use early stopping estimate due to long runtime.
    min_duration = 3600000
    min_query_count = 20000
    
    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):

@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_IGPU_Triton(IGX_ORIN_IGPU):
    use_triton = True

    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):

@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_DGPU(MultiStreamGPUBaseConfig):
    system = KnownSystem.IGX_Orin_dGPU

    workspace_size = 30000000000
    multi_stream_expected_latency_ns = 130000000
    gpu_copy_streams = 2
    gpu_batch_size = 2

    # Use early stopping estimate due to long runtime.
    min_duration = 3600000
    min_query_count = 20000
    
@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_DGPU_Triton(IGX_ORIN_DGPU):
    use_triton = True



@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_ADA6000(MultiStreamGPUBaseConfig):
    system = KnownSystem.IGX_Orin_Ada6000

    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):
    gpu_batch_size: int = 0
    input_dtype: str = ''
    input_format: str = ''
    map_path: str = ''
    multi_stream_expected_latency_ns: int = 0
    multi_stream_samples_per_query: int = 0
    multi_stream_target_latency_percentile: float = 0.0
    precision: str = ''
    tensor_path: str = ''

    # Optional fields:
    active_sms: int = 0
    assume_contiguous: bool = False
    buffer_manager_thread_count: int = 0
    cache_file: str = ''
    complete_threads: int = 0
    deque_timeout_usec: int = 0
    disable_beta1_smallk: bool = False
    energy_aware_kernels: bool = False
    gpu_copy_streams: int = 0
    gpu_inference_streams: int = 0
    instance_group_count: int = 0
    model_path: str = ''
    nms_type: str = ''
    performance_sample_count_override: int = 0
    preferred_batch_size: str = ''
    request_timeout_usec: int = 0
    run_infer_on_copy_streams: bool = False
    use_batcher_thread_per_device: bool = False
    use_cuda_thread_per_device: bool = False
    use_deque_limit: bool = False
    use_graphs: bool = False
    use_jemalloc: bool = False
    use_same_context: bool = False
    use_spin_wait: bool = False
    verbose_glog: int = 0
    warmup_duration: float = 0.0
    workspace_size: int = 0


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_ADA6000_Triton(IGX_ORIN_ADA6000):
    use_triton = True

    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):
    gpu_batch_size: int = 0
    input_dtype: str = ''
    input_format: str = ''
    map_path: str = ''
    multi_stream_expected_latency_ns: int = 0
    multi_stream_samples_per_query: int = 0
    multi_stream_target_latency_percentile: float = 0.0
    precision: str = ''
    tensor_path: str = ''

    # Optional fields:
    active_sms: int = 0
    assume_contiguous: bool = False
    batch_triton_requests: bool = False
    buffer_manager_thread_count: int = 0
    cache_file: str = ''
    complete_threads: int = 0
    deque_timeout_usec: int = 0
    disable_beta1_smallk: bool = False
    energy_aware_kernels: bool = False
    gather_kernel_buffer_threshold: int = 0
    gpu_copy_streams: int = 0
    gpu_inference_streams: int = 0
    instance_group_count: int = 0
    max_queue_delay_usec: int = 0
    model_path: str = ''
    nms_type: str = ''
    num_concurrent_batchers: int = 0
    num_concurrent_issuers: int = 0
    output_pinned_memory: bool = False
    performance_sample_count_override: int = 0
    preferred_batch_size: str = ''
    request_timeout_usec: int = 0
    run_infer_on_copy_streams: bool = False
    use_batcher_thread_per_device: bool = False
    use_concurrent_harness: bool = False
    use_cuda_thread_per_device: bool = False
    use_deque_limit: bool = False
    use_graphs: bool = False
    use_jemalloc: bool = False
    use_same_context: bool = False
    use_spin_wait: bool = False
    verbose_glog: int = 0
    warmup_duration: float = 0.0
    workspace_size: int = 0


