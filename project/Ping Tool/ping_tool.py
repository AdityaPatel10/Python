import subprocess
import platform

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", host]
    
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Ping failed with error:\n{e.output}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    test_hosts = ["facebook.com"]
    for host in test_hosts:
        print(f"Pinging {host}...")
        ping(host)
        print("-" * 40)