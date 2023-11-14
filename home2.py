import cirq
def create_balanced_circuit(qubits):
    circuit = cirq.Circuit()

    circuit.append(cirq.X(qubits[3]))

    circuit.append(cirq.H.on_each(*qubits))

    circuit.append(cirq.X(qubits[3]))

    circuit.append(cirq.H.on_each(qubits[0], qubits[1], qubits[2]))

    circuit.append(cirq.X(qubits[3]).controlled_by(*qubits[:3]))

    circuit.append(cirq.H.on_each(qubits[0], qubits[1], qubits[2]))

    circuit.append(cirq.measure(*qubits, key='result'))

    return circuit

def create_const_circuit(qubits):
    circuit = cirq.Circuit()

    circuit.append(cirq.X(qubits[3]))

    circuit.append(cirq.H.on_each(*qubits))

    circuit.append(cirq.X(qubits[3]))

    circuit.append(cirq.H.on_each(*qubits))

    circuit.append(cirq.measure(*qubits, key='result'))

    return circuit

def deutsch_jozsa_algorithm(oracle_circuit):
    qubits = list(oracle_circuit.all_qubits())

    deutsch_circuit = cirq.Circuit(cirq.H(q) for q in qubits)

    deutsch_circuit.append(oracle_circuit)

    deutsch_circuit.append(cirq.H(q) for q in qubits)

    simulator = cirq.Simulator()
    result = simulator.simulate(deutsch_circuit)

    measurement_result = int(round(result.final_state[-1]))

    return measurement_result




def main():
    qubits = cirq.LineQubit.range(4)

    balanced_circuit = create_balanced_circuit(qubits)

    const_circuit = create_const_circuit(qubits)

    print("Balanced Oracle Circuit:")
    print(balanced_circuit)

    print("\nConst Oracle Circuit:")
    print(const_circuit)

    simulator = cirq.Simulator()
    result_balanced = simulator.run(balanced_circuit)
    measurement_result_balanced = result_balanced.measurements['result']
    print("\nFinal Result (Balanced Oracle):", measurement_result_balanced)

    result_const = simulator.run(const_circuit)
    measurement_result_const = result_const.measurements['result']
    print("Final Result (Const Oracle):", measurement_result_const)

if __name__ == "__main__":
    main()


