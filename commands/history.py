def history(self):
    for idx, cmd in enumerate(self.history):
        print(f"{idx + 1}: {cmd}")