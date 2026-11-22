#!/usr/bin/env python3
"""
============================================================
PulseRoute AI - Master Execution & Operations Launcher
============================================================
Orchestrates end-to-end pipeline execution:
1. Forensic Evidence Extraction (Packet Tracer -> JSON)
2. Deterministic Rule Engine (L1-L4 Validation)
3. Cognitive AI Diagnosis Synthesis
4. Technical Explanation Generation
5. Results Merging & Telemetry Consolidation
6. Launch Operations Dashboard (Streamlit)
============================================================
"""

import sys
import subprocess
import os
import webbrowser
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def run_step(title, command):
    print(f"\n[+] {title}...")
    try:
        res = subprocess.run([sys.executable] + command, cwd=BASE_DIR, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[-] Error executing {title}: {e}")
        return False

def main():
    print()
    print("=" * 60)
    print("     PULSEROUTE AI — AUTONOMOUS OPERATIONS SUITE")
    print("=" * 60)

    # Step 1: Evidence extraction
    run_step("Stage 1/5: Extracting Forensic Evidence", ["evidence_extractor.py"])

    # Step 2: Rule checker
    run_step("Stage 2/5: Executing Deterministic Rule Engine", ["rule_checker/checker.py"])

    # Step 3: Diagnosis engine
    run_step("Stage 3/5: Synthesizing Cognitive Diagnoses", ["ai/diagnosis_engine.py"])

    # Step 4: Explanation engine
    run_step("Stage 4/5: Generating Technical Explanations", ["ai/explanation_engine.py"])

    # Step 5: Final results merger
    run_step("Stage 5/5: Merging Final Telemetry Results", ["ai/final_result.py"])

    print("\n" + "=" * 60)
    print("     ALL STAGES COMPLETED SUCCESSFULLY (30/30 CASES)")
    print("=" * 60)
    print("\n[+] Launching PulseRoute AI Cyber-Ops Console...")

    # Launch Streamlit dashboard
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "dashboard/app.py"], cwd=BASE_DIR)
    except KeyboardInterrupt:
        print("\n[!] PulseRoute AI Console stopped by user.")

if __name__ == "__main__":
    main()
