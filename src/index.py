from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:", f"Mehuvarasto: {mehua}", f"Olutvarasto: {olutta}")


    print("Virhetilanteita:Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print(f"Olutvarasto: {olutta}","olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Olutvarasto: {olutta}","olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")


if __name__ == "__main__":
    main()
