import subprocess

def run_program(program):
    try:
        result = subprocess.run(['python', program], check=True, capture_output=True, text=True)
        print(f"Output of {program}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {program}:\n{e.stderr}")

if __name__ == "__main__":
    programs_to_run = ['program1.py', 'program2.py', 'program3.py']  # Replace with your actual program file names
    print("Select a tool to run:")
    for i, program in enumerate(programs_to_run, 1):
        print(f"{i}. {program}")

    choice = int(input("Enter the number of the tool you want to run: "))
    if 1 <= choice <= len(programs_to_run):
        run_program(programs_to_run[choice - 1])
    else:
        print("Invalid choice")