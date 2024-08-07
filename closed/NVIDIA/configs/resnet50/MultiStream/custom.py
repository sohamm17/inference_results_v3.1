# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_IGPU(MultiStreamGPUBaseConfig):
    system = KnownSystem.igx_orin_igpu

    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):
    gpu_copy_streams = 2
    multi_stream_expected_latency_ns = 2330000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_IGPU_Triton(IGX_ORIN_IGPU):
    use_triton = True

    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):

@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_DGPU(MultiStreamGPUBaseConfig):
    system = KnownSystem.IGX_Orin_dGPU

    gpu_copy_streams = 2
    multi_stream_expected_latency_ns = 2330000

@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class IGX_ORIN_DGPU_Triton(IGX_ORIN_DGPU):
    use_triton = True
