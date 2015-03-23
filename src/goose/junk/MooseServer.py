import moose

class MooseService(SlaveService):
    exposed_runtime = 0.0
    exposed_minruntime = 0.0
    def exposed_load(filename):
        pass

    def exposed_simulate(n):
        moose.start()

    def exposed_stop(n):
        moose.reinit()


def main():
    pass
