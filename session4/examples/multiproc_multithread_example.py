import os
import time
import random
import argparse
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process


def cpu_heavy_calculation(n: int) -> int:
    # Simula trabalho CPU-bound (cálculo pesado)
    s = 0
    for i in range(1, n):
        s += i * i
    return s


def io_simulation(task_id: int, latency_range=(0.05, 0.2)) -> str:
    # Simula operação I/O-bound (ex.: fetch / escrita)
    t = random.uniform(*latency_range)
    time.sleep(t)
    return f"task-{task_id}-done({t:.2f}s)"


def worker(proc_id: int, chunks: list, threads: int, io_tasks: int):
    start = time.time()
    print(f"[P{proc_id}] started (pid={os.getpid()}) with {len(chunks)} chunks")

    for chunk_id, chunk_size in enumerate(chunks):
        # Parte CPU-bound
        cpu_result = cpu_heavy_calculation(chunk_size)

        # Parte I/O-bound: usar threads dentro do processo
        io_results = []
        with ThreadPoolExecutor(max_workers=threads) as ex:
            futures = [ex.submit(io_simulation, f"{proc_id}-{chunk_id}-{i}") for i in range(io_tasks)]
            for f in futures:
                io_results.append(f.result())

        print(f"[P{proc_id}] chunk={chunk_id} cpu={cpu_result} io={io_results}")

    elapsed = time.time() - start
    print(f"[P{proc_id}] finished in {elapsed:.2f}s")


def split_work(total_chunks: int, base_size: int, n_procs: int):
    # Gera uma lista de chunk sizes e particiona entre processos
    sizes = [base_size + (i % 3) * 1000 for i in range(total_chunks)]
    per_proc = [[] for _ in range(n_procs)]
    for i, s in enumerate(sizes):
        per_proc[i % n_procs].append(s)
    return per_proc


def main():
    parser = argparse.ArgumentParser(description="Exemplo: multiprocessing + multithreading benchmark")
    parser.add_argument("--n-procs", type=int, default=min(4, os.cpu_count() or 1), help="Número de processos")
    parser.add_argument("--total-chunks", type=int, default=8, help="Total de chunks a processar")
    parser.add_argument("--base-size", type=int, default=20000, help="Tamanho base (workload CPU)")
    parser.add_argument("--threads", type=int, default=4, help="Threads por processo para I/O")
    parser.add_argument("--io-tasks", type=int, default=6, help="Número de tarefas I/O por chunk")
    args = parser.parse_args()

    n_procs = max(1, args.n_procs)
    total_chunks = max(1, args.total_chunks)
    base_size = max(1, args.base_size)

    per_proc_chunks = split_work(total_chunks, base_size, n_procs)

    procs = []
    t0 = time.time()
    for pid in range(n_procs):
        p = Process(target=worker, args=(pid, per_proc_chunks[pid], args.threads, args.io_tasks))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()

    print(f"All workers finished in {time.time() - t0:.2f}s")


if __name__ == "__main__":
    main()
