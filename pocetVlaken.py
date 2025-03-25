import threading

threads = []
i = 0

try:
    while True:
        t = threading.Thread(target=lambda: threading.Event().wait())
        t.start()
        threads.append(t)
        i += 1
except RuntimeError as e:
    print(f"Zlyhalo po {i} vláknach: {e}")

# pozor nech nespadne windows, na macu je to ok