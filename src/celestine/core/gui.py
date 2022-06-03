import abc


class Window(abc.ABC):
    @abc.abstractmethod
    def close(self):
        raise NotImplementedError

    @abc.abstractmethod
    def start(self):
        raise NotImplementedError

    @abc.abstractmethod
    def watch(self):
        raise NotImplementedError
