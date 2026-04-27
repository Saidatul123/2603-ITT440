import random
import time
import threading
from multiprocessing import Pool, cpu_count
import matplotlib
matplotlib.use("Agg")  # Use non-interactive backend to save without display
import matplotlib.pyplot as plt
# =========================
# GAME SETTINGS
# =========================
GAME_TYPES = {
    "klondike": 0.45,
    "spider":   0.35,
    "freecell": 0.55,
    "pyramid":  0.30,
    "tripeaks": 0.40
}
DIFFICULTY_LEVELS = {
    "easy":   10_000_000,
    "medium": 20_000_000,
    "hard":   30_000_000,
    "expert": 40_000_000,
    "master": 50_000_000
}
BASE_MOVES = {
    "klondike": 90,
    "spider":   120,
    "freecell": 70,
    "pyramid":  60,
    "tripeaks": 80
}
# =========================
# CORE FUNCTION
# =========================
def play_solitaire(game):
    """
    Simulate a single solitaire match.
    Returns True (win) or False (loss) based on the game's win rate.
    """
    win_chance = GAME_TYPES[game]
    moves = BASE_MOVES[game] + random.randint(-10, 10)
    # Simulate each move — there is a win chance at every step
    for _ in range(moves):
        if random.random() < win_chance / moves:
            return True  # Win
    return False  # Loss
# =========================
# SEQUENTIAL
# =========================
def run_sequential(n, game):
    start = time.time()
    wins = sum(play_solitaire(game) for _ in range(n))
    elapsed = time.time() - start
    return elapsed, wins
# =========================
# THREADING
# =========================
def thread_worker(n, game, results, index):
    """Thread worker — stores the number of wins in the results list."""
    wins = sum(play_solitaire(game) for _ in range(n))
    results[index] = wins
def run_threading(n, game, threads=4):
    chunk = n // threads
    remainder = n % threads  # Remaining games not evenly divided
    results = [0] * threads
    t_list = []
    start = time.time()
    for i in range(threads):
        # Last thread takes the remaining games
        extra = remainder if i == threads - 1 else 0
        t = threading.Thread(target=thread_worker, args=(chunk + extra, game, results, i))
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()
    elapsed = time.time() - start
    wins = sum(results)
    return elapsed, wins
# =========================
# MULTIPROCESSING
# =========================
def process_worker(args):
    """Process worker — returns the number of wins."""
    n, game = args
    return sum(play_solitaire(game) for _ in range(n))
def run_multiprocessing(n, game):
    processes = cpu_count()
    chunk = n // processes
    remainder = n % processes  # Remaining games
    # Distribute games to each process, last process takes the remainder
    chunks = [chunk] * processes
    chunks[-1] += remainder
    start = time.time()
    with Pool(processes) as pool:
        results = pool.map(process_worker, [(c, game) for c in chunks])
    elapsed = time.time() - start
    wins = sum(results)
    return elapsed, wins
# =========================
# GRAPH
# =========================
def plot_results(seq_time, thr_time, mp_time, game, difficulty):
    methods = ["Sequential", "Threading", "Multiprocessing"]
    times = [seq_time, thr_time, mp_time]
    colors = ["#4C72B0", "#DD8452", "#55A868"]
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(methods, times, color=colors, width=0.5)
    ax.set_title(
        f"Parallel Programming Performance Comparison\n"
        f"Game: {game.capitalize()} | Difficulty: {difficulty.capitalize()}",
        fontsize=13
    )
    ax.set_ylabel("Time (seconds)", fontsize=11)
    ax.set_ylim(0, max(times) * 1.2)
    for bar, val in zip(bars, times):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(times) * 0.02,
            f"{val:.2f}s",
            ha="center", va="bottom", fontsize=11, fontweight="bold"
        )
    plt.tight_layout()
    plt.savefig("results_chart.png", dpi=150)
    plt.close()
    print("📊 Chart saved as results_chart.png")
# =========================
# SAVE FILE
# =========================
def save_to_file(seq, thr, mp, fastest, game, difficulty, total, wins):
    seq_time, seq_wins = seq
    thr_time, thr_wins = thr
    mp_time,  mp_wins  = mp
    win_rate = (seq_wins / total) * 100  # Use sequential as win rate reference
    with open("results.txt", "w") as f:
        f.write("PARALLEL GAME SIMULATION REPORT\n")
        f.write("=================================\n\n")
        f.write(f"Game Type   : {game.capitalize()}\n")
        f.write(f"Difficulty  : {difficulty.capitalize()}\n")
        f.write(f"Total Games : {total:,}\n")
        f.write(f"Win Rate    : {win_rate:.2f}%\n\n")
        f.write(f"Sequential      : {seq_time:.4f} sec  ({seq_wins:,} wins)\n")
        f.write(f"Threading       : {thr_time:.4f} sec  ({thr_wins:,} wins)\n")
        f.write(f"Multiprocessing : {mp_time:.4f} sec  ({mp_wins:,} wins)\n\n")
        f.write(f"Fastest Method  : {fastest}\n")
    print("📁 results.txt successfully created")
# =========================
# INPUT HELPER
# =========================
def get_numbered_choice(prompt, options_dict):
    """Display numbered menu and return the selected key."""
    options_list = list(options_dict.keys())
    for i, key in enumerate(options_list, 1):
        print(f"  {i}. {key.capitalize()}")
    while True:
        choice = input(prompt).strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options_list):
            return options_list[int(choice) - 1]
        print(f"  ⚠️  Invalid choice. Please enter a number between 1 and {len(options_list)}.")
# =========================
# MAIN
# =========================
def main():
    print("=" * 45)
    print("     SOLITAIRE PARALLEL SIMULATION")
    print("=" * 45)

    print("\nSelect Game Type:")
    game = get_numbered_choice("Enter choice (1-5): ", GAME_TYPES)

    print("\nSelect Difficulty:")
    difficulty = get_numbered_choice("Enter choice (1-5): ", DIFFICULTY_LEVELS)

    total = DIFFICULTY_LEVELS[difficulty]
    print(f"\nStarting simulation: {total:,} games of {game.capitalize()}...\n")

    seq_result = run_sequential(total, game)
    thr_result = run_threading(total, game)
    mp_result  = run_multiprocessing(total, game)

    seq_time, seq_wins = seq_result
    thr_time, thr_wins = thr_result
    mp_time,  mp_wins  = mp_result

    times = {
        "Sequential":      seq_time,
        "Threading":       thr_time,
        "Multiprocessing": mp_time
    }
    fastest = min(times, key=times.get)

    win_rate = (seq_wins / total) * 100

    print("\n" + "=" * 45)
    print("              RESULTS SUMMARY")
    print("=" * 45)
    print(f"  Game Type   : {game.capitalize()}")
    print(f"  Difficulty  : {difficulty.capitalize()}")
    print(f"  Total Games : {total:,}")
    print(f"  Win Rate    : {win_rate:.2f}%")
    print("-" * 45)
    print(f"  Sequential      : {seq_time:.4f} sec  ({seq_wins:,} wins)")
    print(f"  Threading       : {thr_time:.4f} sec  ({thr_wins:,} wins)")
    print(f"  Multiprocessing : {mp_time:.4f} sec  ({mp_wins:,} wins)")
    print("-" * 45)
    print(f"  Fastest Method  : {fastest}")
    print("=" * 45)

    plot_results(seq_time, thr_time, mp_time, game, difficulty)
    save_to_file(seq_result, thr_result, mp_result, fastest, game, difficulty, total, seq_wins)

if __name__ == "__main__":
    main()
