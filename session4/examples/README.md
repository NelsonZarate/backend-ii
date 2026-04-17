# Exemplo: multiprocessing + multithreading

Este exemplo demonstra a combinação de múltiplos processos (para paralelismo CPU-bound e isolamento) com threads internas (para operações I/O-bound). Útil para padrões como: servidor por processo + threads para I/O, pipelines ML (shards + prefetch), crawlers, etc.

Como executar:

```bash
uv run examples/multiproc_multithread_example.py
```

Opções relevantes:

- `--n-procs`: número de processos a criar (default: min(4, CPUs)).
- `--total-chunks`: total de unidades de trabalho a dividir entre processos.
- `--base-size`: tamanho base do trabalho CPU-bound (maior = mais CPU).
- `--threads`: número de threads por processo para simular I/O.
- `--io-tasks`: número de tarefas I/O por chunk.

Exemplos:

```bash
# rodar com 4 processos, 8 chunks, 4 threads por processo
python3 examples/multiproc_multithread_example.py --n-procs 4 --total-chunks 8 --base-size 20000 --threads 4 --io-tasks 6
```

Use esses parâmetros para ajustar o benchmark ao seu hardware e medir trade-offs entre paralelismo de processos e threads.
