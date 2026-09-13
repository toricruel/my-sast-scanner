import ast
import yaml
import sys

def load_rules():
    with open("rules.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["rules"]

def export_to_latex(findings, output_file="report.tex"):
    # LaTeX document template
    tex_content = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\geometry{a4paper, top=2cm, bottom=2cm, left=2.5cm, right=1.5cm}

\title{Appendix: Static Code Analysis Results}
% Specify only the actual co-authors below (those whose signatures were obtained)
\author{Author One \and Author Two} 
\date{Saint Petersburg, December 8--10, 2026}

\begin{document}
\maketitle

\section*{Introduction}
This report is generated automatically. The data presented below demonstrates practical vulnerability detection methods in the analyzed source code.

\section*{Detected Vulnerabilities}
\begin{itemize}
"""
    # Adding findings to the LaTeX list
    if not findings:
        tex_content += "    \\item No vulnerabilities detected.\n"
    else:
        for f in findings:
            # Basic escaping of special characters for safe LaTeX compilation
            safe_finding = str(f).replace("_", "\\_").replace("[", "{[").replace("]", "]}")
            tex_content += f"    \\item {safe_finding}\n"
            
    tex_content += r"""\end{itemize}
\end{document}
"""
    # Saving to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(tex_content)

class SecurityAnalyzer(ast.NodeVisitor):
    def __init__(self, rules):
        self.rules = rules
        self.findings = []

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            for rule in self.rules:
                if node.func.id in rule["functions"]:
                    self.findings.append(f"[{rule['severity']}] {rule['name']} found at line {node.lineno}")
        self.generic_visit(node)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <filename.py>")
        sys.exit(1)
    
    rules = load_rules()
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    
    analyzer = SecurityAnalyzer(rules)
    analyzer.visit(tree)
    
    if analyzer.findings:
        print("Vulnerabilities detected:")
        for f in analyzer.findings:
            print("-", f)
    else:
        print("No vulnerabilities found.")
        
    # Calling the export function
    export_to_latex(analyzer.findings)
    print("LaTeX report 'report.tex' successfully generated!")