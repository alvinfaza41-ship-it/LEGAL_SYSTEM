<main class="content">
  <div class="dashboard-header">
    <h1>Dashboard Overview</h1>
  </div>

  <div class="dashboard-grid">
    <!-- Kartu 1: Total Client -->
    <div class="card card-blue">
      <div class="card-title">Total Client</div>
      <div class="card-value">125</div>
    </div>

    <!-- Kartu 2: Pengajuan Halal -->
    <div class="card card-orange">
      <div class="card-title">Pengajuan Halal</div>
      <div class="card-value">48</div>
    </div>

    <!-- Kartu 3: Invoice -->
    <div class="card card-purple">
      <div class="card-title">Invoice</div>
      <div class="card-value">52</div>
    </div>

    <!-- Kartu 4: Sertifikat -->
    <div class="card card-green">
      <div class="card-title">Sertifikat</div>
      <div class="card-value">85</div>
    </div>

    <!-- Kartu 5: Deadline -->
    <div class="card card-red">
      <div class="card-title">Deadline</div>
      <div class="card-value">7</div>
    </div>

    <!-- Kartu 6: Pendapatan -->
    <div class="card card-teal">
      <div class="card-title">Pendapatan</div>
      <div class="card-value">Rp230.000.000</div>
    </div>
  </div>
</main>
.dashboard-header {
  margin-bottom: 2rem;
}

.dashboard-header h1 {
  font-size: 1.75rem;
  color: #1e293b;
  margin: 0;
}

/* Grid Layout untuk Kartu */
.dashboard-grid {
  display: grid;
  /* Membuat kolom responsif: minimal lebar kartu 240px, maksimal mengisi sisa ruang */
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 1.5rem; /* Jarak antar kartu */
}

/* Gaya Dasar Kartu */
.card {
  background-color: #ffffff;
  border-radius: 0.5rem;
  padding: 1.5rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  border-left: 5px solid #cbd5e1; /* Default border kiri */
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.card-title {
  font-size: 0.875rem;
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.5rem;
}

.card-value {
  font-size: 1.75rem;
  font-weight: 700;
  color: #0f172a;
}

/* Variasi Warna Aksen Kartu (Border Kiri) */
.card-blue { border-left-color: #3b82f6; }
.card-orange { border-left-color: #f97316; }
.card-purple { border-left-color: #a855f7; }
.card-green { border-left-color: #22c55e; }
.card-red { border-left-color: #ef4444; }
.card-teal { border-left-color: #0d9488; }
import customtkinter as ctk

class Dashboard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        label = ctk.CTkLabel(
            self,
            text="Selamat Datang di HCMS",
            font=("Segoe UI", 24, "bold")
        )

        label.pack(pady=40)