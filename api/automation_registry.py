import os
import sys
import platform
import webbrowser
import psutil  # You'll need to install this: pip install psutil
import subprocess

class AutomationRegistry:
    """
    Registry of common automation functions for both Windows and macOS
    """
    
    # Application Control Functions
    @staticmethod
    def open_chrome(url="https://www.google.com"):
        """Open Chrome with a specified URL (defaults to Google)"""
        try:
            if platform.system() == "Darwin":  # macOS
                subprocess.run(["open", "-a", "Google Chrome", url])
            else:  # Windows
                webbrowser.get("chrome").open(url)
        except Exception as e:
            print(f"Error opening Chrome: {e}")
            webbrowser.open(url)  # Fallback to default browser

    @staticmethod
    def open_calculator():
        """Open the system calculator"""
        try:
            if platform.system() == "Darwin":
                subprocess.run(["open", "-a", "Calculator"])
            else:
                os.system("calc")
        except Exception as e:
            print(f"Error opening calculator: {e}")

    @staticmethod
    def open_notepad():
        """Open notepad (Windows) or TextEdit (macOS)"""
        try:
            if platform.system() == "Darwin":
                subprocess.run(["open", "-a", "TextEdit"])
            else:
                os.system("notepad")
        except Exception as e:
            print(f"Error opening text editor: {e}")

    @staticmethod
    def open_vscode(file_path=None):
        """Open VS Code, optionally with a specific file"""
        try:
            if platform.system() == "Darwin":
                cmd = ["open", "-a", "Visual Studio Code"]
                if file_path:
                    cmd.append(file_path)
                subprocess.run(cmd)
            else:
                cmd = "code"
                if file_path:
                    cmd += f" {file_path}"
                os.system(cmd)
        except Exception as e:
            print(f"Error opening VS Code: {e}")

    # System Monitoring Functions
    @staticmethod
    def get_cpu_usage():
        """Return current CPU usage percentage"""
        return psutil.cpu_percent(interval=1)

    @staticmethod
    def get_ram_usage():
        """Return RAM usage statistics"""
        mem = psutil.virtual_memory()
        return {
            "total": mem.total,
            "available": mem.available,
            "used": mem.used,
            "percent": mem.percent
        }

    @staticmethod
    def get_disk_usage():
        """Return disk usage statistics"""
        disk = psutil.disk_usage('/')
        return {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "percent": disk.percent
        }

    @staticmethod
    def get_system_info():
        """Return basic system information"""
        return {
            "system": platform.system(),
            "node": platform.node(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor()
        }

    # Command Execution Functions
    @staticmethod
    def run_command(command):
        """Run a shell command and return the output"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return {
                "success": True,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except subprocess.CalledProcessError as e:
            return {
                "success": False,
                "stdout": e.stdout,
                "stderr": e.stderr,
                "returncode": e.returncode
            }

    @staticmethod
    def execute_python_script(script_path):
        """Execute a Python script"""
        try:
            result = subprocess.run(
                [sys.executable, script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return {
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

# Example usage
if __name__ == "__main__":
    auto = AutomationRegistry()
    
    # Application control examples
    auto.open_chrome()
    auto.open_calculator()
    auto.open_notepad()
    
    # System monitoring examples
    print("CPU Usage:", auto.get_cpu_usage())
    print("RAM Usage:", auto.get_ram_usage())
    
    # Command execution examples
    print("System Info:", auto.get_system_info())
    print("Command Output:", auto.run_command("echo Hello World"))