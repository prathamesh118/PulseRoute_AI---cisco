@echo off
title PulseRoute AI - Full Pipeline & Console Launcher
color 0A
echo ============================================================
echo       PULSEROUTE AI - FULL PIPELINE & DASHBOARD
echo ============================================================
echo.
echo [1/5] Extracting Evidence...
python evidence_extractor.py
echo.
echo [2/5] Running Deterministic Rules...
python rule_checker\checker.py
echo.
echo [3/5] Generating Diagnoses...
python ai\diagnosis_engine.py
echo.
echo [4/5] Generating Explanations...
python ai\explanation_engine.py
echo.
echo [5/5] Consolidating Final Telemetry...
python ai\final_result.py
echo.
echo ============================================================
echo Pipeline Execution Completed! Launching Dashboard...
echo ============================================================
echo.
python -m streamlit run dashboard/app.py
pause
