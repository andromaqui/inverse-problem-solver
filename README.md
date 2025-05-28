# Interactive Inverse Problem Visualizer with Regularization Techniques (1D & 2D)

This is a web-based interactive tool for solving 1D inverse problems using regularized curve fitting, and for performing basic image deblurring on 2D images. The backend is powered by **FastAPI** and **NumPy/SciPy**, while the frontend is built with **Vue 3**.

## Features

### 1D Inverse Solver
- Upload or enter X/Y data points
- Choose model types:
  - Linear, Exponential, Polynomial, Logistic, Sigmoid, Power-law
- Apply regularization:
  - L1, L2, Total Variation (TV), Total Generalized Variation (TGV)
- Adjust regularization strength (`alpha`) via slider
- Plot model fit and view estimated parameters

### 🖼2D Image Deblurring Tool
- View a blurred image (e.g., `cameraman_blurred.png`)
- Click "Unblur" to run a backend deblurring operation
- View deblurred result side-by-side

---

## Technologies

### Backend
- [FastAPI](https://fastapi.tiangolo.com/) – web API
- [NumPy](https://numpy.org/) – numerical computations
- [SciPy](https://scipy.org/) – optimization & deblurring
- [Pillow](https://python-pillow.org/) – image processing

### Frontend
- [Vue 3](https://vuejs.org/) + [Vite](https://vitejs.dev/) – modern UI framework
- Charting via reusable `<DataChart>` component

---

## 🧪 Running the App

### Backend (FastAPI)

```bash
# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Start the API
uvicorn main:app --reload
