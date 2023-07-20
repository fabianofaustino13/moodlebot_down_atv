"""
Base plugin
"""
import pluginlib


class PluginBase:
    def __str__(self):
        return f"{self.__class__.__name__} - {self.__doc__.strip()}"


@pluginlib.Parent("actions")
class ActionPlugin(PluginBase):
    """Classe base para os plugins de ação."""

    @pluginlib.abstractmethod
    def handle(self, page, context):
        raise NotImplementedError


@pluginlib.Parent("checks")
class CheckPlugin(PluginBase):
    """Classe base para os plugins de verificação."""

    @pluginlib.abstractmethod
    def handle(self, page, context):
        raise NotImplementedError
