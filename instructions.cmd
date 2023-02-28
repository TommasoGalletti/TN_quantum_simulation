REM Setup instructions:

pip install qibo

pip install numpy
pip install scipy
pip install numba
pip install cytoolz
pip install tqdm
pip install psutil

pip install opt_einsum
pip install autoray
pip install networkx

# Install STABLE
pip install qimb

# Install DEVELOPER (automatically uninstalls previous STABLE)
pip install --no-deps -U git+https://github.com/jcmgray/quimb.git@develop

REM pip list
REM Package            Version
REM ------------------ -------
REM autoray            0.5.3
REM cma                3.2.2
REM colorama           0.4.6
REM contourpy          1.0.7
REM cycler             0.11.0
REM cytoolz            0.12.1
REM fonttools          4.38.0
REM importlib-metadata 6.0.0
REM joblib             1.2.0
REM kiwisolver         1.4.4
REM llvmlite           0.39.1
REM matplotlib         3.6.3
REM mpmath             1.2.1
REM networkx           3.0
REM numba              0.56.4
REM numpy              1.23.5
REM opt-einsum         3.3.0
REM packaging          23.0
REM Pillow             9.4.0
REM psutil             5.9.4
REM pyparsing          3.0.9
REM python-dateutil    2.8.2
REM PyYAML             6.0
REM qibo               0.1.10
REM quimb              1.4.2
REM scipy              1.10.0
REM six                1.16.0
REM sympy              1.11.1
REM tabulate           0.9.0
REM toolz              0.12.0
REM tqdm               4.64.1
REM zipp               3.11.0


REM Running in Windows

python "c:\Users\tommy\OneDrive\Documenti\Python Scripts\example-circuit-1.py"
python "c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/qu - bell state.py"
python "c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/qu - GHZ state.py"
python "c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/qu - W state.py"
python "c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/qu - q full adder.py"


REM in Ubuntu (WSL)

python3 "/mnt/c/Users/tommy/OneDrive/Documenti/Python Scripts/example-circuit-1.py"