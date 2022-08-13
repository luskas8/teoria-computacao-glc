from glc import GLC

def start():
    G = GLC()
    print(G.createWordWithNSymbols(n=6))
    print(G.appendNotEnds("teste"))

if __name__ == "__main__":
    start()