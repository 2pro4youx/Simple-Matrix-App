import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import ast

class NightlyMatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix App — Nightly Pro ♣♥")
        self.root.geometry("880x640")
        self.root.minsize(840, 580)
        
        # Aesthetic Nightly Palette (Tokyo Night / Modern IDE)
        self.bg_main = "#13141C"       # Deepest background
        self.bg_card = "#1C1E2B"       # Bento card surface
        self.bg_entry = "#26293B"      # Input field background
        self.border_col = "#2E3247"    # Subtle card border
        self.fg_main = "#E2E4F0"       # Primary text
        self.fg_muted = "#6E738D"      # Placeholder / muted text
        
        # Accents
        self.acc_primary = "#3D59A1"   # Standard button
        self.acc_hover = "#5273CC"     # Button hover
        self.acc_purple = "#5A458E"    # Algebraic / Special button
        self.acc_purp_hov = "#7358B5"
        self.acc_console = "#0D0E14"   # Terminal background
        
        self.root.configure(bg=self.bg_main)
        
        # Custom Dark Scrollbar
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Nightly.Vertical.TScrollbar",
                             background=self.bg_entry,
                             troughcolor=self.bg_main,
                             bordercolor=self.bg_main,
                             arrowcolor=self.fg_muted,
                             width=10)
        self.style.map("Nightly.Vertical.TScrollbar",
                       background=[('active', self.acc_primary)])
        
        # State Variables
        self.memory_matrix = None          
        self.current_result = None
        
        self.setup_ui()
        self.log("------------------------Matrix App--------------------------", "header")
        self.log("System Ready. Type a list [[1,2],[3,4]] or click [⊞] for the Visual Grid Editor.\n", "muted")

    # --- UI Component Builders ---
    def create_card(self, parent, title):
        """Creates a sleek, bordered Bento card with a custom header."""
        outer = tk.Frame(parent, bg=self.bg_card, highlightbackground=self.border_col, highlightthickness=1, padx=8, pady=6)
        lbl = tk.Label(outer, text=title.upper(), bg=self.bg_card, fg="#7AA2F7", font=("Segoe UI", 8, "bold"))
        lbl.pack(anchor="w", pady=(0, 4))
        inner = tk.Frame(outer, bg=self.bg_card)
        inner.pack(fill=tk.BOTH, expand=True)
        return outer, inner

    def set_entry_value(self, entry, text_val):
        """Programmatically sets an entry's value and wakes it from placeholder state."""
        entry.delete(0, tk.END)
        entry.config(fg=self.fg_main)
        entry.insert(0, text_val)

    def create_clearable_entry(self, parent, placeholder_text, grid_title=None):
        """Compact modern input box with placeholder, optional [⊞] grid trigger, and [✕] clear button."""
        wrapper = tk.Frame(parent, bg=self.bg_entry, highlightbackground=self.border_col, highlightthickness=1)
        
        entry = tk.Entry(wrapper, bg=self.bg_entry, fg=self.fg_muted, insertbackground=self.fg_main, 
                         font=("Consolas", 10), relief=tk.FLAT, bd=0)
        entry.insert(0, placeholder_text)
        entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=6, pady=3)
        entry.placeholder = placeholder_text
        
        def on_focus_in(event):
            if entry.get() == entry.placeholder and entry.cget('fg') == self.fg_muted:
                entry.delete(0, tk.END)
                entry.config(fg=self.fg_main)
            wrapper.config(highlightbackground="#7AA2F7")
                
        def on_focus_out(event=None):
            wrapper.config(highlightbackground=self.border_col)
            if not entry.get().strip():
                entry.delete(0, tk.END)
                entry.insert(0, entry.placeholder)
                entry.config(fg=self.fg_muted)
                
        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)
        
        # Clear '✕' Button
        clear_btn = tk.Label(wrapper, text="✕", bg=self.bg_entry, fg=self.fg_muted, font=("Segoe UI", 9), cursor="hand2")
        clear_btn.pack(side=tk.RIGHT, padx=(2, 5))
        clear_btn.bind("<Enter>", lambda e: clear_btn.config(fg="#F7768E")) 
        clear_btn.bind("<Leave>", lambda e: clear_btn.config(fg=self.fg_muted))
        
        def clear_action(event):
            entry.delete(0, tk.END)
            self.root.focus()
            on_focus_out()
        clear_btn.bind("<Button-1>", clear_action)

        # Visual Grid '⊞' Button (for Matrix inputs)
        if grid_title:
            grid_btn = tk.Label(wrapper, text="⊞", bg=self.bg_entry, fg=self.fg_muted, font=("Segoe UI", 11), cursor="hand2")
            grid_btn.pack(side=tk.RIGHT, padx=(4, 2))
            grid_btn.bind("<Enter>", lambda e: grid_btn.config(fg="#7AA2F7"))
            grid_btn.bind("<Leave>", lambda e: grid_btn.config(fg=self.fg_muted))
            grid_btn.bind("<Button-1>", lambda e: self.open_grid_editor(entry, grid_title))
        
        return wrapper, entry

    def create_btn(self, parent, text, command, bg=None, hover=None):
        bg_col = bg or self.acc_primary
        hov_col = hover or self.acc_hover
        btn = tk.Button(parent, text=text, command=command, bg=bg_col, fg=self.fg_main, 
                        activebackground=hov_col, activeforeground="#FFFFFF", 
                        relief=tk.FLAT, bd=0, font=("Segoe UI", 8, "bold"), pady=3, cursor="hand2")
        btn.bind("<Enter>", lambda e: btn.config(bg=hov_col))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg_col))
        return btn

    # --- POP-UP MATRIX GRID EDITOR ---
    def open_grid_editor(self, target_entry, title_text):
        popup = tk.Toplevel(self.root)
        popup.title(f"Grid Editor — {title_text}")
        popup.configure(bg=self.bg_main, padx=12, pady=12)
        popup.transient(self.root)
        popup.grab_set()
        popup.resizable(False, False)

        # Parse existing matrix if present
        init_mat = None
        raw = target_entry.get().strip()
        if raw and raw != getattr(target_entry, 'placeholder', ''):
            try:
                parsed = np.array(ast.literal_eval(raw))
                if parsed.ndim == 1:
                    parsed = parsed.reshape(1, -1)
                if parsed.ndim == 2 and 1 <= parsed.shape[0] <= 8 and 1 <= parsed.shape[1] <= 8:
                    init_mat = parsed
            except Exception:
                pass

        rows_var = tk.IntVar(value=init_mat.shape[0] if init_mat is not None else 3)
        cols_var = tk.IntVar(value=init_mat.shape[1] if init_mat is not None else 3)
        cells = []

        # --- Top Controls: Dimensions & Presets ---
        ctrl_card = tk.Frame(popup, bg=self.bg_card, highlightbackground=self.border_col, highlightthickness=1, padx=8, pady=6)
        ctrl_card.pack(fill=tk.X, pady=(0, 8))

        dim_row = tk.Frame(ctrl_card, bg=self.bg_card)
        dim_row.pack(fill=tk.X, pady=(0, 4))

        tk.Label(dim_row, text="Rows:", bg=self.bg_card, fg=self.fg_main, font=("Segoe UI", 8, "bold")).pack(side=tk.LEFT)
        sp_r = tk.Spinbox(dim_row, from_=1, to=8, textvariable=rows_var, width=3, bg=self.bg_entry, fg=self.fg_main,
                          buttonbackground=self.bg_entry, relief=tk.FLAT, font=("Consolas", 9), command=lambda: rebuild_grid())
        sp_r.pack(side=tk.LEFT, padx=(4, 10))

        tk.Label(dim_row, text="Cols:", bg=self.bg_card, fg=self.fg_main, font=("Segoe UI", 8, "bold")).pack(side=tk.LEFT)
        sp_c = tk.Spinbox(dim_row, from_=1, to=8, textvariable=cols_var, width=3, bg=self.bg_entry, fg=self.fg_main,
                          buttonbackground=self.bg_entry, relief=tk.FLAT, font=("Consolas", 9), command=lambda: rebuild_grid())
        sp_c.pack(side=tk.LEFT, padx=(4, 10))

        # Quick Shape Presets
        for label, r_val, c_val in [("2×2", 2, 2), ("3×3", 3, 3), ("3×1", 3, 1)]:
            self.create_btn(dim_row, label, lambda r=r_val, c=c_val: set_shape(r, c), "#2E3C56", "#3E5174").pack(side=tk.LEFT, padx=2)

        # Quick Fill Tools
        tool_row = tk.Frame(ctrl_card, bg=self.bg_card)
        tool_row.pack(fill=tk.X, pady=(2, 0))
        self.create_btn(tool_row, "Identity (I)", lambda: fill_preset("identity"), "#26293B", "#3D59A1").pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 2))
        self.create_btn(tool_row, "Random", lambda: fill_preset("random"), "#26293B", "#3D59A1").pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        self.create_btn(tool_row, "Zeros", lambda: fill_preset("zeros"), "#26293B", "#3D59A1").pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(2, 0))

        # --- Center: Cell Grid Frame ---
        grid_frame = tk.Frame(popup, bg=self.bg_card, highlightbackground=self.border_col, highlightthickness=1, padx=10, pady=10)
        grid_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))

        def focus_cell(r, c):
            r = max(0, min(len(cells) - 1, r))
            c = max(0, min(len(cells[0]) - 1, c))
            cells[r][c].focus_set()
            cells[r][c].select_range(0, tk.END)

        def rebuild_grid(prefill_matrix=None):
            # Preserve existing typed values before rebuilding
            old_vals = {}
            for r_idx, row_list in enumerate(cells):
                for c_idx, ent in enumerate(row_list):
                    old_vals[(r_idx, c_idx)] = ent.get().strip()

            for widget in grid_frame.winfo_children():
                widget.destroy()
            cells.clear()

            try:
                R = max(1, min(8, int(rows_var.get())))
                C = max(1, min(8, int(cols_var.get())))
            except ValueError:
                R, C = 3, 3

            for i in range(R):
                row_entries = []
                for j in range(C):
                    e = tk.Entry(grid_frame, width=6, bg=self.bg_entry, fg=self.fg_main, insertbackground=self.fg_main,
                                 justify="center", font=("Consolas", 11), relief=tk.FLAT,
                                 highlightbackground=self.border_col, highlightthickness=1)
                    e.grid(row=i, column=j, padx=3, pady=3, ipady=3)
                    
                    # Determine cell initial value
                    if prefill_matrix is not None and i < prefill_matrix.shape[0] and j < prefill_matrix.shape[1]:
                        val = prefill_matrix[i, j]
                        val_str = str(int(val) if float(val).is_integer() else round(float(val), 4))
                        e.insert(0, val_str)
                    elif (i, j) in old_vals and old_vals[(i, j)] != "":
                        e.insert(0, old_vals[(i, j)])
                    else:
                        e.insert(0, "0")

                    # Focus styling & Arrow key navigation
                    e.bind("<FocusIn>", lambda ev, w=e: (w.config(highlightbackground="#7AA2F7"), w.select_range(0, tk.END)))
                    e.bind("<FocusOut>", lambda ev, w=e: w.config(highlightbackground=self.border_col))
                    e.bind("<Up>", lambda ev, r=i, c=j: focus_cell(r - 1, c))
                    e.bind("<Down>", lambda ev, r=i, c=j: focus_cell(r + 1, c))
                    e.bind("<Left>", lambda ev, r=i, c=j: focus_cell(r, c - 1))
                    e.bind("<Right>", lambda ev, r=i, c=j: focus_cell(r, c + 1))
                    e.bind("<Return>", lambda ev: apply_to_entry())
                    row_entries.append(e)
                cells.append(row_entries)
            
            if cells and cells[0]:
                cells[0][0].focus_set()

        def set_shape(r, c):
            rows_var.set(r)
            cols_var.set(c)
            rebuild_grid()

        def fill_preset(mode):
            R, C = len(cells), len(cells[0])
            for i in range(R):
                for j in range(C):
                    cells[i][j].delete(0, tk.END)
                    if mode == "zeros":
                        cells[i][j].insert(0, "0")
                    elif mode == "identity":
                        cells[i][j].insert(0, "1" if i == j else "0")
                    elif mode == "random":
                        cells[i][j].insert(0, str(np.random.randint(-9, 10)))

        def apply_to_entry():
            matrix_list = []
            try:
                for row_entries in cells:
                    row_vals = []
                    for ent in row_entries:
                        txt = ent.get().strip()
                        val = float(txt) if txt else 0.0
                        row_vals.append(int(val) if val.is_integer() else val)
                    matrix_list.append(row_vals)
                self.set_entry_value(target_entry, str(matrix_list))
                popup.destroy()
            except ValueError:
                messagebox.showerror("Invalid Cell", "All cells must contain valid numbers.", parent=popup)

        # --- Bottom Bar: Apply & Cancel ---
        bot_bar = tk.Frame(popup, bg=self.bg_main)
        bot_bar.pack(fill=tk.X)
        self.create_btn(bot_bar, "Cancel", popup.destroy, "#2E3247", "#414763").pack(side=tk.RIGHT, padx=(4, 0), ipadx=8)
        self.create_btn(bot_bar, "Apply to Input ✓", apply_to_entry, self.acc_primary, self.acc_hover).pack(side=tk.RIGHT, ipadx=12)

        rebuild_grid(prefill_matrix=init_mat)
        sp_r.bind("<Return>", lambda e: rebuild_grid())
        sp_c.bind("<Return>", lambda e: rebuild_grid())

    def setup_ui(self):
        # ================= TOP BAR: INPUTS & MEMORY =================
        top_outer, top_frame = self.create_card(self.root, "Input & Memory Matrix")
        top_outer.pack(fill=tk.X, padx=10, pady=(10, 4))
        
        top_frame.grid_columnconfigure(1, weight=3)
        top_frame.grid_columnconfigure(3, weight=1)

        # Matrix A (With [⊞] Grid Editor button)
        tk.Label(top_frame, text="Matrix A (or Coeff):", bg=self.bg_card, fg=self.fg_main, font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky="e", pady=2)
        wrap_a, self.entry_a = self.create_clearable_entry(top_frame, "e.g., [[1, 2, 3], [2, 3, 4], [3, 4, 5]]", grid_title="Matrix A")
        wrap_a.grid(row=0, column=1, sticky="ew", padx=(6, 12), pady=2)
        
        # Matrix B (With [⊞] Grid Editor button)
        tk.Label(top_frame, text="Matrix B (or Const):", bg=self.bg_card, fg=self.fg_main, font=("Segoe UI", 9, "bold")).grid(row=1, column=0, sticky="e", pady=2)
        wrap_b, self.entry_b = self.create_clearable_entry(top_frame, "e.g., [[1, 2], [3, 4]]  or  [[1], [2], [3]]", grid_title="Matrix B")
        wrap_b.grid(row=1, column=1, sticky="ew", padx=(6, 12), pady=2)
        
        # Scalar / Size
        tk.Label(top_frame, text="Scalar / Gen Size:", bg=self.bg_card, fg=self.fg_main, font=("Segoe UI", 9, "bold")).grid(row=2, column=0, sticky="e", pady=2)
        wrap_s, self.entry_scalar = self.create_clearable_entry(top_frame, "e.g., 3 (Scalar value or 3x3 generator shape)")
        wrap_s.grid(row=2, column=1, sticky="ew", padx=(6, 12), pady=2)

        # Memory Panel
        mem_box = tk.Frame(top_frame, bg=self.bg_entry, highlightbackground=self.border_col, highlightthickness=1, padx=6, pady=4)
        mem_box.grid(row=0, column=3, rowspan=3, sticky="nsew")
        mem_box.grid_columnconfigure((0, 1), weight=1)
        
        self.lbl_memory = tk.Label(mem_box, text="MEM: EMPTY", bg=self.bg_entry, fg="#E0AF68", font=("Consolas", 9, "bold"))
        self.lbl_memory.grid(row=0, column=0, columnspan=2, pady=(0, 3))
        
        self.create_btn(mem_box, "Save Output", self.save_to_memory, "#2E3C56", "#3E5174").grid(row=1, column=0, columnspan=2, sticky="ew", pady=2)
        self.create_btn(mem_box, "Load → A", lambda: self.load_memory(self.entry_a), "#2E3C56", "#3E5174").grid(row=2, column=0, sticky="ew", padx=(0, 2), pady=2)
        self.create_btn(mem_box, "Load → B", lambda: self.load_memory(self.entry_b), "#2E3C56", "#3E5174").grid(row=2, column=1, sticky="ew", padx=(2, 0), pady=2)

        # ================= MIDDLE: 3-COLUMN BENTO OPERATIONS =================
        bento = tk.Frame(self.root, bg=self.bg_main)
        bento.pack(fill=tk.X, padx=10, pady=4)
        bento.grid_columnconfigure((0, 1, 2), weight=1, uniform="bento")

        # --- Col 0: Basic Operations (Scalar & Vector/Matrix) ---
        c0_outer, c0 = self.create_card(bento, "Basic Operations (Case 2)")
        c0_outer.grid(row=0, column=0, sticky="nsew", padx=(0, 4))
        c0.grid_columnconfigure((0, 1, 2), weight=1)
        
        tk.Label(c0, text="Scalar (Matrix A & Scalar)", bg=self.bg_card, fg=self.fg_muted, font=("Segoe UI", 8)).grid(row=0, column=0, columnspan=3, sticky="w")
        self.create_btn(c0, "A + S", lambda: self.scalar_op('+')).grid(row=1, column=0, sticky="ew", padx=2, pady=2)
        self.create_btn(c0, "A - S", lambda: self.scalar_op('-')).grid(row=1, column=1, sticky="ew", padx=2, pady=2)
        self.create_btn(c0, "A * S", lambda: self.scalar_op('*')).grid(row=1, column=2, sticky="ew", padx=2, pady=2)
        
        tk.Label(c0, text="Vector / Matrix (A & B)", bg=self.bg_card, fg=self.fg_muted, font=("Segoe UI", 8)).grid(row=2, column=0, columnspan=3, sticky="w", pady=(6, 0))
        self.create_btn(c0, "A + B", lambda: self.matrix_op('+')).grid(row=3, column=0, sticky="ew", padx=2, pady=2)
        self.create_btn(c0, "A - B", lambda: self.matrix_op('-')).grid(row=3, column=1, sticky="ew", padx=2, pady=2)
        self.create_btn(c0, "A @ B", lambda: self.matrix_op('@')).grid(row=3, column=2, sticky="ew", padx=2, pady=2)

        # --- Col 1: Advanced Operations (Matrix A) ---
        c1_outer, c1 = self.create_card(bento, "Advanced Operations (Case 3)")
        c1_outer.grid(row=0, column=1, sticky="nsew", padx=4)
        c1.grid_columnconfigure((0, 1, 2), weight=1)

        adv_btns = [
            ("Determinant", self.do_determinant),
            ("Singularity", self.do_singularity),
            ("Transpose", self.do_transpose),
            ("Inverse", self.do_inverse),
            ("Adjoint", self.do_adjoint),
            ("Cofactor", self.do_cofactor),
            ("Rank", self.do_rank),
            ("Orthogonal?", self.do_ortho),
            ("Independent?", self.do_independence),
        ]
        for idx, (lbl, cmd) in enumerate(adv_btns):
            r, col = divmod(idx, 3)
            self.create_btn(c1, lbl, cmd).grid(row=r, column=col, sticky="ew", padx=2, pady=2)

        # --- Col 2: Symmetry & Algebraic Operations ---
        c2_outer, c2 = self.create_card(bento, "Symmetry & Algebraic (Cases 3.4 & 4)")
        c2_outer.grid(row=0, column=2, sticky="nsew", padx=(4, 0))
        c2.grid_columnconfigure((0, 1, 2), weight=1)

        tk.Label(c2, text="Symmetry (Matrix A or Size)", bg=self.bg_card, fg=self.fg_muted, font=("Segoe UI", 8)).grid(row=0, column=0, columnspan=3, sticky="w")
        self.create_btn(c2, "Check Sym", self.do_sym_check).grid(row=1, column=0, sticky="ew", padx=2, pady=2)
        self.create_btn(c2, "Make Sym", self.do_sym_create).grid(row=1, column=1, sticky="ew", padx=2, pady=2)
        self.create_btn(c2, "Gen Sym", self.do_gen_sym).grid(row=1, column=2, sticky="ew", padx=2, pady=2)
        
        self.create_btn(c2, "Gen Skew-Sym", self.do_gen_skew).grid(row=2, column=0, columnspan=3, sticky="ew", padx=2, pady=2)

        tk.Label(c2, text="Algebraic Solver (A=Coeff, B=Const)", bg=self.bg_card, fg=self.fg_muted, font=("Segoe UI", 8)).grid(row=3, column=0, columnspan=3, sticky="w", pady=(4, 0))
        self.create_btn(c2, "Linear Eq", self.do_linear, self.acc_purple, self.acc_purp_hov).grid(row=4, column=0, sticky="ew", padx=2, pady=2)
        self.create_btn(c2, "Quadratic", lambda: self.do_dev("Quadratic"), self.acc_purple, self.acc_purp_hov).grid(row=4, column=1, sticky="ew", padx=2, pady=2)
        self.create_btn(c2, "Cubic", lambda: self.do_dev("Cubic"), self.acc_purple, self.acc_purp_hov).grid(row=4, column=2, sticky="ew", padx=2, pady=2)

        # ================= BOTTOM: CONSOLE OUTPUT =================
        console_outer = tk.Frame(self.root, bg=self.bg_card, highlightbackground=self.border_col, highlightthickness=1, padx=8, pady=6)
        console_outer.pack(fill=tk.BOTH, expand=True, padx=10, pady=(4, 10))
        
        top_console = tk.Frame(console_outer, bg=self.bg_card)
        top_console.pack(fill=tk.X, pady=(0, 4))
        tk.Label(top_console, text="TERMINAL OUTPUT", bg=self.bg_card, fg="#7AA2F7", font=("Segoe UI", 8, "bold")).pack(side=tk.LEFT)
        
        clear_console_btn = tk.Label(top_console, text="✕", bg=self.bg_card, fg=self.fg_muted, font=("Segoe UI", 10, "bold"), cursor="hand2")
        clear_console_btn.pack(side=tk.RIGHT, padx=2)
        clear_console_btn.bind("<Enter>", lambda e: clear_console_btn.config(fg="#F7768E")) 
        clear_console_btn.bind("<Leave>", lambda e: clear_console_btn.config(fg=self.fg_muted))
        clear_console_btn.bind("<Button-1>", lambda e: self.clear_console())

        console_body = tk.Frame(console_outer, bg=self.acc_console)
        console_body.pack(fill=tk.BOTH, expand=True)

        self.console = tk.Text(console_body, bg=self.acc_console, fg="#9ECE6A", font=("Consolas", 10), 
                               state="disabled", relief=tk.FLAT, padx=10, pady=8, bd=0)
        
        # Rich-style text tags
        self.console.tag_config("header", foreground="#7AA2F7", font=("Consolas", 10, "bold"))
        self.console.tag_config("error", foreground="#F7768E", font=("Consolas", 10, "bold"))
        self.console.tag_config("warn", foreground="#E0AF68")
        self.console.tag_config("muted", foreground="#6E738D")
        self.console.tag_config("eq", foreground="#BB9AF7", font=("Consolas", 10, "bold"))

        scrollbar = ttk.Scrollbar(console_body, orient="vertical", command=self.console.yview, style="Nightly.Vertical.TScrollbar")
        self.console.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.console.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # ================= HELPERS & IO =================
    def log(self, msg, tag=None):
        self.console.config(state="normal")
        if tag:
            self.console.insert(tk.END, f"{msg}\n", tag)
        else:
            self.console.insert(tk.END, f"{msg}\n")
        self.console.see(tk.END)
        self.console.config(state="disabled")

    def clear_console(self):
        self.console.config(state="normal")
        self.console.delete(1.0, tk.END)
        self.console.config(state="disabled")
        
    def get_matrix(self, entry_widget, label_name="Matrix"):
        inp = entry_widget.get().strip()
        if not inp or inp == getattr(entry_widget, 'placeholder', ''): 
            self.log(f"Enter a valid format for {label_name}", "error")
            return None
        try:
            arr = ast.literal_eval(inp)
            mat = np.array(arr)
            self.log(f"Your matrix is:\n{mat}")
            self.log(f"Shape of matrix is {mat.shape} and Dimension of matrix is {mat.ndim}", "muted")
            return mat
        except (ValueError, SyntaxError):
            self.log("Enter a valid format", "error")
            return None

    def get_scalar(self):
        inp = self.entry_scalar.get().strip()
        if not inp or inp == getattr(self.entry_scalar, 'placeholder', ''): 
            self.log("Enter a valid Scalar / Size value", "error")
            return None
        try:
            return float(inp)
        except ValueError:
            self.log("Invalid Format", "error")
            return None

    # ================= MEMORY FEATURES =================
    def save_to_memory(self):
        if self.current_result is not None:
            self.memory_matrix = self.current_result
            shape = self.memory_matrix.shape
            self.lbl_memory.config(text=f"MEM: {shape}", fg="#9ECE6A")
            self.log(f"--- Saved {shape} Matrix to Memory ---", "warn")
        else:
            self.log("No valid matrix result to save.", "error")

    def load_memory(self, entry_widget):
        if self.memory_matrix is not None:
            self.set_entry_value(entry_widget, str(self.memory_matrix.tolist()))
            self.log("Memory loaded into input field.", "muted")
        else:
            self.log("Memory is empty.", "error")

    # ================= CORE MATH HELPERS (FROM CASE 3) =================
    def check_singularity(self, mat):
        try:
            det = np.linalg.det(mat)
            if np.isclose(det, 0):
                self.log("Matrix is Singular")
            else:
                self.log("Matrix is not Singular")
        except np.linalg.LinAlgError:
            self.log("The matrix must be a square matrix to compute Singularity", "error")

    def check_determinant(self, mat):
        try:
            det1 = np.linalg.det(mat)
            self.log(f"Determinant of the Matrix is: {round(det1, 4)}")
            return det1
        except (ValueError, SyntaxError, np.linalg.LinAlgError):
            self.log("The matrix shall be a square matrix to compute Determinant", "error")
            return None

    def check_symmetry(self, mat):
        if np.array_equal(mat, mat.T):
            self.log("Matrix is Symmetric")
            return 1
        elif np.array_equal(mat, -mat.T):
            self.log("Matrix is Skew-Symmeteric")
            return -1
        else:
            self.log("Matrix is not Symmetric")
            return 0

    def print_extras(self, mat):
        self.log("\nExtras:", "warn")
        self.check_singularity(mat)
        self.check_symmetry(mat)
        self.check_determinant(mat)
        self.log("-" * 60, "muted")

    # ================= CASE 2: BASIC OPERATIONS =================
    def scalar_op(self, op):
        self.log("----------------------Basic Scalar Op-----------------------", "header")
        matrix1 = self.get_matrix(self.entry_a, "Matrix A")
        scalar = self.get_scalar()
        if matrix1 is None or scalar is None: return
        
        identity = np.eye(len(matrix1))
        if op == '+':
            self.current_result = matrix1 + (scalar * identity)
        elif op == '-':
            self.current_result = matrix1 - (abs(scalar) * identity)
        elif op == '*':
            self.current_result = matrix1 * scalar
            
        self.log(f"------------------------Solution----------------------------\n{self.current_result}")
        self.log("-" * 60, "muted")

    def matrix_op(self, op):
        self.log("----------------------Basic Matrix Op-----------------------", "header")
        matrix1 = self.get_matrix(self.entry_a, "Matrix A")
        if matrix1 is None: return
        matrix2 = self.get_matrix(self.entry_b, "Matrix B")
        if matrix2 is None: return
        
        if op in ('+', '-'):
            if matrix1.shape == matrix2.shape and matrix1.ndim == matrix2.ndim:
                self.current_result = matrix1 + matrix2 if op == '+' else matrix1 - matrix2
                self.log(f"------------------------Solution----------------------------\n{self.current_result}")
            else:
                self.log("The operation is not possible due to different shape or dimension", "error")
        elif op == '@':
            if matrix1.shape[1] == matrix2.shape[0]:
                self.current_result = matrix1 @ matrix2
                self.log(f"------------------------Solution----------------------------\n{self.current_result}")
            else:
                self.log("The operation is not possible.", "error")
        self.log("-" * 60, "muted")

    # ================= CASE 3: ADVANCED OPERATIONS =================
    def do_determinant(self):
        self.log("-------------------------Determinant------------------------", "header")
        m3 = self.get_matrix(self.entry_a)
        if m3 is None: return
        self.check_determinant(m3)
        self.log("\nExtras:", "warn")
        self.check_singularity(m3)
        self.check_symmetry(m3)
        self.log("-" * 60, "muted")

    def do_singularity(self):
        self.log("------------------------Singularity-------------------------", "header")
        m3 = self.get_matrix(self.entry_a)
        if m3 is None: return
        self.check_singularity(m3)
        self.log("\nExtras:", "warn")
        self.check_symmetry(m3)
        self.check_determinant(m3)
        self.log("-" * 60, "muted")

    def do_transpose(self):
        self.log("----------------------Current Matrix------------------------", "header")
        m3 = self.get_matrix(self.entry_a)
        if m3 is None: return
        self.print_extras(m3)
        
        self.log("---------------------Transposed Matrix----------------------", "header")
        transposed = m3.T
        self.current_result = transposed
        self.log(f"Your transposed matrix is:\n{transposed}")
        self.log(f"Shape of matrix is {transposed.shape} and Dimension of matrix is {transposed.ndim}", "muted")
        self.print_extras(transposed)

    def do_inverse(self):
        self.log("---------------------Inversed Matrix------------------------", "header")
        m3 = self.get_matrix(self.entry_a)
        if m3 is None: return
        try:
            if not np.isclose(np.linalg.det(m3), 0):
                inv = np.linalg.inv(m3)
                self.current_result = inv
                self.log(f"{inv}")
                self.print_extras(inv)
            else:
                self.log("The matrix is singular, therefore it is not invertible", "error")
        except np.linalg.LinAlgError:
            self.log("The matrix must be square to compute Inverse", "error")

    def do_adjoint(self):
        self.log("----------------------Adjoint Matrix------------------------", "header")
        m3 = self.get_matrix(self.entry_a)
        if m3 is None: return
        try:
            det = np.linalg.det(m3)
            if np.isclose(det, 0):
                self.log("The matrix is singular, therefore it is not invertible", "error")
                return
            adj = det * np.linalg.inv(m3)
            self.current_result = adj
            self.log(f"{adj}")
            self.print_extras(adj)
        except np.linalg.LinAlgError:
            self.log("The matrix must be square to compute Adjoint", "error")

    def do_cofactor(self):
        self.log("---------------------Cofactor Matrix------------------------", "header")
        m3 = self.get_matrix(self.entry_a)
        if m3 is None: return
        try:
            det = np.linalg.det(m3)
            if np.isclose(det, 0):
                self.log("Cannot Compute cofactor matrix due to singularity", "error")
                return
            cof = np.transpose(np.linalg.inv(m3)) * det
            self.current_result = cof
            self.log(f"{cof}")
            self.print_extras(cof)
        except np.linalg.LinAlgError:
            self.log("The matrix must be square to compute Cofactor", "error")

    def do_rank(self):
        self.log("----------------------Rank of Matrix------------------------", "header")
        m3 = self.get_matrix(self.entry_a)
        if m3 is None: return
        self.log(f"Rank of the Matrix is: {np.linalg.matrix_rank(m3)}")
        self.print_extras(m3)

    def do_ortho(self):
        self.log("-------------------Orthogonal Checker-----------------------", "header")
        m3 = self.get_matrix(self.entry_a)
        if m3 is None: return
        try:
            res = np.allclose(m3 @ np.transpose(m3), np.eye(m3.shape[0]))
            status = "is Orthogonal" if res else "is not Orthogonal"
            self.log(f"The given matrix {status}")
            self.print_extras(m3)
        except ValueError:
            self.log("Matrix dimensions incompatible for Orthogonality check", "error")

    def do_independence(self):
        self.log("------------------Independence Checker----------------------", "header")
        m3 = self.get_matrix(self.entry_a)
        if m3 is None: return
        res = np.allclose(m3.shape[1], np.linalg.matrix_rank(m3))
        status = "is Independent" if res else "is not Independent"
        self.log(f"The given matrix {status}")
        self.print_extras(m3)

    # ================= CASE 3.4: SYMMETRY OPERATIONS =================
    def do_sym_check(self):
        self.log("-------------------------Symmetry---------------------------", "header")
        m3 = self.get_matrix(self.entry_a)
        if m3 is None: return
        self.print_extras(m3)

    def do_sym_create(self):
        self.log("---------------------Symmetric Creator----------------------", "header")
        m3 = self.get_matrix(self.entry_a)
        if m3 is None: return
        self.print_extras(m3)
        
        if np.array_equal(m3, m3.T):
            self.log("Matrix is Already Symmetric", "warn")
        elif np.array_equal(m3, -m3.T):
            ans = messagebox.askyesno("Skew-Symmetric Detected", "Matrix is Skew-Symmetric; Do you want to Continue?")
            if ans:
                m3 = m3 * m3.T
                self.current_result = m3
                self.log(f"---------------------Symmetric Matrix-----------------------\n{m3}")
                self.print_extras(m3)
            else:
                self.log("Operation Cancelled", "error")
        else:
            m3 = m3 * m3.T
            self.current_result = m3
            self.log(f"---------------------Symmetric Matrix-----------------------\n{m3}")
            self.print_extras(m3)

    def do_gen_sym(self):
        s = self.get_scalar()
        if s is None: return
        size = int(abs(s))
        matrix = np.zeros((size, size), dtype=int)
        for i in range(size):
            for j in range(i, size):
                val = np.random.randint(1, 100)
                matrix[i, j] = val
                matrix[j, i] = val
        self.current_result = matrix
        self.log("---------------------Symmetric Matrix-----------------------", "header")
        self.log(f"{matrix}")
        self.print_extras(matrix)

    def do_gen_skew(self):
        s = self.get_scalar()
        if s is None: return
        size = int(abs(s))
        matrix = np.zeros((size, size), dtype=int)
        for i in range(size):
            for j in range(i + 1, size):
                val = np.random.randint(1, 100)
                matrix[i, j] = val
                matrix[j, i] = -val
        self.current_result = matrix
        self.log("-------------------Skew-Symmetric Matrix--------------------", "header")
        self.log(f"{matrix}")
        self.print_extras(matrix)

    # ================= CASE 4: ALGEBRAIC OPERATIONS =================
    def linp(self, A, B):
        var = [chr(x) for x in range(97, 123)]
        rows, columns = A.shape
        if B.shape[0] != rows:
            self.log("Error: Number of rows in B must be equal to the number of rows in A", "error")
            return None
        
        for i in range(rows):
            eq = []
            for j in range(columns):
                val = float(A[i, j])
                if len(eq) == 0:
                    sign = '-' if val < 0 else ''
                else:
                    sign = ' - ' if val < 0 else ' + '
                
                abs_val = abs(val)
                if abs_val == 1:
                    coef = ""
                else:
                    coef = str(int(abs_val) if abs_val.is_integer() else abs_val)
                
                term = f"{sign}{coef}{var[j]}"
                eq.append(term)
            
            lhs = "".join(eq) if eq else "0"
            rhs = B[i] if B.ndim == 1 else B[i, 0]
            self.log(f"  {lhs} = {rhs}", "eq")
        return var

    def do_linear(self):
        self.log("-----------------------------------------------------------", "error")
        self.log("This only works for square coefficient matrices,\ni.e. the number equations shall be equal to number of variables", "error")
        self.log("-----------------------------------------------------------", "error")
        
        matrixA = self.get_matrix(self.entry_a, "Coefficient Matrix A")
        if matrixA is None: return
        matrixB = self.get_matrix(self.entry_b, "Constant Matrix B")
        if matrixB is None: return
        
        self.log("---------------------Current Equation----------------------", "header")
        self.log("Equations formed are:")
        var = self.linp(matrixA, matrixB)
        if var is None: return
        
        self.log("---------------------Linear Solution-----------------------", "header")
        try:
            solution = np.linalg.solve(matrixA, matrixB)
            self.current_result = solution
            for i, v in enumerate(solution):
                val_str = np.round(v, 4)
                self.log(f"  {var[i]} = {val_str}", "eq")
        except np.linalg.LinAlgError as e:
            self.log(f"Linear Solver Error: {e} (Ensure A is square and non-singular)", "error")
        self.log("-" * 60, "muted")

    def do_dev(self, name):
        self.log(f"--- {name} Function ---", "header")
        self.log("Under Development", "warn")
        self.log("-" * 60, "muted")

if __name__ == "__main__":
    root = tk.Tk()
    app = NightlyMatrixApp(root)
    root.mainloop()