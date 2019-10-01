class Verbosity:

    verbo = False

    @staticmethod
    def show(v):
        if Verbosity.verbo:
            print(v)
