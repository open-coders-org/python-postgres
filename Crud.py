from abc import ABC, abstractmethod


class Crud(ABC):
    @abstractmethod
    def crear(self, **kwargs):
        pass

    @abstractmethod
    def mostrar(self, **kwargs):
        pass

    @abstractmethod
    def eliminar(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def mostrarId(self, **kwargs):
        pass

    @abstractmethod
    def editar(self, **kwargs):
        pass

    @abstractmethod
    def eliminar(self, **kwargs):
        pass
