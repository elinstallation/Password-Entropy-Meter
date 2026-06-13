import customtkinter as ctk
from main import calculate_entropy

COLOR_WEAK = "#e74c3c"      # red
COLOR_MODERATE = "#f5a623"  # orange
COLOR_STRONG = "#2ecc71"    # green


def get_strength(entropy: float):
    """Return (label, color) based on per-character entropy."""
    if entropy < 1.5:
        return "WEAK", COLOR_WEAK
    elif entropy < 3.0:
        return "MODERATE", COLOR_MODERATE
    else:
        return "STRONG", COLOR_STRONG


def on_password_change(event=None):
    password = password_entry.get()
    result = calculate_entropy(password)

    #  avoid negative values 
    entropy = max(0.0, result["per_char_entropy"])
    length = max(0, result["length"])
    unique_chars = max(0, result["unique_chars"])

    strength_text, strength_color = get_strength(entropy)

    score_label.configure(text=f"{entropy:.2f}")
    strength_label.configure(text=strength_text, text_color=strength_color)

    progress_value = max(0.0, min(entropy / 4.0, 1.0))
    progress.set(progress_value)
    progress.configure(progress_color=strength_color)

    length_label.configure(text=f"Length: {length}")
    unique_label.configure(text=f"Unique Chars: {unique_chars}")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Password Entropy Meter")
root.geometry("500x400")

ctk.CTkLabel(root, text="Enter Password").pack(pady=(15, 5))
password_entry = ctk.CTkEntry(root, width=250)
password_entry.pack(pady=5)
password_entry.bind("<KeyRelease>", on_password_change)

ctk.CTkLabel(root, text="Entropy Score").pack(pady=(15, 0))
score_label = ctk.CTkLabel(root, text="0.00", font=("Arial", 40, "bold"))
score_label.pack()

strength_label = ctk.CTkLabel(root, text="WEAK", font=("Arial", 20, "bold"), text_color=COLOR_WEAK)
strength_label.pack(pady=5)

progress = ctk.CTkProgressBar(root, width=400, progress_color=COLOR_WEAK)
progress.pack(pady=10)
progress.set(0)

length_label = ctk.CTkLabel(root, text="Length: 0")
length_label.pack()

unique_label = ctk.CTkLabel(root, text="Unique Chars: 0")
unique_label.pack()

on_password_change()

root.mainloop()