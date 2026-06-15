@echo off
setlocal EnableExtensions

:: ------------------------------------------------------------
:: CREATE/RECREATE mhtenv using Conda only for Python,
:: then pip for the Python package stack.
::
:: V2: avoids source builds for py7zr/pyzstd dependencies by
:: pinning the old wheel versions from the original environment.
:: ------------------------------------------------------------

set ENV_NAME=mhtenv
set PYTHON_VERSION=3.8.12

echo.
echo This script will create/recreate the Conda environment: %ENV_NAME%
echo Python version: %PYTHON_VERSION%
echo.

:: Make sure conda.bat is available inside this batch process.
if exist "%USERPROFILE%\anaconda3\condabin\conda.bat" (
    call "%USERPROFILE%\anaconda3\condabin\conda.bat" --version
) else (
    call conda --version
)

echo.
echo Removing existing %ENV_NAME% environment if present...
call conda env remove -n %ENV_NAME% -y >nul 2>nul

echo.
echo Creating clean environment...
call conda create -n %ENV_NAME% python=%PYTHON_VERSION% pip -y
if errorlevel 1 goto :fail

echo.
echo Activating environment...
call conda activate %ENV_NAME%
if errorlevel 1 goto :fail

:: Prevent user-site packages from leaking into this environment.
set PYTHONNOUSERSITE=1

echo.
echo Verifying interpreter and user-site isolation...
python -c "import sys, site; print('Python:', sys.executable); print('User site enabled:', site.ENABLE_USER_SITE); print('User site:', site.getusersitepackages())"
if errorlevel 1 goto :fail

echo.
echo Pinning pip tooling, while keeping Python 3.8 compatibility...
python -m pip install --upgrade "pip==24.3.1" "setuptools==69.5.1" "wheel==0.45.1"
if errorlevel 1 goto :fail

echo.
echo Installing core scientific packages...
python -m pip install --only-binary=:all: ^
    numpy==1.22.2 ^
    scipy==1.8.0 ^
    matplotlib==3.5.1 ^
    pillow==9.0.1 ^
    openpyxl==3.0.9 ^
    sympy==1.9 ^
    mpmath==1.2.1
if errorlevel 1 goto :fail

echo.
echo Installing MHT-X runtime packages...
python -m pip install ^
    networkx==2.6.3 ^
    tqdm==4.62.3 ^
    pandas==1.4.1 ^
    imageio==2.16.0 ^
    algorithm-x==0.1.0
if errorlevel 1 goto :fail

python -m pip install opencv-python-headless==4.5.5.64 --no-deps
if errorlevel 1 goto :fail

echo.
echo Installing pinned archive/7zip dependency wheels first...
:: Original conda env used:
::   py7zr 0.17.4, pyzstd 0.14.4, pyppmd 0.17.3,
::   pybcj 0.5.0, pycryptodomex 3.14.1, texttable 1.6.4.
:: Installing these first prevents pip from selecting a newer pyzstd
:: source distribution that requires Microsoft C++ Build Tools.
python -m pip install --only-binary=:all: ^
    pyzstd==0.14.4 ^
    pyppmd==0.17.3 ^
    pybcj==0.5.0 ^
    pycryptodomex==3.14.1 ^
    multivolumefile==0.2.3 ^
    texttable==1.6.4 ^
    brotli==1.0.9
if errorlevel 1 goto :fail

echo.
echo Installing py7zr without re-resolving its dependencies...
python -m pip install py7zr==0.17.4 --no-deps
if errorlevel 1 goto :fail

echo.
echo Installing project/support packages...
python -m pip install --only-binary=:all: ^
    wolframclient==1.1.7 ^
    requests==2.27.1 ^
    aiohttp==3.8.1 ^
    aiosignal==1.2.0 ^
    async-timeout==4.0.2 ^
    frozenlist==1.3.0 ^
    multidict==6.0.2 ^
    yarl==1.7.2 ^
    attrs==21.4.0 ^
    paramiko==2.8.1 ^
    bcrypt==3.2.0 ^
    cryptography==36.0.0 ^
    PyNaCl==1.4.0 ^
    cffi==1.15.0 ^
    pycparser==2.21 ^
    PyYAML==6.0 ^
    pyzmq==22.3.0 ^
    pytz==2021.3 ^
    oauthlib==3.2.0 ^
    certifi==2021.10.8 ^
    urllib3==1.26.8 ^
    charset-normalizer==2.0.4 ^
    idna==3.3
if errorlevel 1 goto :fail

echo.
echo Installing Spyder 5-era GUI stack...
:: Original Conda env used PyQt 5.12.x and Spyder 5.1.5.
python -m pip install --only-binary=:all: ^
    PyQtWebEngine==5.12.1 ^
    PyQt5==5.12.3 ^
    PyQtChart==5.12 ^
    spyder==5.1.5 ^
    spyder-kernels==2.1.3
if errorlevel 1 goto :fail

echo.
echo Running pip dependency check...
python -m pip check

echo.
echo Verifying important imports...
python -c "import sys, numpy, scipy, matplotlib, openpyxl, sympy, py7zr, pyzstd, wolframclient, spyder, spyder_kernels; from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR; print('Python:', sys.executable); print('numpy:', numpy.__version__); print('scipy:', scipy.__version__); print('matplotlib:', matplotlib.__version__); print('py7zr:', py7zr.__version__); print('pyzstd:', pyzstd.__version__); print('Spyder:', spyder.__version__); print('spyder-kernels:', spyder_kernels.__version__); print('Qt:', QT_VERSION_STR); print('PyQt:', PYQT_VERSION_STR)"
if errorlevel 1 goto :fail

echo.
echo Environment setup completed successfully.
echo.
echo To use it later:
echo     conda activate %ENV_NAME%
echo     set PYTHONNOUSERSITE=1
echo     spyder
echo.
goto :end

:fail
echo.
echo ERROR: Setup failed. Scroll up to find the first error message.
echo You can remove the partial env with:
echo     conda deactivate
echo     conda remove -n %ENV_NAME% --all -y
echo.
exit /b 1

:end
endlocal
