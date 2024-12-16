import random
import time
import matplotlib.pyplot as plt

def array_acak(n, nilai_max, seed=42):
    random.seed(seed)
    return [random.randint(1, nilai_max) for _ in range(n)]

def cek_unik(array):
    seen = set()
    for num in array:
        if num in seen:
            return False
        seen.add(num)
    return True

def waktu_eksekusi(n, max_val, iterations=30):
    waktu_worst_case = 0
    waktu_average_case = 0

    # Mengukur worst case
    array_worst_case = array_acak(n, max_val, seed=42)
    array_worst_case.append(array_worst_case[0])  # Tambahkan duplikat
    mulai = time.perf_counter()
    cek_unik(array_worst_case)
    waktu_worst_case = time.perf_counter() - mulai

    # Mengukur average case
    total_waktu = 0
    for i in range(iterations):
        array_avg_case = array_acak(n, max_val, seed=42 + i)
        mulai = time.perf_counter()
        cek_unik(array_avg_case)
        total_waktu += time.perf_counter() - mulai
    waktu_average_case = total_waktu / iterations

    return waktu_worst_case, waktu_average_case

def main():
    nilai_n = [100, 150, 200, 250, 300, 350, 400, 500]
    stambuk_last_3_digits = 41
    max_value = 250 - stambuk_last_3_digits

    results = []
    for n in nilai_n:
        worst, avg = waktu_eksekusi(n, max_value)
        results.append((n, worst, avg))

    # Simpan hasil perhitungan
    with open("worst_avg.txt", "w") as f:
        for n, worst, avg in results:
            f.write(f"n = {n}, Worst Case = {worst:.6f}s, Average Case = {avg:.6f}s\n")

    # Grafik
    plt.figure(figsize=(10, 6))
    worst_cases = [r[1] for r in results]
    average_cases = [r[2] for r in results]

    plt.plot(nilai_n, worst_cases, label="Worst Case", marker="o")
    plt.plot(nilai_n, average_cases, label="Average Case", marker="s")

    plt.title("Time Complexity of Unique Element Check")
    plt.xlabel("Array Size (n)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid()

    # Simpan grafik
    plt.savefig("hasil.jpg")
    plt.show()

    print("Program selesai. Semua file telah disimpan.")

if __name__ == "__main__":
    main()
