import run_exe
import create_exe
import time

def main():
    print("Creating executable...")
    executable = create_exe.create_exe("helloworld")

    time.sleep(1)

    print("Packing and executing executable file...")
    run_exe.run_exe(executable)

if __name__=="__main__":
    main()