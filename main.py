import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import zipfile


def collect_nk_files(src_directory, dst_directory):
    # Create a new zipfile at the destination directory
    zip_filename = os.path.join(dst_directory, 'collected_nk_files.zip')
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the source directory
        for root, dirs, files in os.walk(src_directory):
            for file in files:
                if file.endswith('.nk'):
                    # Construct the file path
                    file_path = os.path.join(root, file)
                    # Write the file to the zip
                    zipf.write(file_path, os.path.relpath(file_path, src_directory))
                    print(f'Added {file_path} to {zip_filename}')
    messagebox.showinfo("Success", f"All .nk files have been collected into {zip_filename}")


def browse_path(entry):
    directory = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, directory)


def on_submit(src_entry, dst_entry):
    src_directory = src_entry.get()
    dst_directory = dst_entry.get()
    if not src_directory or not dst_directory:
        messagebox.showwarning("Warning", "Please select both source and destination directories.")
        return
    collect_nk_files(src_directory, dst_directory)


def main():
    root = tk.Tk()
    root.title('Nuke Script Collector')

    src_label = tk.Label(root, text="Source Directory:")
    src_label.grid(row=0, column=0)

    src_entry = tk.Entry(root, width=50)
    src_entry.grid(row=0, column=1)

    src_browse_button = tk.Button(root, text="Browse", command=lambda: browse_path(src_entry))
    src_browse_button.grid(row=0, column=2)

    dst_label = tk.Label(root, text="Destination Directory:")
    dst_label.grid(row=1, column=0)

    dst_entry = tk.Entry(root, width=50)
    dst_entry.grid(row=1, column=1)

    dst_browse_button = tk.Button(root, text="Browse", command=lambda: browse_path(dst_entry))
    dst_browse_button.grid(row=1, column=2)

    submit_button = tk.Button(root, text="Collect and Zip NK Files", command=lambda: on_submit(src_entry, dst_entry))
    submit_button.grid(row=2, column=0, columnspan=3, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import zipfile


def collect_nk_files(src_directory, dst_directory):
    # Create a new zipfile at the destination directory
    zip_filename = os.path.join(dst_directory, 'collected_nk_files.zip')
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the source directory
        for root, dirs, files in os.walk(src_directory):
            for file in files:
                if file.endswith('.nk'):
                    # Construct the file path
                    file_path = os.path.join(root, file)
                    # Write the file to the zip
                    zipf.write(file_path, os.path.relpath(file_path, src_directory))
                    print(f'Added {file_path} to {zip_filename}')
    messagebox.showinfo("Success", f"All .nk files have been collected into {zip_filename}")


def browse_path(entry):
    directory = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, directory)


def on_submit(src_entry, dst_entry):
    src_directory = src_entry.get()
    dst_directory = dst_entry.get()
    if not src_directory or not dst_directory:
        messagebox.showwarning("Warning", "Please select both source and destination directories.")
        return
    collect_nk_files(src_directory, dst_directory)


def main():
    root = tk.Tk()
    root.title('NK File Collector')

    src_label = tk.Label(root, text="Source Directory:")
    src_label.grid(row=0, column=0)

    src_entry = tk.Entry(root, width=50)
    src_entry.grid(row=0, column=1)

    src_browse_button = tk.Button(root, text="Browse", command=lambda: browse_path(src_entry))
    src_browse_button.grid(row=0, column=2)

    dst_label = tk.Label(root, text="Destination Directory:")
    dst_label.grid(row=1, column=0)

    dst_entry = tk.Entry(root, width=50)
    dst_entry.grid(row=1, column=1)

    dst_browse_button = tk.Button(root, text="Browse", command=lambda: browse_path(dst_entry))
    dst_browse_button.grid(row=1, column=2)

    submit_button = tk.Button(root, text="Collect and Zip NK Files", command=lambda: on_submit(src_entry, dst_entry))
    submit_button.grid(row=2, column=0, columnspan=3, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()