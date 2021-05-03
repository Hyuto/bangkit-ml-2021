# BANGKIT 2021 - Machine Learning Path

<p align="center">
  <img src="Bangkit.png" />
</p>

```
Started   : Feb 2021
Completed : -
```

Semua aset, code dan bahan pembelajaran selama mengikuti program **Bangkit**

## Materi 

[ILTs Notebook](Notebook/README.md)

* February - March<br>
  1. [IT Automation](IT%20Automation/README.md) :heavy_check_mark:
  2. [IT Support Specialist](IT%20Supports%20Specialist/README.md) :heavy_check_mark:
  3. [Math for Machine Learning](Math%20for%20Machine%20Learning/README.md) :heavy_check_mark:
* March - April<br>
  1. [DeepLearning.AI TensorFlow Developer](DeepLearning.AI%20TensorFlow%20Developer/README.md) :heavy_check_mark:
* April - Mei<br>
  1. [Structuring Machine Learning Projects](Structuring%20Machine%20Learning%20Projects/README.md) :heavy_check_mark:
  2. [TensorFlow: Data and Deployment](TensorFlow%20-%20Data%20and%20Deployment/README.md) :heavy_check_mark:

## Run on Local?

### Install libraries

Install prerequisite library terlebih dahulu

**Windows via PIP**

```cmd
py -m pip install -r requirements.txt
```

**Linux via PIP**

```bash
pip install -r requirements.txt
```
### Note / Catatan

Gunakan `markserv` untuk view `markdown` file

**Install `markserv`**

```bash
cd bangkit-ml-2021
npm install -g markserv
```

**Serve**

```bash
npm run serve
```

### Exercise Notebook

Run `prepare.py` untuk menyiapkan data dan directory agar tidak terjadi error selama runtime.

:warning: **Note** : Data berukuran cukup besar sehingga disarankan untuk menggunakan wifi ketika `prepare.py` di jalankan.

Run `prepare.py` dan ikuti instruksinya

**Windows**

```cmd
py prepare.py
```

**Linux**

```bash
python3 prepare.py
```