import sys
import subprocess
import pkg_resources

print("=" * 50)
print(f"Python: {sys.version}")
print(f"Executable: {sys.executable}")
print("=" * 50)

# Проверка установленных пакетов
required = {'playwright'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print(f"Отсутствующие пакеты: {missing}")
    print("Установите: pip install playwright")
else:
    print("✓ Playwright установлен")

    # Проверка версии playwright
    try:
        import playwright

        print(f"Версия playwright: {playwright.__version__}")
    except ImportError as e:
        print(f"Ошибка импорта: {e}")
print("=" * 50)