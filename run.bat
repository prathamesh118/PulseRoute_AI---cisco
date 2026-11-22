@echo off
title PulseRoute AI - Cyber-Ops Console Launcher
color 0B
echo ============================================================
echo         PULSEROUTE AI - AUTONOMOUS OPERATIONS CONSOLE
echo ============================================================
echo.
echo Launching Streamlit Cyber-Ops Dashboard...
echo URL: http://localhost:8501
echo.
python -m streamlit run dashboard/app.py
pause
