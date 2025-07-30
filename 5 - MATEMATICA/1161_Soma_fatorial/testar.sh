#!/bin/bash

echo "Executando script: sol.py"
time python3 sol.py < arquivo.in > my.sol

echo "-------------------------------------"
echo "Comparando resultados..."

# O -w no diff ignora diferenças de espaços em branco (muito útil!)
if diff -w arquivo.sol my.sol; then
    echo "✅ Accepted: A saída está correta!"
else
    echo "❌ Wrong Answer: A saída está diferente."
    echo ""
    echo "--- Sua Saída (my.sol) ---"
    cat my.sol
    echo ""
    echo "--- Saída Esperada (arquivo.sol) ---"
    cat arquivo.sol
fi