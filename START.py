import subprocess

def run_programs(programs):
    for program in programs:
        try:
            result = subprocess.run(['python', program], check=True, capture_output=True, text=True)
            print(f"Output of {program}:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Error running {program}:\n{e.stderr}")

if __name__ == "__main__":
    programs_to_run = ['program1.py', 'program2.py', 'program3.py']  # Replace with your actual program file names
    run_programs(programs_to_run)