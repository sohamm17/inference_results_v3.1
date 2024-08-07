# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import annotations

import os

from code.common.constants import *
from code.common.systems.base import *
from code.common.systems.accelerator import AcceleratorConfiguration, GPU, MIG
from code.common.systems.cpu import CPUConfiguration, CPU
from code.common.systems.memory import MemoryConfiguration
from code.common.systems.systems import SystemConfiguration
from code.common.systems.known_hardware import *


custom_systems = dict()


# Do not manually edit any lines below this. All such lines are generated via scripts/add_custom_system.py

###############################
### START OF CUSTOM SYSTEMS ###
###############################
custom_systems['igx_orin_igpu'] = SystemConfiguration(host_cpu_conf=CPUConfiguration(layout={CPU(name="Cortex-A78AE", architecture=CPUArchitecture.aarch64, core_count=4, threads_per_core=1): 1}), host_mem_conf=MemoryConfiguration(host_memory_capacity=Memory(quantity=56.106956, byte_suffix=ByteSuffix.GB), comparison_tolerance=0.05), accelerator_conf=AcceleratorConfiguration(layout={GPU(name="Orin (nvgpu)", accelerator_type=AcceleratorType.Integrated, vram=None, max_power_limit=None, pci_id="[N/A]", compute_sm=87): 1}), numa_conf=None, system_id="igx_orin_colossus")
custom_systems['IGX_Orin_dGPU'] = SystemConfiguration(host_cpu_conf=CPUConfiguration(layout={CPU(name="Cortex-A78AE", architecture=CPUArchitecture.aarch64, core_count=4, threads_per_core=1): 1}), host_mem_conf=MemoryConfiguration(host_memory_capacity=Memory(quantity=56.106199999999994, byte_suffix=ByteSuffix.GB), comparison_tolerance=0.05), accelerator_conf=AcceleratorConfiguration(layout={GPU(name="NVIDIA RTX A6000", accelerator_type=AcceleratorType.Discrete, vram=Memory(quantity=47.98828125, byte_suffix=ByteSuffix.GiB), max_power_limit=300.0, pci_id="0x223010DE", compute_sm=86): 1}), numa_conf=None, system_id="IGX_Orin_dGPU")


###############################
#### END OF CUSTOM SYSTEMS ####
###############################
