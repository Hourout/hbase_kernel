from ipykernel.kernelapp import IPKernelApp
from .kernel import HbaseKernel


IPKernelApp.launch_instance(kernel_class=HbaseKernel)