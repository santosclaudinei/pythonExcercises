# Crie as seguintes classes com suas determinadas carcteristicas
# ram, hd, processador

# Agora, crie a classe Placa_mae, que deve ser composta pelos 3 itens acima

# Por fim, utilizando herança, crie dispositivos que utilizam a placa mãe;
# por exemplo: computador


class MemoryRam:
    def __init__(self, capacidade: float, tipo_ram: str, cache: float):
        self.capacidade = capacidade
        self.tipo_ram = tipo_ram
        self.cache = cache


    def __repr__(self):
        return "<cap: {}, type {}, freq {}, cache {}>".format(self.capacidade, self.tipo_ram,
        self.cache)


def create_ram_obj_() -> MemoryRam:
    capacidade_m = int(input("Informe a capacidade da memoria [2GB / 4GB / 8GB / 16GB]: "))
    tipo_ram = str(input("Informe o tipo da RAM [DDR3 / DDR4 / DDR5]: "))
    cache = int(input("Informe o tamanho da cache [3MB / 4MB / 6MB / 8MB / 12MB]: "))

    return MemoryRam(capacidade=capacidade_m, tipo_ram=tipo_ram, cache=cache)


class HardDisk:
    def __init__(self, capacidade, interface_comunicacao):
        self.capacidade = capacidade
        self.cache = interface_comunicacao


    def __repr__(self):
        return (f"{self.capacidade}, {self.interface_comunicacao}")
        # return "<cap: {}, type {}, freq {}, cache {}>".format(self.capacidade, self.tipo_hd,
        #                                                       self.velocidade, self.interface_comunicacao)


def create_hd_obj_() -> HardDisk:
    capacidade_hd = int(input("Informe o tamanho do armazenameno [500GB / 1TB / 2TB / 5TB]: "))
    interface_comunicacao = str(input("Informe o tipo de interface desejada: [ATA / SATA I / SATA II / SATA III"))


class Processor:
    def __init__(self, modelo_processor, capacidade_proc, tipo_cache):
        self.modelo_processor = modelo_processor
        self.capacidade_proc = capacidade_proc
        self.tipo_cache = tipo_cache


    def __repr__(self):
        return (f"{self.modelo_processor}, {self.capacidade_proc}, {self.tipo_cache}")


def create_proc_obj_() -> Processor:
    modelo_proc = str(input("Informe o modelo do processador [Core i3 / Core i5 / Core i7 / Core i9]: "))
    capacidade_proc = int(input("Informe a quantidade de nucleos [2 / 4 / 6]: "))
    cache = int(input("Informe a capacidade da cache [4MB / 8MB / 12MB]: "))

class MotherBoard(self, MemoryRam, HardDisk, Processor):
    self.marca = marca



if __name__ == "__main__":
    while True:
        escolha = int(input(
            """Escolha o produto dentre as opções abaixo:
            1 - Escolher Memoria RAM
            2 - Escolher Disco Rigido
            3 - Escolher Processador
            0 - Sair\n
            Informe a opção desejada: """))

        if (0 <= escolha <= 3):
            if (escolha ==  1):
                memoria = create_ram_obj_()
            elif (escolha == 2):
                hd = create_hd_obj_()
            elif (escolha == 3):
                processador = create_proc_obj_()
            else:
                print("Agradecemos sua visita a loja. Volte sempre!")
                break

