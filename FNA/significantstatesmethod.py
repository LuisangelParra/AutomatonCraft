def afdOptimization(TranD, translated_subconjuntos):
    # Optimización del DFA
    # Se eliminan los estados equivalentes

    #Identificar los estados equivalentes en el DFA con translated_subconjuntos
    equivalent_states = []
    for label1, estados1 in translated_subconjuntos.items():
        for label2, estados2 in translated_subconjuntos.items():
            if label1 != label2 and estados1 == estados2:
                if (label2, label1) not in equivalent_states:
                    equivalent_states.append((label1, label2))

    # Eliminar los estados equivalentes del DFA en la TranD
    todelete = []
    for label1, label2 in equivalent_states:
        for key, value in TranD.items():
            if value == label2:
                TranD[key] = label1
            if key[0] == label2:
                todelete.append(key)
    for key in todelete:
        del TranD[key]
    return TranD