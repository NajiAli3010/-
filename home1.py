import cirq

def create_oracle_circuit(qubits):
    circuit = cirq.Circuit()

    circuit.append(cirq.X(qubits[3]).controlled_by(*qubits[:3]))

    circuit.append(cirq.measure(qubits[3], key='result'))

    return circuit

def main():
    qubits = cirq.LineQubit.range(4)

    oracle_circuit = create_oracle_circuit(qubits)

    print("Oracle Circuit:")
    print(oracle_circuit)

    simulator = cirq.Simulator()
    result = simulator.run(oracle_circuit)

    print("\nMeasurement Result:")
    print(result.measurements['result'])

if __name__ == "__main__":
    main()