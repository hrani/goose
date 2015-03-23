from abc import ABCMeta, abstractmethod

class Model(QObject, metaclass=ABCMeta):

    def __init__(self, moose):
        self.moose = moose
        # self.root

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def setsolver(self, solver):
        pass

    @abstractmethod
    def getsolver(self):
        pass

    @abstractmethod
    def enable(self):
        raise NotImplementedError("Implement code to enable simulation of this model.")

    @abstractmethod
    def disable(self):
        raise NotImplementedError("Implement code to disable simulation of this model.")

    @abstractmethod
    def load(self, source, target):
        raise NotImplementedError("Implement code to disable simulation of this model.")

    def simulate(self):
        pass

    def run(self, time):
        self.moose.run(time)

    def pause(self):
        pass

    def reset(self):
        self.moose.reinit()

    def clear(self):
        pass

    def element(self):
        pass

    def find(self):
        pass

class ElectricalModel(Model):
    def __init__(self, source, target, moose):

class NeuroMlModel(ElectricalModel)
    def type(self):
        return NEUROML_1_8

class ChemicalModel(Model):
    def __init__(self, moose, source, target=None):
        pass

class GenesisModel(ChemicalModel):
    def __init__(self, moose, source, target=None):
        pass

class SbmlModel(ChemicalModel):
    def __init__(self, moose, source, target=None):
        pass

class CspaceModel(ChemicalModel):
    def __init__():
        pass
