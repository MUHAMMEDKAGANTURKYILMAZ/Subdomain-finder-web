
# 🔍 Ultra Full Subdomain Scanner v3.0

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

> **Professional subdomain enumeration tool powered by certificate transparency logs.**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Output Example](#output-example)
- [Troubleshooting](#troubleshooting)
- [Support](#support)
- [License](#license)

---

## 🎯 Overview

**Ultra Full Subdomain Scanner v3.0** is a powerful yet lightweight Python tool designed for security researchers, penetration testers, and bug bounty hunters to discover subdomains through certificate transparency (CT) logs.

Unlike brute-force scanners that guess subdomains, this tool queries real certificate databases that have recorded actual subdomains in use, providing highly accurate results with zero noise.

---

## ✨ Features

- 🚀 **Certificate Transparency Lookup** - Queries crt.sh database (most comprehensive source)
- 🎯 **Zero False Positives** - Only returns validated, existing subdomains
- 🧹 **Smart Filtering** - Automatically removes wildcards and duplicates
- 🎨 **Color-Coded Output** - Professional terminal interface
- 💾 **Auto-Save Results** - Exports clean list to text file
- ⚡ **Fast & Lightweight** - Single API call, instant results
- 🌐 **Global Database** - Searches all historical certificate records

---

## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Quick Install

```bash
# Install required dependencies
pip install requests colorama
