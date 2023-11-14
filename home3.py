import cirq

def oracle_add_one(circuit, qubits):
    circuit.append(cirq.X(qubits[0]))
    circuit.append(cirq.X(qubits[1]))

def oracle_check_equation(circuit, qubits):
    circuit.append(cirq.X(qubits[0]))
    circuit.append(cirq.X(qubits[1]))

    circuit.append(cirq.X(qubits[2]))

def grover_algorithm(oracle_circuit, iterations):
    qubits = list(oracle_circuit.all_qubits())

    grover_circuit = cirq.Circuit(cirq.H(q) for q in qubits)

    diffusion_gate = cirq.H(qubits[0]).controlled_by(*qubits[1:])

    for _ in range(iterations):
        grover_circuit.append(oracle_circuit)

        grover_circuit.append(cirq.H(q) for q in qubits)

        grover_circuit.append(cirq.X(q) for q in qubits)

        grover_circuit.append(diffusion_gate)

        grover_circuit.append(cirq.X(q) for q in qubits)

        grover_circuit.append(cirq.H(q) for q in qubits)

    grover_circuit.append(cirq.measure(*qubits, key='result'))

    return grover_circuit




def main():
    qubits = cirq.LineQubit.range(3)

    oracle_add_one_circuit = cirq.Circuit()
    oracle_add_one(oracle_add_one_circuit, qubits[:2])

    oracle_check_equation_circuit = cirq.Circuit()
    oracle_check_equation(oracle_check_equation_circuit, qubits)

    print("Oracle Circuit for Adding One (mod 4):")
    print(oracle_add_one_circuit)

    print("\nOracle Circuit for Checking x + 1 = 3:")
    print(oracle_check_equation_circuit)

    iterations = 2  
    grover_add_one_circuit = grover_algorithm(oracle_add_one_circuit, iterations)
    print("\nGrover's Algorithm for Adding One (mod 4):")
    print(grover_add_one_circuit)

    iterations = 2 
    grover_check_equation_circuit = grover_algorithm(oracle_check_equation_circuit, iterations)
    print("\nGrover's Algorithm for Checking x + 1 = 3:")
    print(grover_check_equation_circuit)

if __name__ == "__main__":
    main()
