from sonic_platform_base.sonic_thermal_control.thermal_manager_base import ThermalManagerBase
from . import thermal_infos
from . import thermal_conditions
from . import thermal_actions


class ThermalManager(ThermalManagerBase):
    @classmethod
    def initialize(cls):
        """
        Initialize thermal manager, including register thermal condition types and thermal action types
        and any other vendor specific initialization.
        :return:
        """
        return True

    @classmethod
    def deinitialize(cls):
        """
        Destroy thermal manager, including any vendor specific cleanup. The default behavior of this function
        is a no-op.
        :return:
        """
        return True
