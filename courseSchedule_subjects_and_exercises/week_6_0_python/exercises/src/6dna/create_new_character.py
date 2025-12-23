import random
import sys


def generate_dna_sequence(str_counts, min_gap=50, max_gap=150):
    """
    Generates a realistic DNA sequence with the specified STRs.

    Args:
        str_counts: Dictionary with STRs and their counts
        min_gap: Minimum size of random sequence between STRs
        max_gap: Maximum size of random sequence between STRs

    Returns:
        String with the complete DNA sequence
    """

    # DNA Bases
    bases = ["A", "C", "G", "T"]

    # Start with random sequence
    dna_parts = []
    initial_length = random.randint(200, 500)
    dna_parts.append("".join(random.choice(bases) for _ in range(initial_length)))

    # Add each STR with its repetitions.
    for str_seq, count in str_counts.items():
        # Add random sequence between STRs
        gap_length = random.randint(min_gap, max_gap)
        gap_sequence = "".join(random.choice(bases) for _ in range(gap_length))
        dna_parts.append(gap_sequence)

        # Add the repeated STR
        dna_parts.append(str_seq * count)

    # Add final random sequence
    final_length = random.randint(200, 500)
    dna_parts.append("".join(random.choice(bases) for _ in range(final_length)))

    return "".join(dna_parts)


def save_to_file(sequence, filename):
    with open(filename, "w") as f:
        f.write(sequence)
    print(f"✓ Sequência salva em: {filename}")
    print(f"  Tamanho: {len(sequence)} bases")


def main():

    print("=" * 60)
    print("CRIADOR DE SEQUÊNCIA DE DNA PERSONALIZADA")
    print("=" * 60)

    # Define the STRs and counts for Edmar Radanovis
    edmar_strs = {
        "AGATC": 20,
        "TTTTTTCT": 15,
        "AATG": 25,
        "TCTAG": 30,
        "GATA": 35,
        "TATC": 40,
        "GAAA": 45,
        "TCTG": 50,
    }

    # Generate the sequence
    print("\nGerando sequência de DNA para Edmar Radanovis...")
    print("\nContagens de STRs:")
    for str_seq, count in edmar_strs.items():
        print(f"  {str_seq}: {count} repetições")

    dna_sequence = generate_dna_sequence(edmar_strs)

    # Save to file
    output_file = "sequences/edmar.txt"
    save_to_file(dna_sequence, output_file)

    # Generate a line for the CSV as well.
    print("\n" + "=" * 60)
    print("PARA ADICIONAR AO ARQUIVO large.csv:")
    print("=" * 60)

    # Order of STRs as per large.csv
    str_order = ["AGATC", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]
    counts_ordered = [str(edmar_strs[str_seq]) for str_seq in str_order]
    csv_line = f"Edmar Radanovis,{','.join(counts_ordered)}"

    print(f"\nAdicione esta linha ao final do arquivo databases/large.csv:\n")
    print(f"{csv_line}")

    print("\n" + "=" * 60)
    print("PARA TESTAR:")
    print("=" * 60)
    print(f"\nApós adicionar a linha ao CSV, execute:")
    print(f"  python dna.py databases/large.csv sequences/edmar.txt")
    print(f"\nSaída esperada: Edmar Radanovis")


def create_custom_character():
    """Function to create a completely customized character.."""

    print("\n" + "=" * 60)
    print("CRIAR PERSONAGEM PERSONALIZADO")
    print("=" * 60)

    name = input("\nNome do personagem: ").strip()
    if not name:
        name = "Novo Personagem"

    available_strs = [
        "AGATC",
        "TTTTTTCT",
        "AATG",
        "TCTAG",
        "GATA",
        "TATC",
        "GAAA",
        "TCTG",
    ]

    str_counts = {}
    print(f"\nDigite o número de repetições para cada STR (1-100):")

    for str_seq in available_strs:
        while True:
            try:
                count = int(input(f"  {str_seq}: "))
                if 1 <= count <= 100:
                    str_counts[str_seq] = count
                    break
                else:
                    print("    Por favor, digite um número entre 1 e 100")
            except ValueError:
                print("    Por favor, digite um número válido")

    print(f"\nGerando sequência de DNA para {name}...")
    dna_sequence = generate_dna_sequence(str_counts)

    filename = f"sequences/{name.replace(' ', '_').lower()}.txt"
    save_to_file(dna_sequence, filename)

    counts_ordered = [str(str_counts[str_seq]) for str_seq in available_strs]
    csv_line = f"{name},{','.join(counts_ordered)}"

    print("\n" + "=" * 60)
    print("LINHA PARA O CSV:")
    print("=" * 60)
    print(f"\n{csv_line}")

    return name, filename, csv_line


if __name__ == "__main__":
    print("=" * 60)
    print("CRIADOR DE PERSONAGENS DE DNA - CS50 DNA")
    print("=" * 60)

    while True:
        print("\nOpções:")
        print("  1. Criar sequência para Edmar Radanovis (pré-definido)")
        print("  2. Criar personagem personalizado")
        print("  3. Sair")

        choice = input("\nEscolha (1-3): ").strip()

        if choice == "1":
            main()
            break
        elif choice == "2":
            name, filename, csv_line = create_custom_character()

            # Ask if they want to test it now.
            test = input("\nDeseja testar agora? (s/n): ").lower()
            if test == "s":
                print("\n" + "=" * 60)
                print("INSTRUÇÕES PARA TESTAR:")
                print("=" * 60)
                print(f"\n1. Adicione esta linha ao databases/large.csv:")
                print(f"   {csv_line}")
                print(f"\n2. Execute:")
                print(f"   python dna.py databases/large.csv {filename}")
                print(f"\n3. Saída esperada: {name}")
            break
        elif choice == "3":
            print("\nAté logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
