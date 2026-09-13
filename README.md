# 🛡️ Lightweight Python SAST Scanner

A lightweight Static Application Security Testing (SAST) engine designed to detect security vulnerabilities in Python source code using Abstract Syntax Tree (AST) analysis. 

Unlike traditional regex-based scanners, this tool parses the code into an AST, allowing for a deeper understanding of the code structure and significantly reducing false positives.

## ✨ Features

* **AST-Based Engine:** Parses Python code into an Abstract Syntax Tree (`ast` module) to accurately track function calls and data flows.
* **Pluggable Rule Set:** Vulnerability signatures are separated from the core logic and stored in a customizable `rules.yaml` file.
* **Academic Reporting:** Automatically generates structured LaTeX reports (`.tex`), making it exceptionally convenient to attach audit results as appendices to academic manuscripts and conference proceedings.

## 🚀 Installation & Usage

1. **Clone the repository:**
```bash
git clone [https://github.com/toricruel/my-sast-scanner.git](https://github.com/toricruel/my-sast-scanner.git)
cd my-sast-scanner
```

2. **Install dependencies:**
```bash
pip3 install pyyaml
```

3. **Run the scanner:**
```bash
python3 main.py test.py
```

## 🛠️ Configuration (rules.yaml)

You can easily expand the detection capabilities by adding new signatures to `rules.yaml` without changing the core engine. Example rule:

```yaml
rules:
  - id: "SEC-001"
    name: "Arbitrary Code Execution"
    functions: ["eval", "exec"]
    severity: "CRITICAL"
```

## 📊 Example Output

**Console:**
```text
Vulnerabilities detected:
- [CRITICAL] Arbitrary Code Execution found at line 2
LaTeX report 'report.tex' successfully generated!
```

**LaTeX Report (`report.tex`):**
The generated report is ready to be compiled into a PDF, pre-formatted with standard academic styling (A4 geometry, structured itemization).
